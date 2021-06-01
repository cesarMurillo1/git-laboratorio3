from django.test import SimpleTestCase,TestCase
from .models import curso,usuario,User
class testUrl(TestCase):
    @classmethod
    def setUp(self):
        self.usuario_1=usuario.objects.create()
    def test_text(self):
        self.assertEquals(self.curso_1.nombre, 'matematicas', msg='Equal')
        self.assertEquals(self.curso_1.nombre, 'matematicas', msg='Equal')
        self.assertEquals(self.curso_1.nombre, 'matematicas', msg='Equal')
