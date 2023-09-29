from flask import Flask , jsonify , request
from config_productor import config
import mysql.connector

conexion = mysql.connector.connect(

    user="root", password="Heropro.12",
    host='localhost',
    database="usuarios_api_rest",
    port="3306",
    
)
app = Flask(__name__)
app.config['SECRET KEY'] = '48f1f33c2c66a4ca6da7d9cf8b3617f5de86bd0e'

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        miCursor = conexion.cursor()
        miCursor.execute("select * from usuario;")
        datos = miCursor.fetchall() #es como un arraylist de arreglos
        usuarios=[]
        for fila in datos:
            usuario= {'usuario_id':fila[0],'nombre':fila[1],'clave':fila[2]}
            usuarios.append(usuario)
        
        return jsonify({'usuarios':usuarios , 'mensaje':'usuarios listados'})
    except Exception as ex:
        return jsonify({'mensaje':'no se pudo listar a los usuarios'})    
    
#se utiliza para recuperar información de un recurso específico o una colección de recursos    
@app.route('/usuarios/<usuario_id>', methods=['GET'])
def leer_usuario(usuario_id):
    try:
        miCursor = conexion.cursor()
        sql="SELECT UsuarioId, nombre, clave FROM usuario WHERE UsuarioId = '{0}';".format(usuario_id)
        miCursor.execute(sql)
        dato= miCursor.fetchone()
        print(dato)
        if dato != None:   
           usuario= {'usuario_id':dato[0],'nombre':dato[1],'clave':dato[2]}
           return jsonify({'usuario':usuario , 'mensaje':'usuario encontrado'})
        else:
           return jsonify({'usuario':usuario , 'mensaje':'usuario no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'error en el proceso'})
           
#POST se utiliza para enviar datos al servidor para crear un nuevo recurso
@app.route('/usuarios/registro', methods=['POST'])
def registrar_usuario():
    # print(request.json)
    try:
        miCursor = conexion.cursor()
        sql="INSERT INTO usuario(Nombre, Clave) VALUES('{0}','{1}')".format(request.json['nombre'],request.json['clave'])
        miCursor.execute(sql)
        conexion.commit()
        return jsonify({'mensaje':'usuario registrado con exito'})
    except:
        return jsonify({'mensaje':'error en el proceso'})
    
@app.route('/usuarios/<codigo>', methods=['GET'])
def borrar_usuario(codigo):
    try:
        miCursor = conexion.cursor()
        miCursor.execute("select * from usuario;")
        datos = miCursor.fetchall() #es como un arraylist de arreglos
        return
    except:
        return  
    
@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            print(request.json['nombre'])
            print(request.json['clave'])


        return jsonify({'mensaje':'usuario logeado'})
    except:
        return jsonify({'mensaje':'error en el proceso'})  
    
    
    
def pagina_no_encontrada(error):
    return "<h1>la pagina que intentas buscar no existe</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada), 404
    app.run()