# -*- coding: utf-8 -*-

'''
model- 管理和数据库的交互

'''


class UserModel(object):

    #类变量
    #内存数据库,方便，重启后数据丢失
    users = {
        1: {'name':'zhang','age':10},
        2: {'name': 'wang', 'age': 12},
        3: {'name': 'li', 'age': 20},
        4: {'name': 'zhao', 'age': 30},
    }

    #获取单个用户
    @classmethod
    def get(cls,user_id):
        return cls.users[user_id]


    #获取所有用户
    @classmethod
    def get_all(cls):
        return list(cls.users.values())  #返回一个可迭代的对象

    #创建一个用户
    @classmethod
    def create(cls,name,age):
        user_dict = {'name':name,'age':age}
        max_id = max(cls.users.keys()) + 1      # 自增ID
        cls.users[max_id] = user_dict

    #更新用户年龄
    @classmethod
    def update(cls,user_id,age):
        # print('更新',age)
        cls.users[user_id]['age'] = age

    @classmethod
    def delete(cls,user_id):
        if user_id in cls.users:     #为了是幂等的
            return cls.users.pop(user_id)