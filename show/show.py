import json

import sys
from datetime import datetime

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy, Model

from Record import Record, session
from t1 import postData, postData1, postData2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:377814789@localhost:3306/test' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动




# sql = "insert into record(pname, pid,rss,vms,cpu) values (%s, %s,%s,%s，%s)"
# name, pid, rss * 100 / total_mem, vms * 100 / total_mem, cpu,cpio
@app.route('/' , methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        try:
            for d1 in postData1():
                if d1 is not None :
                    u=Record(d1[0],d1[1],d1[2],d1[3],d1[4])
                    session.add(u)
            session.commit()
        except Exception as e:
           print(e)
        return json.dumps(postData2())
    else:
        return render_template('index.html')

@app.route('/list' , methods=['GET', 'POST'])
def list():
    if request.method == 'POST':
        return json.dumps(postData1())
    else:
        return render_template('list.html')


@app.route('/bing' , methods=['GET', 'POST'])
def bing():
    if request.method == 'POST':
        try:
            for d1 in postData1():
                if d1 is not None :
                    u=Record(d1[0],d1[1],d1[2],d1[3],d1[4])
                    session.add(u)
            session.commit()
        except Exception as e:
            print(e)
        return json.dumps(postData())
    else:
        return render_template('bing.html')

if __name__ == '__main__':
    app.run(debug=True)