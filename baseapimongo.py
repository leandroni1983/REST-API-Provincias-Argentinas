from flask import Flask,jsonify,Response
import pymongo
from bson import json_util


class Baseprovincias():

    def __init__(self,base,host):
        self.base = base
        self.host = host
        self.conn =  pymongo.MongoClient(self.host)
        self.db = self.conn[self.base]

    def gethome(self):
        self.data = self.db.provincias.find({'$query':{},"$orderby":{"id" : 1 }},{ "_id": 0,'id':1,'nombre':1})
        return self.data

    def getprovincias(self):
        self.data = self.db.provincias.find({},{ "_id": 0})
        return self.data
        
    def getprovincia(self,provincia_id):
        self.data = self.db.provincias.find({'id':provincia_id},{ "_id": 0})
        return self.data

    def getlocalidades(self):
        self.data = self.db.data_provs.find({},{ "_id": 0})
        return self.data
    
    def getlocalidadesprovincia(self,provincia_id):
        self.data = self.db.data_provs.find({'provincia_id':provincia_id},{ "_id": 0})
        return  self.data
