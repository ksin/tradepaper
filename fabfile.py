from fabric.api import lcd, local

# env.user = 'eli'
# env.hosts = ['198.58.125.106']

def prep_deploy(branch_name):
    local('./manage.py test tradepaper')
    local('git add -A . && git commit')
    local('git push origin %s' % branch_name)

def deploy_staging():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')
        local('export DJANGO_SETTINGS_MODULE="../dev/tradepaper/tradepaper/settings/development.py"')
        local('echo $DJANGO_SETTINGS_MODULE')

        #users app
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver localhost:8000')

def deploy_prod():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull origin master')

        #users app
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver localhost:8000') #change this to prod server when you have one
