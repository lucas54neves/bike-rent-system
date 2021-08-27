import unittest
from models import Client, Store

class ClientTests(unittest.TestCase):
    def test_id_is_not_int(self):
        with self.assertRaises(TypeError) as error:
            Client("something", 'Nome1', 'email1@mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O ID do cliente deve ser um inteiro.')

    def test_name_is_not_str(self):
        with self.assertRaises(TypeError) as error:
            Client(1, 123, 'email1@mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O nome do cliente deve ser string.')

    def test_email_is_not_str(self):
        with self.assertRaises(TypeError) as error:
            Client(1, "Nome1", 123, '11122233344')
        
        self.assertEqual(error.exception.args[0], 'O email do cliente deve ser string.')

    def test_cpf_is_not_str(self):
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

class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store('Loja de bikes', 'Rua Um, 123')
    
    def test_attributes(self):
        self.assertEqual(self.store.name, 'Loja de bikes')
        self.assertEqual(self.store.address, 'Rua Um, 123')
        self.assertEqual(self.store.clients, [])
        self.assertEqual(self.store.rentals, []) 
        self.assertEqual(self.store.bikes, [])              
    
    def test_name_is_not_string(self):
        with self.assertRaises(TypeError) as error:
            Store(123, 'Rua Um, 123')
        
        self.assertEqual(error.exception.args[0], 'O nome da loja deve ser string.')
    
    def test_address_is_not_string(self):
        with self.assertRaises(TypeError) as error:
            Store('Loja de bikes', [])
        
        self.assertEqual(error.exception.args[0], 'O endereco da loja deve ser string.')
    
    def test_client_already_added(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        with self.assertRaises(TypeError) as error:
            self.store.addClient('Nome1', 'email1@mail.com', '11122233344')
        
        self.assertEqual(error.exception.args[0], 'Cliente ja cadastrado.')
    
    def test_type_rent_invalid(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        with self.assertRaises(ValueError) as error:
            self.store.addRental('monthly', 'email1@mail.com', 1)
        
        self.assertEqual(error.exception.args[0], 'Tipo de aluguel invalido.')
    
    def test_quantity_rent_is_not_int(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        with self.assertRaises(TypeError) as error:
            self.store.addRental('weekly', 'email1@mail.com', "1")
        
        self.assertEqual(error.exception.args[0], 'A quantidade de alugueis deve ser inteira.')
    
    def test_bikes_unavailable_for_rental(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        with self.assertRaises(KeyError) as error:
            self.store.addRental('weekly', 'email1@mail.com', 1)
        
        self.assertEqual(error.exception.args[0], 'Bicicleta indisponivel.')
    
    def test_client_of_the_not_registered(self):
        self.store.addBike('Branco')

        with self.assertRaises(KeyError) as error:
            self.store.addRental('weekly', 'email1@mail.com', 1)
        
        self.assertEqual(error.exception.args[0], 'Cliente nao cadastrado.')
    
    def test_family_rent_must_be_between_two_and_five(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(5):
            self.store.addBike('Branco')

        with self.assertRaises(ValueError) as error:
            self.store.addRental('weekly', 'email1@mail.com', 1, True)
        
        self.assertEqual(error.exception.args[0], 'Aluguel para familia deve ser de 3 a 5 emprestimos.')
    
    def test_hourly_rental(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        self.store.addBike('Branco')

        self.store.addRental('hourly', 'email1@mail.com', 1)
        
        self.assertEqual(self.store.rentals[0]['model'], 'hourly')
        self.assertEqual(len(self.store.rentals), 1)
    
    def test_daily_rental(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        self.store.addBike('Branco')

        self.store.addRental('daily', 'email1@mail.com', 1)
        
        self.assertEqual(self.store.rentals[0]['model'], 'daily')
        self.assertEqual(len(self.store.rentals), 1)
    
    def test_weekly_rental(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        self.store.addBike('Branco')

        self.store.addRental('weekly', 'email1@mail.com', 1)
        
        self.assertEqual(self.store.rentals[0]['model'], 'weekly')
        self.assertEqual(len(self.store.rentals), 1)
    
    def test_three_family_rentals(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(3):
            self.store.addBike('Branco')

        self.store.addRental('weekly', 'email1@mail.com', 3, True)

        for rent in self.store.rentals:
            self.assertNotEqual(rent['start'], None)
            self.assertEqual(rent['end'], None)
            self.assertGreaterEqual(rent['bikeId'], 1)
            self.assertLessEqual(rent['bikeId'], 5)
            self.assertEqual(rent['clientId'], self.store.clients[0].id)
            self.assertEqual(rent['model'], 'weekly')
        self.assertEqual(len(self.store.rentals), 3)
    
    def test_four_family_rentals(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(4):
            self.store.addBike('Branco')

        self.store.addRental('weekly', 'email1@mail.com', 4, True)

        for rent in self.store.rentals:
            self.assertNotEqual(rent['start'], None)
            self.assertEqual(rent['end'], None)
            self.assertGreaterEqual(rent['bikeId'], 1)
            self.assertLessEqual(rent['bikeId'], 5)
            self.assertEqual(rent['clientId'], self.store.clients[0].id)
            self.assertEqual(rent['model'], 'weekly')
        self.assertEqual(len(self.store.rentals), 4)
    
    def test_five_family_rentals(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(5):
            self.store.addBike('Branco')

        self.store.addRental('weekly', 'email1@mail.com', 5, True)

        for rent in self.store.rentals:
            self.assertNotEqual(rent['start'], None)
            self.assertEqual(rent['end'], None)
            self.assertGreaterEqual(rent['bikeId'], 1)
            self.assertLessEqual(rent['bikeId'], 5)
            self.assertEqual(rent['clientId'], self.store.clients[0].id)
            self.assertEqual(rent['model'], 'weekly')
        self.assertEqual(len(self.store.rentals), 5)
    
    def test_hourly_family_rentals(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(5):
            self.store.addBike('Branco')

        self.store.addRental('hourly', 'email1@mail.com', 5, True)

        for rent in self.store.rentals:
            self.assertNotEqual(rent['start'], None)
            self.assertEqual(rent['end'], None)
            self.assertGreaterEqual(rent['bikeId'], 1)
            self.assertLessEqual(rent['bikeId'], 5)
            self.assertEqual(rent['clientId'], self.store.clients[0].id)
            self.assertEqual(rent['model'], 'hourly')
        self.assertEqual(len(self.store.rentals), 5)
    
    def test_daily_family_rentals(self):
        self.store.addClient('Nome1', 'email1@mail.com', '11122233344')

        for i in range(5):
            self.store.addBike('Branco')

        self.store.addRental('daily', 'email1@mail.com', 5, True)

        for rent in self.store.rentals:
            self.assertNotEqual(rent['start'], None)
            self.assertEqual(rent['end'], None)
            self.assertGreaterEqual(rent['bikeId'], 1)
            self.assertLessEqual(rent['bikeId'], 5)
            self.assertEqual(rent['clientId'], self.store.clients[0].id)
            self.assertEqual(rent['model'], 'daily')
        self.assertEqual(len(self.store.rentals), 5)
        

if __name__ == "__main__":
    unittest.main()