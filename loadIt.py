import json
import urllib.request
abstract_url = 'https://dl.dropbox.com/s/tlj4bd6d76jqpzi/ohbm2017_abstracts.json?dl=0'
with urllib.request.urlopen(abstract_url) as url:
    abstracts = json.loads(url.read().decode())
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
for idx, d in enumerate(abstracts):
    es.index(index='ohbm', doc_type='abstract', id=idx + 1, body=d)

