from fabric.api import lcd, local, hosts, run, cd, prefix, sudo

def prep_deploy(branch_name):
    local('./manage.py test tradepaper')
    local('git add -A . && git commit')
    local('git push origin %s' % branch_name)

def deploy_dev():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')
        local('pip install -r requirements.txt --allow-all-external')

        #users app
        local('./manage.py syncdb')
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver localhost:8000')

@hosts('eli@beta.trade-paper.com')
def deploy_prod():
    app_dir = '/webapps/paper-py2'
    git_dir = '/webapps/paper-py2/tradepaper'
    with cd(git_dir):
        run('git pull origin master')
    with prefix('source %s/bin/activate' % app_dir):
        with cd(app_dir):
            run('pip install -r requirements.txt --allow-all-external')
        with cd(git_dir):
            run('./manage.py syncdb')
            run('./manage.py migrate users')
            run('./manage.py collectstatic')
            sudo('supervisorctl restart tradepaper')

def update_dev():
    with lcd('~/Documents/Apps/Django/dev/tradepaper/'):
        local('brew update')
        local('brew upgrade')
        with prefix('workon paper-py2'):
            local('pip install -r requirements.txt --allow-all-external')
            local('pip freeze > requirements.txt')

@hosts('eli@beta.trade-paper.com')
def update_prod():
    print('\n\nMake sure you update your dev environment first!')
    app_dir = '/webapps/paper-py2'
    git_dir = '/webapps/paper-py2/tradepaper'
    with cd(git_dir):
        run('git pull origin master')
    with cd(app_dir):
        sudo('apt-get update')
        sudo('apt-get upgrade')
        with prefix('source bin/activate'):
            run('pip install -r requirements.txt --allow-all-external')
