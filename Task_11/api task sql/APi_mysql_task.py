from flask import Flask, request, jsonify
import mysql.connector as conn
mydb=conn.connect(host="localhost", user = "root", passwd="sanjay#11")
import logging
logging.info(mydb)
cursor = mydb.cursor()
app = Flask(__name__)
logging.basicConfig(filename="test.log", level= logging.INFO)

@app.route('/mysql/insert', methods=['GET',"POST"])
def sql_insert():
    try:
        if (request.method == "POST"):
            id = request.json['id']
            name = request.json['name']
            batch = request.json['batch']
            q1 = "insert into api_testing.api_test1 values({a},'{b}','{c}')".format(a=id, b=name, c=batch)
            cursor.execute(q1)
            mydb.commit()
            return jsonify("Record inserted successfully")
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))

@app.route('/mysql/update', methods=['GET',"POST"])
def sql_update():
    try:
        if (request.method == "POST"):

            id = request.json['id']
            col_name = request.json['col_name']
            new_value = request.json['new_value']
            cursor.execute("select * from api_testing.api_test1 where id = {a}".format(a=id))
            l=[i for i in cursor.fetchall()]
            q2 = "update api_testing.api_test1 set `{b}` = '{c}' where id = {a}".format(a=id, b=col_name, c=new_value)
            cursor.execute(q2)
            mydb.commit()
            cursor.execute("select * from api_testing.api_test1 where id = {a}".format(a=id))
            return jsonify("Record Updated Successfuly"+":"+str(l)+"---->"+str([i for i in cursor.fetchall() ]))
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))
@app.route('/mysql/delete', methods=['GET',"POST"])
def sql_del():
    try:
        if (request.method == "POST"):
            id = request.json['id']
            #q3 = "Delete from api_testing.api_test1 where id={a}".format(a=id)
            q3 = "Delete from api_testing.api_test1 where id={a}".format(a=id)
            cursor.execute(q3)
            mydb.commit()
            return jsonify("Record Deleted Successfully")
    except Exception as e:
        print(e)
        logging.exception(e)
        return jsonify(str(e))

@app.route('/mysql/fetch_record', methods=['GET',"POST"])
def sql_fetch():
    try:
        if (request.method == "POST"):
            fetch_all = request.json["fetch_all"]
            if fetch_all == "True" or fetch_all == "true" or fetch_all == "1" or fetch_all == "yes":
                s=""
                cursor.execute("select * from api_testing.api_test1")
                for i in cursor.fetchall():
                   s = s + str(i)
                return jsonify(s)
            else:
                id = request.json['id']
                cursor.execute("select * from api_testing.api_test1 where id={a}".format(a=id))
                for i in cursor.fetchall():
                    s = i
                return jsonify(s)
    except Exception as e:
        logging.exception(e)
        return jsonify(str(e))


if __name__ == '__main__':
     app.run()