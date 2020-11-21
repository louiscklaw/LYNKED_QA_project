#!/usr/bin/env python

import os,sys
from pprint import pprint
import json

import requests

url = 'http://httpbin.org/cookies'

LIST_TABLE_URL='http://menymeny.com/manage/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/lineup'
MANAGE_TOKEN='c670dbb4543e8eab16cb1ce7510f145d94a84f419050e666bb914b083bdc6448ffd5d8551d93eebc11f9d46842e440d43459bc26b9ef7374b9ac1a6566ab0dc0'

json_raw='{"lid":"5fb7f0f17f11c030c1f30cea","seat":"3"}'
payload_json = json.loads(json_raw)

cookies = dict(manage_token=MANAGE_TOKEN)


try:

  r = requests.post(LIST_TABLE_URL,cookies=cookies, json=payload_json)

  if r.status_code != 200:
    raise Exception('end point not reachable')

  print(r.text)

except Exception as e:
  pass

print('helloworld')