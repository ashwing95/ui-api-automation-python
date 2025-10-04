import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import pytest
import time
import threading
import requests
from mock_server.flaskapp import app
from werkzeug.serving import make_server


class ServerThread(threading.Thread):
    def __init__(self ,app ,host="127.0.0.1", port=5000):
        super().__init__(daemon=True)
        self.server = make_server(host,port,app)
        self.host = host
        self.port = self.server.server_port
        self.base_url = f"http://{self.host}:{self.port}"
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def wait_for_server(self , path="/get_users"):
        for _ in range(10):
            try:
                response = requests.get(f"{self.base_url}{path}")
                if response.status_code < 500 :
                    return
            except Exception:
                time.sleep(0.2)
        raise RuntimeError("Server did not start")


    def shutdown(self):
        self.server.shutdown()
        self.ctx.pop()

@pytest.fixture(scope="session")
def run_flask():
    """Start the Flask server  for all tests."""

    srv = ServerThread(app)
    srv.start()
    srv.wait_for_server()
    os.environ["API_URL"] = srv.base_url
    try:
        yield
    finally:
        srv.shutdown()
        srv.join(timeout=5)

