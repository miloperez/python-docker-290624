from flask import Flask
import numpy as np

app = Flask(__name__)

x = np.random.randint(10, size=1)

@app.route("/")
def hello():
    return 'Hello, World {}!\n'.format(x)

app.run(host="0.0.0.0")