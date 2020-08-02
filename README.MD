# REST API Provincias Argentinas y Localidades
### Realizada con Python y Framework Flask,  DataBase con MongoDB.

Podes ver la api funcionando en:
https://provinciasapi.herokuapp.com/


Son necesarios de instalar los siguientes Paquetes complementarios

- pymongo
- flask
- dnspython (si deseas correr la base desde un servidor /servicio Cloud)

Para realizar las pruebas correspondientes  se recomienda montar y probar desde tu localhost,
utilice la app MongoDB Compass [Link Descarga y Documentacion](https://www.mongodb.com/try/download/compass)
donde tambien encontraras documentacion al respecto con los pasos a seguir
para que funcione sin tener que modificar el codigo deberas crear 
la base de datos con el nombre "mydatabase"
y las colecciones agregarlas con el mismo nombre de los archivos json incuidos en la carpeta datasets


si desdeas puedes contectarte desde una base en la nube con MongoDB
https://docs.atlas.mongodb.com/tutorial/create-new-cluster/ 
Tambien deberas modificar en app.py  la linea 5 por la direccion brindada al crear el cluster en Mongo Atlas
host ='mongodb://127.0.0.1:27017'





Sobre mi:
https://about.me/leandronicolas




