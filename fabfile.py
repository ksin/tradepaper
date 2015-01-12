from fabric.api import lcd, local, hosts, run, cd, prefix, sudo, settings

def deploy_dev():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')
        local('pip install -r requirements.txt --allow-all-external')
        local('./manage.py runserver localhost:8000')

def prep_deploy():
    git_dir = '/webapps/trade-paper.com/tradepaper'
    with cd(git_dir):
        local('./manage.py test')
        local('git add -A .')
        with settings(warn_only=True):
            local('git commit')
        local('./manage.py makemigrations')
        local('./manage.py migrate')
        local('./manage.py test')
        local('git add -A .')
        with settings(warn_only=True):
            local('git commit -m "added migrations"')
        local('git push origin master')


@hosts('eli@beta.trade-paper.com')
def deploy_prod():
    app_dir = '/webapps/trade-paper.com'
    git_dir = '/webapps/trade-paper.com/tradepaper'
    with cd(git_dir), prefix('export DJANGO_SETTINGS_MODULE=tradepaper.settings.production'):
        run('git pull origin master')
        run('pip install -r requirements.txt --allow-all-external')
        run('./manage.py migrate')
        run('./manage.py collectstatic')
        run('./manage.py clear_cache')
        sudo('service nginx restart tradepaper')
    with cd(app_dir), prefix('export DJANGO_SETTINGS_MODULE=tradepaper.settings.production'):
        run('kill -HUP `cat tmp/gunicorn.pid`')

@hosts('eli@beta.trade-paper.com')
def update_prod():
    print('\n\nMake sure you update your dev environment first!')
    app_dir = '/webapps/trade-paper.com'
    git_dir = '/webapps/trade-paper.com/tradepaper'
    with cd(git_dir):
        run('git pull origin master')
        run('pip install -r requirements.txt --allow-all-external')
    with cd(app_dir):
        sudo('apt-get update')
        sudo('apt-get upgrade')

