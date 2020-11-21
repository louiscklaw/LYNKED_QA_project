#!/usr/bin/env python3

import os,sys
from pprint import pprint
import json

import requests

def listAllTable():

  url = 'http://httpbin.org/cookies'

  LIST_TABLE_URL='http://menymeny.com/manage/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?home=lineup&query=lineup'
  MANAGE_TOKEN='c670dbb4543e8eab16cb1ce7510f145d94a84f419050e666bb914b083bdc6448ffd5d8551d93eebc11f9d46842e440d43459bc26b9ef7374b9ac1a6566ab0dc0'

  cookies = dict(manage_token=MANAGE_TOKEN)
  r = requests.get(LIST_TABLE_URL, cookies=cookies)

  try:
    if r.status_code != 200:
      raise Exception('end point not reachable')

    # print(r.status_code)
    TABLE_LIST_TEXT=r.text
    TABLE_LIST_JSON = json.loads(TABLE_LIST_TEXT)

    # pprint(TABLE_LIST_JSON)
    # print(list(map(lambda x: x['lid'], TABLE_LIST_JSON)))

    return TABLE_LIST_JSON
  except Exception as e:

    pass

if __name__ == '__main__':
  listAllTable()