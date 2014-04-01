from fabric.api import lcd, local

def prep_deploy(branch_name):
    local('./manage.py sqlclear users')
    local('./manage.py syncdb')
    local('./manage.py test tradepaper')
    local('git add -A . && git commit')
    local('git push origin %s' % branch_name)

def deploy():
    with lcd('~/Documents/Apps/Django/tradepaper/'):
        local('git config --local --bool core.bare false ')
        local('git pull origin master')

        #users app
        local('./manage.py migrate users')
        local('./manage.py test users')
        local('./manage.py runserver 0.0.0.0:8000') #change this to prod server when you have one
