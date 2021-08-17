from models import Store, Client

def main():
    storeOfBikes = Store('A Loja', 'Rua 1')
    storeOfBikes.addBike('Vermelho')
    storeOfBikes.addBike('Branco')
    storeOfBikes.showBikes()
    storeOfBikes.addClient('Nome1', 'email1@mail.com', '11122233344')
    storeOfBikes.addClient('Nome2', 'email2@mail.com', '12345678901')
    storeOfBikes.addClient('Nome3', 'email3@mail.com', '13345678901')
    storeOfBikes.addClient('Nome3', 'email3@mail.com', '13345678901')

main()