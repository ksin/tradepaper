from fabric.api import lcd, local, hosts, run, cd, prefix, sudo, settings

def deploy_dev():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')
        local('pip install -r requirements.txt --allow-all-external')
        local('./manage.py runserver localhost:8000')

@hosts('eli@beta.trade-paper.com')
def deploy_prod():
    app_dir = '/webapps/trade-paper.com'
    git_dir = '/webapps/trade-paper.com/tradepaper'
    with cd(git_dir), prefix('export DJANGO_SETTINGS_MODULE=tradepaper.settings.production'):
        run('git pull origin master')
        run('pip install -r requirements.txt --allow-all-external')
        run('./manage.py syncdb')
        run('./manage.py migrate users')
        run('./manage.py migrate papers')
        run('./manage.py collectstatic')

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

def migrate_local():
    local('./manage.py syncdb')
    with settings(warn_only=True):
        local('./manage.py schemamigration --auto users')
        local('./manage.py schemamigration --auto papers')
    local('./manage.py migrate users')
    local('./manage.py migrate papers')
