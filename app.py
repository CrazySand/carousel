from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有域访问


@app.route('/')
def index():
    # print(request.remote_addr)
    # 这里会渲染 templates 文件夹中的 index.html 文件
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
