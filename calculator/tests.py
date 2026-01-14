from django.test import TestCase, Client

class CalcTests(TestCase):
    def test_operacion_suma(self):
        c = Client()
        # Asegúrate de enviar n1, n2 y op exactamente así
        response = c.post('/', {'n1': '10', 'n2': '5', 'op': 'sumar'})
        
        self.assertEqual(response.status_code, 200)
        # Verificamos que 'resultado' existe en el contexto antes de comparar
        self.assertIn('resultado', response.context)
        self.assertEqual(response.context['resultado'], 15.0)