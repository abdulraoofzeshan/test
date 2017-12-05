import pymongo
mongocli=pymongo.mongo_client
mongoC=mongocli.MongoClient(host='localhost',port=27017)
databaseobj=mongoC.get_database('zeshan')
mongo=databaseobj.create_collection('zeshan6')
mongo1=databaseobj.get_collection('zeshan6')
mongo1.insert({"k":1,"l":2,"j":8})
allrecobj=mongo1.find({})
print allrecobj.next()
print mongoC.drop_database('zeshan')
print mongo1.drop()




                            
