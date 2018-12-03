# -*- coding: utf-8 -*-

'''


'''

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("<h1>Hello, world2</h1>")   # 渲染模版
        self.render("base.html")

def make_app():
    return tornado.web.Application(
        [
        (r"/", MainHandler),
        ],
        template_path = os.path.join(
            os.path.dirname(__file__),"templates"
        ),
        debug=True    # 可自动重启服务器，方便调试
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)                            #  浏览器输入   http://localhost:8888
    tornado.ioloop.IOLoop.current().start()