#!/usr/bin/env python 
# -*- coding:utf-8 -*- 

import os 
from tornado.httpserver import HTTPServer 
from tornado.web import Application, RequestHandler 
from tornado.ioloop import IOLoop

from tornado.options import define, options
define("port",  default=8000, help="run on the given port", type=int)

class TestHandler(RequestHandler): 
    def get(self): 
        #import pdb
        #pdb.set_trace()
        self.write("Hello, World!\n")
        
class SignupHandler(RequestHandler):
    def get(self):
        self.render('signup.html')
    
class LoginHandler(RequestHandler):
    pass
    
class LogoutHandler(RequestHandler):
    pass
    
class EditPageHandler(RequestHandler):
    pass
    
class HistoryPageHandler(RequestHandler):
    pass
    
class WikiPageHandler(RequestHandler):
    pass
    
settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"), 
    "template_path" : os.path.join(os.path.dirname(__file__), "templates")
}

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
application = Application([
    (r"/", TestHandler), 
    (r'/signup', SignupHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/_edit' + PAGE_RE, EditPageHandler),
    (r'/_history' + PAGE_RE, HistoryPageHandler),
    (PAGE_RE, WikiPageHandler),
    ], **settings) 

if __name__ == "__main__": 
    server = HTTPServer(application) 
    server.listen(options.port) 
    IOLoop.instance().start() 
