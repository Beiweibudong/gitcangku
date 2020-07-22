from flask import Flask,url_for
from flask import request
from flask import render_template
from models import session, User

app = Flask(__name__)
# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:/map_test?charset=utf8"'
# 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    page_index = request.args.get('page',1,type=int)
    #print('索引值为:'+str(page_index))
    #page_index = 1
    page_size = 9
    user_count = session.query(User).count()
    print('计数='+str(user_count))
    user = session.query(User).order_by(User.id).limit(
        page_size).offset((page_index-1)*page_size)
    page_num = user_count//page_size+1
    #user = session.query(User).order_by(User.id).all()
    return render_template('index.html', user=user,page_num=page_num)

@app.route('/search', methods=['GET','POST'])
def search():
    page_num = 0
    if request.method=='POST':
        name = request.values.get("username")
        #print(name)
        search_name = session.query(User).filter_by(name=name).all()
        #user = session.query(User).order_by(User.id).all()
        return render_template('index.html', user=search_name,page_num=page_num)


if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True)
    app.run(debug=True)
