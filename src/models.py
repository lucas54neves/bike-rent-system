from tabulate import tabulate
from datetime import datetime
import re

class Client(object):
    def __init__(self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf

class Store(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.clients = []
        self.rents = []
        """
        {
            model: hora/dia/semana
            start: data inicio
            end: data entrega
            bikeId: indice na lista de bikes
            clientId: indice do clients
        }
        """
        self.bikes = []
        """
        {
            color: cor da bike
            available: booleano que informa se esta disponivel
        }
        """
    
    # Metodo que adicionar uma bicicleta
    def addBike(self, cor):
        self.bikes.append({
            'id': len(self.bikes) + 1,
            'color': cor,
            'available': True
        })
    
    # Metodo que adiciona um usuario
    def addClient(self, name, email, cpf):
        try:
            if not (isinstance(name, str) and isinstance(email, str) and isinstance(cpf, str)):
                raise TypeError('Os dados do cliente devem ser strings.')
            
            regexEmail = '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

            if not re.fullmatch(regexEmail, email):
                raise TypeError('Email invalido.')
            
            if self.clientByEmail(email):
                raise TypeError('Cliente ja cadastrado.')

            regexCpf = '^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$'

            if not re.fullmatch(regexCpf, cpf):
                raise TypeError('CPF invalido.')

            self.clients.append(Client(name, email, cpf))
        except TypeError as error:
            print(f'ERROR: {error}')
        except Exception as error:
            print(f'ERROR: Erro nao identificado. {error}')

    
    # Metodo que adiciona um aluguel
    def addRental(self, model, email):
        try:
            if not model in ['hourly', 'daily', 'weekly', 'family']:
                raise ValueError('Tipo de aluguel invalido.')

            bikeAvailable = self.getAvailableBike()

            if not bikeAvailable:
                raise KeyError('Bicicleta indisponivel.')

            existsClient = self.findClientByEmail(email)

            if not existsClient:
                raise KeyError('Cliente nao cadastrado.')

            self.rents.append({
                'model': model,
                'start': datetime.today(),
                'end': None,
                'bikeId': bikeAvailable['id'],
                'clientId': existsClient['id']
            })
        except (ValueError, Exception, KeyError) as error:
            print(f'ERROR: {error}')
        except Exception as error:
            print(f'ERROR: Erro nao identificado. {error}')

    # Metodo que retorna a primeira bicicleta displonivel
    def getAvailableBike(self):
        for bike in self.bikes:
            if bike['available']:
                return bike
        
        return None
    
    # Metodo que retorna o cliente pelo email
    def findClientByEmail(self, email):
        for client in self.clients:
            if client.email == email:
                return client
        
        return None


    # Metodo que exibe o estoque, ou seja, imprime todas as bicicletas
    def showBikes(self):
        print(tabulate(self.bikes, headers="keys", tablefmt="fancy_grid"))