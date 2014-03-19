#!/usr/bin/python
# coding:utf8

import os
from quixote.publish import Publisher

from webapp.views import RootDirectory
#from quixote.qwip import QWIP
from libs.gzipper import make_gzip_middleware
#from libs import show_performance_metric
from config import UPLOAD_DIR
import time

class Pub(Publisher):
    def __init__(self, *args, **kwargs):
        Publisher.__init__(self, *args, **kwargs)
        #self.configure(DISPLAY_EXCEPTIONS='plain', UPLOAD_DIR=UPLOAD_DIR)

    def start_request(self, request):
        os.environ['SQLSTORE_SOURCE'] = request.get_url()

        resp = request.response
        resp.set_content_type('text/html; charset=utf-8')
        resp.set_header('Expires', 'Sun, 1 Jan 2006 01:00:00 GMT')
        resp.set_header('Pragma', 'no-cache')
        resp.set_header('Cache-Control', 'must-revalidate, no-cache, private')
        request.enable_ajax = False
        request.browser = request.guess_browser_version()
        request.method = request.get_method()
        request.url = '/'
        request.start_time = time.time()

    def _generate_cgitb_error(self, request, original_response, exc_type, exc_value, tb):
        return "500"

def create_publisher():
    return Publisher(RootDirectory(),
            display_exceptions='plain')

#app = make_gzip_middleware(QWIP(create_publisher()))

if __name__ == '__main__':
    from quixote.server.simple_server import run
    print 'creating server listening on http://localhost:8000'
    run(create_publisher, host='localhost', port=8000)
