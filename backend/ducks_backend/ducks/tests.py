from django.test import TestCase
from .models import Duck
from ducks.serializers import DuckSerializer
class DuckModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creamos un objeto Duck de prueba para usar en las pruebas
        cls.duck = Duck.objects.create(name="Donald", age="5", location="Pond", image="donald.jpg")

    def test_name(self):
        self.assertEqual(str(self.duck), "Donald")

    def test_age_max_length(self):
        max_length = self.duck._meta.get_field('age').max_length
        self.assertEqual(max_length, 3) 


    def test_serialized_data(self):
        # Creamos una instancia del serializador y la inicializamos con nuestra instancia de Duck
        serializer = DuckSerializer(instance=self.duck)

        # Verificamos que los datos serializados coincidan con los datos esperados
        expected_data = {
            'id': self.duck.id,
            'name': self.duck.name,
            'age': self.duck.age,
            'location': self.duck.location,
            'image': self.duck.image.url if self.duck.image else None,
        }
        self.assertEqual(serializer.data, expected_data)
