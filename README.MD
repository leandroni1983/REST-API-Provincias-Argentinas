# REST API Provincias Argentinas y Localidades
### Realizada con Python y Framework Flask,  DataBase con MongoDB.

Podes ver la api funcionando en:
[API Provincias](https://provinciasapi.herokuapp.com/)


#### Es necesario instalar los siguientes Paquetes complementarios
- pymongo
- flask
- dnspython (si deseas correr la base desde un servidor /servicio Cloud)

#### Puesta en marcha
Para realizar las pruebas correspondientes  se recomienda montar y probar desde tu localhost,
utilice la app MongoDB Compass [Link Descarga y Documentacion](https://www.mongodb.com/try/download/compass)
donde tambien encontraras documentacion al respecto.
Para que funcione sin tener que modificar el codigo deberas crear la base de datos con el nombre "mydatabase"
y las colecciones agregarlas con el mismo nombre de los archivos json incuidos en la carpeta datasets

Si desdeas puedes contectarte desde una base en la nube con MongoDB
[Crear Cluster Documentacion](https://docs.atlas.mongodb.com/tutorial/create-new-cluster/ )
y deberas modificar en app.py  
- 5 host ='mongodb://127.0.0.1:27017' <--  direccion del cluster.


Contactame: [**SobreMi**](https://about.me/leandronicolas)






