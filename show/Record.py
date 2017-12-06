from sqlalchemy.orm import mapper, sessionmaker

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql.expression import Cast
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.dialects.mysql import \
    BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
    DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

#功能:创建数据库表格，初始化数据库

#创建数据库连接，使用 mysqldb连接方式
mysql_db = create_engine("mysql+pymysql://root:377814789@localhost:3306/test")
# #绑定元信息
# metadata = MetaData(engine)

#表的属性描述对象
metadata = MetaData()

#创建表格，初始化数据库
record = Table('record', metadata,
             Column('id', Integer, primary_key = True),
             Column('pname', String(255)),
             Column('pid', String(255)),
             Column('rss', String(255)),
             Column('vms', String(255)),
             Column('cpu', String(255)) )

#创建一个映射类

class Record(object):
    __tablename__ = 'record'
    pname = Column(String(255))
    pid = Column(String(255))
    rss=Column(String(255))
    vms=Column(String(255))
    cpu=Column(String(255))
    id =Column(Integer, primary_key=True)


    def __init__(self, pname,pid,rss,vms,cpu):
        self.pname = pname
        self.pid = pid
        self.rss = rss
        self.vms = vms
        self.cpu=cpu
#把表映射到类
mapper(Record, record)
#创建了一个自定义了的 Session类
Session = sessionmaker()
#将创建的数据库连接关联到这个session
Session.configure(bind=mysql_db)
session = Session()

# session.execute('set names utf8')
# u=Record('123','555','5','d1[3]','d1[4]')
# i=session.add(u)
# print(i)
    #保存数据
# session.flush()
    #数据库事务的提交,sisson自动过期而不需要关闭
# session.commit()
# i = Record.insert()
# #print i
# #插入一组数据
# u=Record(pname='d1[0]',pid='d1[1]',rss='d1[2]',vms='d1[3]',cpu='d1[4]')
# #执行查询，第一个为查询对象，第二个参数为一个插入数据字典，如果插入的是多个对象
# #就把对象字典放在列表里边
# r1 = conn.execute(i, **u)
# print(r1)

# main()