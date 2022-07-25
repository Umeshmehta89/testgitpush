import pymongo
client = pymongo.MongoClient("mongodb+srv://umesh89:<ukr123@mehta#>@cluster0.ztjryfy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)