#!/usr/bin/python3
#-*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)
pwd = "Victoruy10%40"
user = "victor"
uri = "mongodb+srv://" + user + ":" + pwd + "@cluster0.wozvku8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

database_name = 'todo'

# Funciones de api a hacer.



if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)