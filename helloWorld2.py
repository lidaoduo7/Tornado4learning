# -*- coding: utf-8 -*-

'''


'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world2</h1>")   #渲染模版

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)     #  浏览器输入   http://localhost:8888
    tornado.ioloop.IOLoop.current().start()