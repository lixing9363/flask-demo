import os
from gevent.pywsgi import WSGIServer

from apps import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    # app.run()
    http_server = WSGIServer(('127.0.0.1', 5000), app, environ={"wsgi.multithread": True})
    http_server.serve_forever()
