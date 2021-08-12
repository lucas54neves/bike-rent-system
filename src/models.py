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
        }
        """
    
    def showBikes(self):
        for bike in self.bikes:
            print(bike)