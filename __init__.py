# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
#
#
# app = Flask(
#     "visplatform",  # 如果报错改成__name__
#     template_folder='./templates',  # 搜索模板的入口
#     static_folder='.',  # 表示为搜索资源的入口
#     static_url_path='',  # 这是路径前缀, 个人认为非常蛋疼的设计之一, 建议传空字符串, 可以避免很多麻烦
# )
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
# app.config.from_pyfile('settings.py')
# db = SQLAlchemy(app)
#
# loginmanager = LoginManager(app)#loginmanager对象定义并对app初始化
# loginmanager.session_protection = "strong"#session保护登记
# loginmanager.login_view = "login"#如果访问需要登录的界面自动重定向到login界面
#
# from visplatform import views, filterW