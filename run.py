# encoding=utf-8
from flask import Flask,request
import json
import os
app = Flask(__name__)
@app.route('/')
def index():
    return '阿里云Docker触发'

@app.route('/docker/my_applet',methods=['POST'])
def my_applet():
    shell_path = '/****/******/******/update.sh'
    data = request.get_data()
    data = json.loads(data)
    tag = data['push_data']['tag']
    print(tag)
    if 'CACHE' not in tag:
        shell = shell_path +' '+tag
        print(shell)
        os.system(shell)
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True, port=35555)

# 部署 gunicorn app:app -b 0.0.0.0:35555 -w 2 -D