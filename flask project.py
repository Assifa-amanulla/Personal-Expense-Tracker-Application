from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("&quot;/&quot;")
def home():
    return render_template("&quot;index.html&quot;")

@app.route("&quot;/login&quot;")
def login():
    return render_template("&quot;login.html&quot;")

@app.route("&quot;/about&quot;")
def about():
    return render_template("&quot;about.html&quot;")

if __name__ == "&quot;__main__&quot;":
    app.run()
