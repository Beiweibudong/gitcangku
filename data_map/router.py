#!user/bin/env python3
#-*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from model import getdata
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:377814789@localhost:3306/map_test?charset=utf8"' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动

@app.route('/',methods=['GET','POST'])
def getMapdata():
    if request.method == 'POST':
        try:
            list2=getdata()
        except Exception as e:
           print(e)
        return json.dumps(list2)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)