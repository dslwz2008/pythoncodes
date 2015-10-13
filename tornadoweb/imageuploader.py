# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import tornado.ioloop
import tornado.web
import json

DATA_DIR = 'D:/data/images/testdb/'

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self, *args, **kwargs):
        result = {}
        try:
            if self.request.files.get('image') is not None:
                for pic in self.request.files['image']:
                    with open(DATA_DIR + pic['filename'], 'wb') as fp:
                        fp.write(pic['body'])
            result['success'] = True
        except:
            result['success'] = False
        finally:
            self.set_header('Content-Type', 'application/json')
            self.write(json.dumps(result))


application = tornado.web.Application([
    (r"/upload", UploadHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

