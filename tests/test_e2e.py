import requests
from multiprocessing import Process
import time
import sys
import os

# 把项目根目录加入 Python 搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app
def start_app():
    app.app.run(port=5000)

def test_root_endpoint():
    p = Process(target=start_app)
    p.start()
    time.sleep(1)  # 等服务起来

    res = requests.get("http://127.0.0.1:5000/")
    assert res.status_code == 200
    assert res.json().get("msg") == "OK"

    p.terminate()
