from flask import Flask, render_template, request, redirect, url_for, g
from base_datos.conexion import Conexion

app = Flask(__name__)

# Función para obtener la conexión a la base de datos
def obtener_conexion():
    conexion = getattr(g, '_conexion', None)
    if conexion is None:
        conexion = g._conexion = Conexion('base_datos/feria_del_plato.db')
    return conexion

# Antes de cada solicitud, establece la conexión a la base de datos
@app.before_request
def before_request():
    g.conexion = obtener_conexion()

# Después de cada solicitud, cierra la conexión a la base de datos
@app.teardown_request
def teardown_request(exception=None):
    conexion = getattr(g, '_conexion', None)
    if conexion is not None:
        conexion.cerrar_conexion(exception)
        g._conexion = None

# Página principal, simplemente redirige al panel de administración
@app.route('/')
def index():
    return redirect(url_for('admin_panel'))

# Panel de administración: muestra usuarios y productos
@app.route('/admin_panel')
def admin_panel():
    conexion = obtener_conexion()
    usuarios = conexion.mostrar_usuarios()
    productos = conexion.mostrar_productos()
    return render_template('admin.html', usuarios=usuarios, productos=productos)

# Agregar usuario: muestra formulario para agregar un nuevo usuario
@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    error = None
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        password = request.form['password'].strip()
        isAdmin = 1 if 'isAdmin' in request.form else 0
        
        # Validación: asegurar que nombre y password no estén vacíos
        if not nombre or not password:
            error = "Nombre y contraseña son campos obligatorios"
        else:
            conexion = obtener_conexion()
            if conexion.agregar_usuario(nombre, password, isAdmin):
                return redirect(url_for('admin_panel'))
            else:
                return "Error al agregar usuario"
    
    return render_template('agregar_usuario.html', error=error)

# Editar usuario: muestra formulario para editar un usuario existente
@app.route('/editar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    error = None
    conexion = obtener_conexion()
    usuario = conexion.obtener_usuario_por_id(usuario_id)
    
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        isAdmin = 1 if 'isAdmin' in request.form else 0
        
        # Validación: asegurar que nombre no esté vacío
        if not nombre:
            error = "Nombre es un campo obligatorio"
        else:
            if conexion.actualizar_usuario(usuario_id, nombre, isAdmin):
                return redirect(url_for('admin_panel'))
            else:
                return "Error al actualizar usuario"
    
    return render_template('editar_usuario.html', usuario=usuario, error=error)

# Borrar usuario: maneja la eliminación de un usuario
@app.route('/borrar_usuario/<int:usuario_id>', methods=['POST'])
def borrar_usuario(usuario_id):
    conexion = obtener_conexion()
    
    if conexion.borrar_usuario(usuario_id):
        return redirect(url_for('admin_panel'))
    else:
        return "Error al borrar usuario"

# Agregar producto: muestra formulario para agregar un nuevo producto
@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    error = None
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        
        # Validación: asegurar que todos los campos obligatorios no estén vacíos
        if not nombre or not descripcion:
            error = "Nombre y descripción son campos obligatorios"
        else:
            conexion = obtener_conexion()
            if conexion.agregar_producto(nombre, descripcion, stock, precio):
                return redirect(url_for('admin_panel'))
            else:
                return "Error al agregar producto"
    
    return render_template('agregar_producto.html', error=error)

# Editar producto: muestra formulario para editar un producto existente
@app.route('/editar_producto/<int:producto_id>', methods=['GET', 'POST'])
def editar_producto(producto_id):
    error = None
    conexion = obtener_conexion()
    producto = conexion.obtener_producto_por_id(producto_id)
    
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        
        # Validación: asegurar que todos los campos obligatorios no estén vacíos
        if not nombre or not descripcion:
            error = "Nombre y descripción son campos obligatorios"
        else:
            if conexion.actualizar_producto(producto_id, nombre, descripcion, stock, precio):
                return redirect(url_for('admin_panel'))
            else:
                return "Error al actualizar producto"
    
    return render_template('editar_producto.html', producto=producto, error=error)

# Borrar producto: maneja la eliminación de un producto
@app.route('/borrar_producto/<int:producto_id>', methods=['POST'])
def borrar_producto(producto_id):
    conexion = obtener_conexion()
    
    if conexion.borrar_producto(producto_id):
        return redirect(url_for('admin_panel'))
    else:
        return "Error al borrar producto"

# Manejador de error 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
