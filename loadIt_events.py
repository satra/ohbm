import json
import urllib.request
events_url = 'https://dl.dropbox.com/s/7nb3wzrndmkoim1/ohbm2017_events.json?dl=0'
with urllib.request.urlopen(events_url) as url:
    events = json.loads(url.read().decode())

from elasticsearch import Elasticsearch
es = Elasticsearch(['http://elastic:changeme@localhost:9200/'])
"""
mapping = '''{
  "mappings":{
      "abstract" : {
        "properties" : {
          "startsOn" : {
              "type":"date",
              "format":"dd/MM/yyy HH:mm:ss"
            },
          "endsOn": {
              "type":"date",
              "format":"dd/MM/yyy HH:mm:ss"
            }
        }
      }
  }
}'''
es.indices.create(index='ohbm', ignore=400, body=mapping)
"""


for idx, d in enumerate(events):
    es.index(index='ohbm', doc_type='event', id=idx + 1, body=d)

