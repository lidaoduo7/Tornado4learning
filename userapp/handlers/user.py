# -*- coding: utf-8 -*-

'''


'''



import tornado.web
from userapp.models.user import UserModel
from tornado.escape import json_encode

class UserListHandler(tornado.web.RequestHandler):

    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        UserModel.create(name,age)
        resp = {'status':True,'msg':'create sucess'}
        self.write(json_encode(resp))




