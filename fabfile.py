from fabric.api import lcd, local

def prep_deploy(branch_name):
    local('./manage.py test tradepaper')
    local('git add -A . && git commit')

def deploy():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git pull ~/Documents/Apps/Django/dev/tradepaper/')
        local('git push origin master')

        #users app
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver 0.0.0.0:8000') #change this to prod server when you have one
