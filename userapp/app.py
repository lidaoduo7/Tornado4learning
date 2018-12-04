# -*- coding: utf-8 -*-

'''
使用Tornado构建RESTful微服务

'''


import tornado.web
from userapp.handlers import user as user_handlers

HANDLEERS = [
(r"/api/users", user_handlers.UserListHandler),
(r"/api/users/(\d+)", user_handlers.UserHandler),    #正则匹配
]

def run():
    app = tornado.web.Application(
        HANDLEERS,
        debug=True,   #方便自动重启做验证
    )
    http_server = tornado.httpserver.HTTPServer(app)    # http://localhost:8888/api/users
    port = 8888
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()