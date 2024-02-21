from flask import Flask
from leetcode import *

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/", methods=["GET"])
def homepage():
    return {"status":"ok","developer":"Devesh Singh"}

@app.route("/<username>", methods=["GET"])
def info(username):
    return {"status":"ok","message":"Coming Soon"}

@app.route("/profile/<username>", methods=["GET"])
def userprofile(username):
    return profile(username)

@app.route("/languagestats/<username>", methods=["GET"])
def langstat(username):
    return languagestat(username)

@app.route("/skillstats/<username>", methods=["GET"])
def skill(username):
    return skillstat(username)

@app.route("/contestranking/<username>", methods=["GET"])
def contest(username):
    return contestranking(username)

@app.route("/problemsolved/<username>", methods=["GET"])
def problems(username):
    return problemsolved(username)

@app.route("/badges/<username>", methods=["GET"])
def userbadges(username):
    return badges(username)

@app.route("/calendar/<username>", methods=["GET"])
def usercalandar(username):
    return calandar(username)

@app.route("/submissions/<username>", methods=["GET"])
def usersubmissions(username):
    return submissions(username)


app.run()