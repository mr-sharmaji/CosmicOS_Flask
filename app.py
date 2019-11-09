from flask import Flask, request, redirect, url_for, render_template
import json
import requests


app = Flask(__name__, static_url_path='/static')


@app.route('/',  methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/downloads', methods=['POST', 'GET'])
def download():
    api_request = requests.get("https://raw.githubusercontent.com/Cosmic-OS/platform_vendor_cos/corona-release/cosDevices.json")
    # with open("cosDevices.json") as f:
    #     api = json.load(f)
    api = json.loads(api_request.content)
    print(api)
    return render_template('downloads.html', api=api)


@app.route('/privacy-policy',  methods=['POST', 'GET'])
def privacy_policy():
    return render_template('p.html')


if __name__ == '__main__':
    app.run()
