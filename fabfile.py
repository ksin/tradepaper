from fabric.api import lcd, local, hosts, run, cd

def prep_deploy(branch_name):
    local('./manage.py test tradepaper')
    local('git add -A . && git commit')
    local('git push origin %s' % branch_name)

def deploy_dev():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')
        local('export DJANGO_SETTINGS_MODULE=tradepaper.settings')
        local('echo $DJANGO_SETTINGS_MODULE')
        local('pip install -r requirements.txt --allow-all-external')

        #users app
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver localhost:8000')

@hosts('eli@beta.trade-paper.com')
def deploy_prod():
    app_dir = '/webapps/paper-py2/'
    git_dir = '/webapps/paper-py2/tradepaper'
    with cd(app_dir):
        run('source bin/activate')
        run('pip install -r requirements.txt --allow-all-external')
    with cd(git_dir), run('source ../bin/activate'):
        run('git pull origin master')
        run('export DJANGO_SETTINGS_MODULE=tradepaper.settings.production')
        run('echo $DJANGO_SETTINGS_MODULE')

        #users app
        run('./manage.py migrate users')
        run('./manage.py test users')
        run('./manage.py runserver localhost:8000')
