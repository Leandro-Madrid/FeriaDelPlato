import unittest
from models.Usuario import Usuario

class TestUsuario(unittest.TestCase):

    def test_guardar_en_db(self):
        # Mock de datos de usuario
        nombre = "test_user"
        password = "test_password"
        isAdmin = 1  # O 0 dependiendo de tus necesidades

        # Crear instancia de Usuario
        usuario = Usuario(nombre, password, isAdmin)

        # Probar guardar en la base de datos
        result = usuario.guardar_en_db()

        # Verificar que la inserción fue exitosa
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
