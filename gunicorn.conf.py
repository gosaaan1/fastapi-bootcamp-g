bind = '127.0.0.1:8000'
worker_class = 'uvicorn.workers.UvicornWorker'
loglevel = 'debug'
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '-'
proc_name = 'FastAPI Todo sample app'
