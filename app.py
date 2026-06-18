import os
import random
import string
import requests
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me")


def get_surl(url):
  

 burl = "https://q1llke7695.execute-api.us-east-1.amazonaws.com/shortit"
 body={
    "url":url
 }

 response = requests.post(burl,json=body)
 scode=response.json()["short_code"]
 u=f"https://q1llke7695.execute-api.us-east-1.amazonaws.com/{scode}"
 return u



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():
    original_url = request.form.get("url", "").strip()
    if not original_url:
        flash("Please enter a valid URL.", "warning")
        return redirect(url_for("index"))

    short_url=get_surl(original_url)

    return render_template("index.html", short_url=short_url, original_url=original_url)


if __name__ == "__main__":
    app.run(debug=True)
