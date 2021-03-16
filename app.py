from flask import Flask,render_template
# 确定资源所在路径
app = Flask(__name__)

#装饰器定义路由
#flask调用视图函数，返回字符串或者html页面
@app.route('/')
def index():
    # return 'index 页面'
    return render_template('/templates/index.html')


if __name__ == '__main__':
    #执行后 flask程序运行在内置服务器上（测试）
    app.run()
