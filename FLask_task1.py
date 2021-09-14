import json
from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:oracle@localhost/mohit1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
app.db = db
db.create_all()


@app.route('/emp', methods = ['GET'])
def emp():

    emp_data = Employees.query.all()
    global emp_all_data
    emp_all_data = []

    for row in emp_data:
        emp_all_data.append(row.id)
        emp_all_data.append(row.name)
        emp_all_data.append(row.contact)
        emp_all_data.append(row.password)
    # return str(emp_all_data)

    empall = json.dumps(emp_all_data, indent=4)
    return make_response(jsonify({"employees" : empall}))


@app.route('/rec', methods = ['GET'])
def rec():
    rec_data= Records.query.all()
    global rec_all_data
    rec_all_data = []

    for row in rec_data:
        rec_all_data.append(row.id)
        rec_all_data.append(row.name)
        rec_all_data.append(row.contact)
        rec_all_data.append(row.email)
        rec_all_data.append(row.password)

    # retur str(rec_all_data)
    recall = json.dumps(rec_all_data)
    return  jsonify({"records": recall})


@app.route('/emp2', methods=['POST'])
def create_emp():
    data={
        "id":"7",
        "Name":"ll",
        "Contact":"9895",
        "password":"ll123"
    }
    objSave=Employees()
    objSave.id = data["id"]
    objSave.name=data["Name"]
    objSave.contact=data["Contact"]
    objSave.password = data["password"]
    db.session.add(objSave)
    db.session.commit()

    emp_data = Employees.query.all()
    emp_all_data = []
    for row in emp_data:
        emp_all_data.append(row.id)
        emp_all_data.append(row.name)
        emp_all_data.append(row.contact)
        emp_all_data.append(row.password)
        # return str(emp_all_data)

    empall = json.dumps(emp_all_data, indent=4)
    return make_response(jsonify({"employees": empall}))

    return "succesfull", 200

@app.route('/rec2', methods = ['post'])
def create_rec():
    data={
        "id" : "4",
        "name" : "ss",
        "contact" : "9878",
        "email" : "ss@123",
        "password" : "ss344"
    }
    obj = Records()
    obj.id = data['id']
    obj.name = data['name']
    obj.contact = data['contact']
    obj.email = data['email']
    obj.password = data['password']
    db.session.add(obj)
    db.session.commit()

    rec_data = Records.query.all()
    rec_all_data = []
    for row in rec_data:
        rec_all_data.append(row.id)
        rec_all_data.append(row.name)
        rec_all_data.append(row.contact)
        rec_all_data.append(row.email)
        rec_all_data.append(row.password)

    recall = json.dumps(rec_all_data,indent=4)
    return jsonify({"Records": recall})


class Employees(db.Model):

    __tablename__ = 'employees'

    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    contact = db.Column(db.Integer)
    password = db.Column(db.String(30))


class Records(db.Model):

    __tablename__ = 'records'

    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    contact = db.Column(db.Integer)
    email = db.Column(db.String(100))
    password = db.Column(db.String(30))


if __name__ == '__main__':
    app.run()

