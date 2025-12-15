import requests
import time
import pytest
from multiprocessing import Process
import sys
import os

# add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def start_app():
    app.app.run(port=5001)

@pytest.mark.timeout(10)
def test_performance():
    p = Process(target=start_app)
    p.start()
    time.sleep(1)

    start = time.time()
    for i in range(20):  # send 20 consecutive requests
        res = requests.get("http://127.0.0.1:5001/")
        assert res.status_code == 200
    end = time.time()

    p.terminate()

    total = end - start
    print(f"20 requests took ≈ {total:.2f} seconds")
    assert total < 5  # ensure it takes less than 5 seconds for 20 requests
