from flask import Flask, request, jsonify
import pymongo
import logging
logging.basicConfig(filename="test2.log", level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')
app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://sanjay:sanjay11@cluster0.m69g2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['api_testing']
collection = database["api_test"]
@app.route('/mongo/insert',methods=['GET',"POST"])
def mongo_insert():
    try:
        if (request.method == 'POST'):
            data = request.get_json()
            collection.insert_one(data)
            return "successfully inserted into mongodb server"
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))
@app.route('/mongo/delete',methods=['GET',"POST"])
def mongo_delete():
    try:
        if (request.method == 'POST'):
            key = request.json['key']
            value = request.json['value']
            query = {key:value}
            print(query)
            collection.delete_one(query)
            return "successfully deleted from mongodb server"
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))

@app.route('/mongo/update',methods=['GET',"POST"])
def mongo_update():
    try:
        if (request.method == 'POST'):
            key = request.json['key']
            value = request.json['value']
            new_val = request.json['new_val']
            query = {key:value}
            set = {"$set":{key:new_val}}
            collection.update_one(query, set)
            return "successfully updated"
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))

@app.route('/mongo/fetch',methods=['GET',"POST"])
def mongo_fetch():
    try:
        if (request.method == 'POST'):
            key = request.json['key']
            value = request.json['value']
            query = {key:value}
            fetch = collection.find(query)
            return "successfully fetched from mongodb server : \n" + str([i for i in fetch])
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))

if __name__ =='__main__':
    app.run()

