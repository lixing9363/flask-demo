import os
import sys

from apps import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2])
