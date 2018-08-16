#导入
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象基类
Base = declarative_base()

#定义对象
class User(Base):
    #表的名字
    __tablename__='user'
    #表结构
    id = Column(Integer,primary_key=True,autoincrement=True)
    work_no = Column(String(20))
    name = Column(String(20),nullable=False)
    mobile_phone = Column(String(20))
    office_phone = Column(String(20))
    department = Column(String(30))

#初始化数据库连接
engine = create_engine('mysql+pymysql://root:377814789@localhost:3306/map_test?charset=utf8')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)
session = DBSession()
#for x in session.query(User).filter(User.name=='汪文平'):
    #print(x.id,x.name,x.work_no,x.mobile_phone,x.department)