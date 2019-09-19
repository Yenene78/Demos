import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "6896a2e7a0d7488fb3c6828a934133a5"
BASE_URL = "https://api.cognitive.microsoft.com/bing/v7.0/localbusinesses/search"

@app.route("/", methods=["GET", "POST"])
def helloWorld():
	return render_template("index1.html")
@app.route("/ping", methods=["GET", "POST"])
def ping():
	headers = {'Ocp-Apim-Subscription-Key': API_KEY}
	params = {'q': request.args.get("q"), 'mkt': 'en-us', 'localCircularView':'47.6421, -122.13715, 5000'}
	ret = requests.get(url=BASE_URL, headers=headers, params=params)
	retList = json_to_obj(ret.text)
	retDic = {}
	for i in range(len(retList)):
		retDic[i] = retList[i]
	return json.dumps(retDic)

def json_to_obj(dict):
    my_dict = json.loads(dict)
    obj_list,obj_dict =[],{}
    values = my_dict['places']['value']
    key_list = ['name','geo','routablePoint']
    for value in values:
        curName = value["name"]
        curGeo = value["geo"]
        curAddress = value["address"]
        obj_list.append({'name':curName, 'geo':curGeo, 'address': curAddress})
    return obj_list

if(__name__ == "__main__"):
	app.run(host="0.0.0.0", port="8888", debug=True)