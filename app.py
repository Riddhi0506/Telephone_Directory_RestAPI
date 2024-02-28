from flask import Flask, render_template, request, jsonify
# import Flask;
import re
import datetime
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="telephonedirectory"
)

def logging(action, name=None):
    now = datetime.datetime.now()
    with open('log.txt', 'a') as f:
        if name:
            log = f"{now} : {action} for {name}\n"
        else:
            log = f"{now} : {action}\n"
        f.write(log)

@app.route('/')
def home():
    return "Welcome to PhoneBook Application"

@app.route('/PhoneBook/add', methods=["POST"])
def Add():
    ID = request.form['ID']
    Name = request.form['Name']
    number_regex = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    # number_regex="^(00)?(011)?(\+)?[-.\s]?(1)?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$|^(\+45)?[\d\s]{8}$ | ^\d{3}[-.\s]?\d{4}$ | ^(\d{4})[.\s]\d{4}$ | ^(\d{2})[.\s]{3}\d{2}$ | ^\d{5}[.\s]?\d{5}$ | ^\+\d{2} \(\d{2}\) \d{3}\-\d{4}$"
    name_regex="[A-Za-z]{2,25}( [A-Za-z]{2,25})?"
    # name_regex = r"^([A-Za-z]+(?:[-']\w+)?),?\s+([A-Za-z]+(?:[-'\s]\w+)*)$ | [A-Za-z]{2,25}( [A-Za-z]{2,25})?"
    # name_regex = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?) | ^[A-Za-z]{2,25}( [A-Za-z]{2,25})?$"

    if not re.match(name_regex, Name):
        logging('Invalid name', Name)
        error = {'error': 'Invalid Name'}
        return jsonify(error), 400
    PhoneNumber = request.form['PhoneNumber']
    if not re.match(number_regex, PhoneNumber):
        logging('Invalid phone number', PhoneNumber)
        error = {'error': 'Invalid Phone Number'}
        return jsonify(error), 400
    print(ID, Name, PhoneNumber)
    mycursor = mydb.cursor()    
    sql = "INSERT INTO telephonedirectory (ID, Name, PhoneNumber) values (%s, %s, %s)"
    mycursor.execute(sql,(ID, Name, PhoneNumber, ))
    mydb.commit()
    mycursor.close()
    logging('Record added', Name)
    return ("Record Added Successfully", 200)


@app.route('/PhoneBook/deleteByNumber', methods=["PUT"])
def delByNumber():
    Phone = request.form['PhoneNumber']
    number_regex = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    # logging('Phone',Phone)
    # logging('regex',number_regex)
    if re.match(number_regex, Phone):
        error = {'error': 'Valid Phone Number'}

    else:
        error = {'error': 'Invalid Phone Number'}
        return jsonify(error), 400
    mycursor = mydb.cursor()
    sql = "DELETE FROM telephonedirectory WHERE PHONENUMBER=%s"
    mycursor.execute(sql,(Phone, ))
    mydb.commit()
    mycursor.close()
    logging('Record Deleted', Phone)
    return ("Record with Phone Number Deleted Successfully", 200)


@app.route('/PhoneBook/deleteByName', methods=["PUT"])
def delByName():
    Name = request.form['Name']
    name_regex="[A-Za-z]{2,25}( [A-Za-z]{2,25})?"
    if re.match(name_regex, Name):
        error = {'error': 'valid Name'}

    else: 
        error = {'error': 'Invalid Name'}
        return jsonify(error), 400
    mycursor = mydb.cursor()
    sql = "DELETE FROM telephonedirectory WHERE Name=%s"
    mycursor.execute(sql,(Name, ))
    mydb.commit()
    mycursor.close()
    logging('Record deleted', Name)
    return ("Record Deleted Successfully", 200)


@app.route('/PhoneBook/list', methods=["GET"])
def viewList():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM telephonedirectory")
    result = mycursor.fetchall()
    logging('Listed names')
    phonelist = []
    for row in result:
        phonelist.append((row[1], row[2]))
    return phonelist

if __name__ == "__main__":
    app.run(port=5000)
