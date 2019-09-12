import pymongo
from pymongo import MongoClient

client = MongoClient() # connects to client locally
db = client['my_db'] # get the database
produits = db['produit'] # get the connection




def our_insert_many(items, db, collection):
    if (items is NotImplemented):
        produits.insert_many(items)
    else:
        print('mongo error')