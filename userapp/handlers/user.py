# -*- coding: utf-8 -*-

'''


'''



import tornado.web
from userapp.models.user import UserModel
from tornado.escape import json_encode

# 用来处理批量的用户信息
class UserListHandler(tornado.web.RequestHandler):

    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))     #给定的Python对象序列化成一个字符串

    #创建一个用户
    def post(self):
        name = self.get_argument('name')   #获取参数
        age = self.get_argument('age')
        UserModel.create(name,age)
        resp = {'status':True,'msg':'create sucess'}  #返回信息
        self.write(json_encode(resp))

# 用来处理单个用户的增删改查
class UserHandler(tornado.web.RequestHandler):

    #获取单个用户信息
    def get(self,user_id):
        # print(user_id)
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)
        self.write(json_encode(user))


    #
    def put(self,user_id):
        age = self.get_argument('age')
        # print("更新为",age)
        UserModel.update(int(user_id),age)
        resp = {'status': True, 'msg': 'update sucess'}  # 返回信息
        self.write(json_encode(resp))


    #
    def delete(self, user_id):
        UserModel.delete(int(user_id))
        resp = {'status': True, 'msg': 'delete sucess'}  # 返回信息
        self.write(json_encode(resp))







