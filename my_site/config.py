from pymongo import MongoClient

client = MongoClient()

db = client['store_db']
db.Products.remove({})
# db['Products']

p1 = { 'ref':"BS-800",'title':"BS-800",'pu':60, 'inStock': 100}
p2 = { 'ref':"BS-77",'title':"BS-77",'pu':83, 'inStock': 300}
p3 = { 'ref':"TR-1000",'title':"TR-1000",'pu':19.5, 'inStock': 80}
p4 = { 'ref':"BS-500",'title':"BS-500",'pu':49, 'inStock': 635}
p5 = { 'ref':"BS-340",'title':"BS-340",'pu':15, 'inStock': 540}
p6 = { 'ref':"TR-5700",'title':"TR-5700",'pu':79.99, 'inStock': 26}
p7 = { 'ref':"BS-33",'title':"BS-33",'pu':99, 'inStock': 210}

db.Products.insert([p1,p2, p3, p4, p5, p6, p7])

# db.createCollection('Clients')
client = {'account_type': 'company','firstname': 'Anas', 'lastname': 'Erra', 'email': 'anas@mail.com', 'birth_date': '1898-8-7', 'address': {'nbr': 84, 'street': 'rue Tabakayo', 'apprt': '' ,'codePostal': 95684, 'city': 'Chinta', 'country':'Dreamland'}}
db.Clients.insert(client)

db.Sales.remove({})
paymentPerson1 = { 'firstname': 'John', 'lastname': 'Dank', 'eamil': 'john@mail.com', 'paymentMethod': {'type': 'Visa','code': '**** 7856', 'exp_date': '09/2020'}}
paymentPerson2 = { 'firstname': 'Anas', 'lastname': 'Erra', 'eamil': 'anas@mail.com', 'paymentMethod': {'type': 'Visa','code': '**** 3321', 'exp_date': '03/2025'}}
# sale = { 'ref': 'xF5oT3' ,'client': client, 'products': [p1, p3, p4], 'quantities': [2,8,3], 'shipping': 14, 'orderDate': '2019-09-05', 'payment': paymentPerson}
sale1 = { 'ref': 'xF5oT3' ,'client': client, 'product':  p4, 'quantity': 3, 'shipping': 14, 'orderDate': '2019-09-05', 'payment': paymentPerson1}
sale2 = { 'ref': 'xF5oT3' ,'client': client, 'product':  p3, 'quantity': 7, 'shipping': 1, 'orderDate': '2019-09-05', 'payment': paymentPerson1}
sale3 = { 'ref': 'xF5oT3' ,'client': client, 'product':  p2, 'quantity': 5, 'shipping': 0, 'orderDate': '2019-09-05', 'payment': paymentPerson1}
sale4 = { 'ref': 'Tj7U69' ,'client': client, 'product':  p7, 'quantity': 2, 'shipping': 0, 'orderDate': '2019-09-01', 'payment': paymentPerson2}
db.Sales.insert([sale1, sale2, sale3, sale4])

db.Factures.remove({})
db.Factures.insert({'ref': 'fac1','sales': [sale1, sale2, sale3]})


def get_all_products():
    return db.Products.find()

def get_Sale(clientName, refFacture):
    return db.Sales.find({'ref': refFacture,'client.firstname' : clientName})

def get_Sales(client):
    return db.Sales.aggregate([
        { '$match' : { 'client.firstname' : client } },
		{"$group" : {'_id': {'date':"$orderDate",'ref': '$ref'},'count': { '$sum': 1 }, 'totalPrice': { '$sum': { '$multiply': [ "$product.pu", "$quantity" ] } }}}
	])
    # return db.Sales.find({'ref': 'xF5oT3'})

def our_insert_many(items, db, collection):
    if (items is NotImplemented):
        db.Products.insert_many(items)
    else:
        print('mongo error')