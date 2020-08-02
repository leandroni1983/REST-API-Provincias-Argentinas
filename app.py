from flask import Flask,render_template,Response
from bson import json_util
from baseapimongo import Baseprovincias

host ="http://localhost:5000/"
base ="mydatabase"
b=Baseprovincias(base,host)

app = Flask(__name__)

@app.route('/')
def get_Home():
    datos = b.gethome()
    return render_template('index.html',c=datos)

@app.route('/provincia')
def get_provincias():
    datos= b.getprovincias()
    return Response(json_util.dumps(datos,indent=4, sort_keys=True),mimetype='application/json')

@app.route('/provincia/<provincia_id>',methods=['GET'])
def get_provincia(provincia_id):
    datos =b.getprovincia(provincia_id)
    return Response(json_util.dumps(datos,indent=4, sort_keys=True),mimetype='application/json')
    
@app.route('/localidades')
def get_localidades():
    datos =b.getlocalidades()
    return Response(json_util.dumps(datos,indent=4, sort_keys=True),mimetype='application/json')

@app.route('/localidades/<provincia_id>',methods=['GET'])
def get_localidadesprovincia(provincia_id):
    datos =b.getlocalidadesprovincia(provincia_id)
    return Response(json_util.dumps(datos,indent=4, sort_keys=True),mimetype='application/json')



app.run(host="localhost")
#if __name__ == "__name__": app.run()
 