import pymongo as pm
import os

client = pm.MongoClient(os.environ['MONGOKEY'])
db = client.botperrete
collection = db.tfbot

class Data:
    

"""
find_one
find

insert_one
insert_many

count_documents

create_index
"""