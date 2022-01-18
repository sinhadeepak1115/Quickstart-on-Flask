from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", gender=gender, age=age, name=name)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blogs = blog_response.json()
    return render_template("blog.html", posts=blogs)

if __name__ == "__main__":
    app.run(debug=True)
