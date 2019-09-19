import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "6896a2e7a0d7488fb3c6828a934133a5"
BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/localbusinesses/search"

@app.route("/", methods=["GET", "POST"])
def helloWorld():
	return render_template("index.html")
@app.route("/ping", methods=["GET", "POST"])
def ping():
	headers = {'Ocp-Apim-Subscription-Key': API_KEY}
	params = {'q': request.args.get("q"), 'mkt': 'en-us'}
	ret = requests.get(url=BASE_URL, headers=headers, params=params)
	return json.dumps(ret.json(), indent=4)

if(__name__ == "__main__"):
	app.run(host="0.0.0.0", port="8888", debug=True)