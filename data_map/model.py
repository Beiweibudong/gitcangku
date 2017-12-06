#!user/bin/env python3
#-*- coding:utf-8 -*-

from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象基类
Base = declarative_base()
#定义map对象
class Map(Base):
    #表的名字:
    __tablename__='mapdata' 
    id = Column(Integer,primary_key = True)
    zone = Column(String(255))
    premium = Column(String(255))
#获取数据并整理成指定格式
def getdata():
    #创建初始化数据库连接
    engine = create_engine("mysql+pymysql://root:377814789@localhost:3306/map_test?charset=utf8")    
    #创建DBsession类型：
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    mapdata = session.query(Map).filter().all()
    x=0
    list1=[]
    while x<len(mapdata):
        dictto = {'name':mapdata[x].zone,'value':mapdata[x].premium}
        x=x+1
        list1.append(dictto)
        #print(dictto['name'],dictto['value'])
        #for key,values in dictto.items():
            #print(key,values+',',end='')
    return list1
#if __name__ == '__main__':
#    getdata()

