# -*- coding: utf-8 -*-

'''


'''

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("<h1>Hello, world2</h1>")   #渲染模版
        self.render("base.html")


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("500.html")

def make_app():
    return tornado.web.Application(
        [
        (r"/", MainHandler),
        (r"/500", ErrorHandler),               #  浏览器输入   http://localhost:8888/500
        ],
        template_path = os.path.join(
            os.path.dirname(__file__),"templates"
        ),
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)     #  浏览器输入   http://localhost:8888
    tornado.ioloop.IOLoop.current().start()