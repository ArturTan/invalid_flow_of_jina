import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/")
def response():
    return 200


if __name__ == "__main__":
    subprocess.call("python3 app.py -t index".split())
    app.run(host="0.0.0.0", port=8888)


