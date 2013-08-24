#!/usr/bin/env python 
# -*- coding:utf-8 -*- 

import os
import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tempfile
from PIL import Image
import dbengine

from tornado.options import define, options
import json

define("port", default=8000, help="run on the given port", type=int)

settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"), 
    "template_path" : os.path.join(os.path.dirname(__file__), "templates")
}

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input)

class WrapHandler(tornado.web.RequestHandler):
    def get(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 10)
        if isinstance(width, basestring):
            width = int(width)
        self.write(textwrap.fill(text, width))

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')
        
class AutoescapeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("autoescape.html")
    def post(self):
        words = self.get_argument('words')
        print words
        #self.write('test:'.join(words))
        #neccessary!
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + words)

class FileUploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('fileupload.html')
    def post(self):
        if self.request.files:
            for file in self.request.files['picture']:
                rawname = file['filename']
                dstname = 'jyblog_'+rawname
                thbname = 'thumb_'+dstname
                tf = tempfile.NamedTemporaryFile()
                tf.write(file['body'])
                tf.seek(0)
                
                img = Image.open(tf.name)
                img.thumbnail((920,920),resample=1)
                img.save("static/upload/"+dstname)
                # create thumb file
                img.thumbnail((100,100),resample=1)
                img.save("static/upload/"+thbname)
                tf.close()

class AjaxTestHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name')
        location = self.get_argument('location')
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps({'a':'aa','b':'bb'}))

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('testajax.html')

class ShipInfoHandler(tornado.web.RequestHandler):
    def get(self):
        page = self.get_argument('page')
        rows = self.get_argument('rows')
        sidx = self.get_argument('sidx')
        sord = self.get_argument('sord')
        shipinfos = dbengine.show_shipinfo(page,rows,sidx,sord)
        print shipinfos
        result = {}
        result['page'] = 1
        result['total'] = 1
        result['records'] = 10
        result['rows'] = []
        index = 0
        for si in shipinfos:
            temp = {}
            temp['id'] = index
            temp['cell'] = [index, si['name'], si['beidou'], si['owner'], si['tele'], si['power'], si['port'], si['worktype']]
            result['rows'].append(temp)
            index = index + 1
        self.set_header('Content-Type','application/json')
        self.set_header("Access-Control-Allow-Origin", "http://192.148.140.158")
        self.write(json.dumps(result))
        #self.set_header('Content-Type','text/plain')
        #self.write('test,test,test')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), 
            (r'/reverse/(\w+)', ReverseHandler),
            (r'/wrap', WrapHandler),
            (r'/autoescape', AutoescapeHandler),
            (r'/fileupload', FileUploadHandler),
            (r'/ajaxtest', AjaxTestHandler),
            (r'/test', TestHandler),
            (r'/shipinfo', ShipInfoHandler)
                  ], **settings
                  )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
