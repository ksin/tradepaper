pidfile = '/webapps/trade-paper.com/tmp/gunicorn.pid'
bind = 'tp.elibierman.com:8888'
workers = 3
accesslog = '/webapps/trade-paper.com/logs/gunicorn-access.log'
errorlog = '/webapps/trade-paper.com/logs/gunicorn-error.log'
loglevel = 'debub'
