# -*- coding: utf-8 -*-
import requests;
import json;

def send_messag_example():
	resp = requests.post(("https://sms-api.luosimao.com/v1/send.json"),
	auth=("api", "key-..."),
    data={
		"mobile": "...",
		"message": "hello,wolrd【发达是】"
	},timeout=3 , verify=False);
	result =  json.loads( resp.content )
	print result

if __name__ == "__main__":
    send_messag_example();
