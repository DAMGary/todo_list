#!/usr/bin/python3
#-*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
pwd = "Victoruy10%40"
user = "victor"
uri = "mongodb+srv://" + user + ":" + pwd + "@cluster0.wozvku8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

database_name = 'todo'

# Crea un nuevo usuario
# curl -X POST -H "Content-Type: application/json" -d '{"nom":"Victor Alberto", "nickname":"victoruy", "password":"1234"}' http://localhost:5000/usuaris
@app.route('/usuaris', methods=['POST'])
def create_usuari():
    data = request.get_json() # request the whole data
    if not data:
        return jsonify({"message": "Informacion no introducida"}), 400
    usuari = {
        "nom": data.get("nom"),
        "nickname": data.get("nickname"),
        "password": data.get("password"),
    }
    if client[database_name].usuaris.find_one({'nickname': usuari.get("nickname")}) is None:
       client[database_name].usuaris.insert_one({'nom':usuari.get("nom"),'nickname':usuari.get("nickname"),'password':usuari.get("password")})
       return "Created", 201
    else: return "", 409

# Muestra todo los usuarios
@app.route('/usuaris',methods=['GET'])
def get_usuaris():
    usuaris = client[database_name].usuaris.find()
    response = []
    for usuari in usuaris:
        response.append({
            '_id': str(usuari['_id']),
            'nickname': usuari['nickname'],
            'nom': usuari['nom'],
            'password': usuari['password']
        })
    return jsonify(response), 201

# curl -X POST -H "Content-Type: application/json" -d '{"nickname":"victoruy", "password":"1234"}' http://localhost:5000/login
@app.route('/login', methods=['POST'])
def login_usuari():
    data = request.get_json() # request the whole data
    if not data:
        return jsonify({"message": "Informacion no introducida"}), 400
    usuari = {
        "nickname": data.get("nickname"),
        "password": data.get("password"),
    }
    find_user = client[database_name].usuaris.find_one({'nickname':usuari.get("nickname")})
    if find_user and find_user["password"] == usuari.get("password"):
        return jsonify({"message": "Logeado correctamente"}), 201
    else:
        return "Forbidden", 403



if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
