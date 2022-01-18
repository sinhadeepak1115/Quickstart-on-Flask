from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/guess/<name>")
def guess(name):
    return "<p>bye Deepak</p>"

if __name__ == "__main__":
    app.run(debug=True)

