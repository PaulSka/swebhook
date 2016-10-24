# coding: utf-8 

"""
Simple Flask Webhook
"""

from flask import Flask, request
import json
import requests

app = Flask(__name__)

UUID = "f0819446-394c-4c16-ab41-60222995ba17" #Change if you want

@app.route('/%s/<hook>' %UUID, methods=['POST'])
def call_hook(hook):
	data_json_hook = request.get_json()
	return "OK"
	

if __name__ == '__main__':
	app.run(debug=True)