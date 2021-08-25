import unittest
from models import Client

class ClientTests(unittest.TestCase):
    def test_id_not_int(self):
        with self.assertRaises(TypeError) as error:
            Client("something", 'Nome1', 'email1@mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O ID do cliente deve ser um inteiro.')

    def test_name_not_str(self):
        with self.assertRaises(TypeError) as error:
            Client(1, 123, 'email1@mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O nome do cliente deve ser string.')

    def test_email_not_str(self):
        with self.assertRaises(TypeError) as error:
            Client(1, "Nome1", 123, '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O email do cliente deve ser string.')

    def test_cpf_not_str(self):
        with self.assertRaises(TypeError) as error:
            Client(1, "Nome1", 'email1@mail.com', 11122)
        
        self.assertEqual(error.exception.args[0], 'O CPF do cliente deve ser string.')
    
    def test_email_invalid(self):
        with self.assertRaises(TypeError) as error:
            Client(1, 'Nome1', 'email1mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'Email invalido.')
    
    def test_taxpayer_id_invalid(self):
        with self.assertRaises(TypeError) as error:
            Client(1, 'Nome1', 'email1@mail.com', '11122233vcb')
        
        self.assertEqual(error.exception.args[0], 'CPF invalido.')

if __name__ == "__main__":
    unittest.main()