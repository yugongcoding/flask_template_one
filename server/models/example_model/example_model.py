# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Float, JSON, DATE, Text
from sqlalchemy.ext.declarative import declarative_base
from server.dbs.db import engine_one, session_zs
# 创建基础的元数据
base_one = declarative_base()


# 创建表对象orm,继承base_one
# 这里类名User就相当于数据库的表映射成的对象
# __tablename__指定我们的表名
# id name sex指定了类的属性，对应数据库表的字段名
class User(base_one):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    sex = Column(JSON)


if __name__ == '__main__':
    import json
    # 创建所有的与base_one关联的实体表
    base_one.metadata.create_all(bind=engine_one)
