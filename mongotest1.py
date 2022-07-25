import pymongo
client = pymongo.MongoClient("mongodb+srv://umesh89:<ukr123>@cluster0.ztjryfy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name": "umesh", "surname": "kumar", "email": "umesh@ineuron.ai"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
