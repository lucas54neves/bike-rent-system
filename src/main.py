from models import Store

def operationsMenu():
    print(f'========== Menu ==========')
    print(f'[1] Adicionar bicicleta')
    print(f'[2] Adicionar cliente')
    print(f'[3] Exibir biciletas')
    print(f'[4] Adicionar aluguel')
    print(f'[5] Calcular aluguel')
    print(f'[0] Sair')
    print(f'==========================')

def main():
    option = input('Deseja entrar no sistema? [s/n] ')

    if option == 's':
        store_name = input('Qual o nome da loja? ')

        store_address = input('Qual o endereco da loja? ')

        store = Store(store_name, store_address)

    while option == 's':
        operationsMenu()

        option_as_string = input('Qual opcao desejada? ')
        
        try:
            option = int(option_as_string)
        except:
            print('A entrada deve ser um inteiro entre 0 e 5')

        if option == 1:
            color = input('Qual a cor? ')

            try:
                store.addBike(color)
            except Exception as error:
                print(str(error))
        elif option == 2:
            name = input('Qual o nome do cliente? ')

            email = input('Qual o email do cliente? ')
            
            cpf = input('Qual o CPF do cliente? ')

            try:
                store.addClient(name, email, cpf)
            except Exception as error:
                print(str(error))
        elif option == 3:
            print(f'=== Estoque de bicicletas ===')
            
            store.showBikes()
        elif option == 4:
            model = input('Qual modelo do aluguel? ')

            email = input('Qual email do cliente? ')

            quantity = int(input('Qual a quantidade de alugueis? '))

            family = input('O aluguel e de familia? [s/n] ')

            isFamily = family == 's'

            try:
                store.addRental(model, email, quantity, isFamily)
            except Exception as error:
                print(str(error))

        elif option == 5:
            email = input('Qual email do cliente? ')

            try:
                value = store.calculateRental(email)
            except Exception as error:
                print(str(error))

            print(f'O valor do aluguel e R$ {value}')
        elif option != 0:
            print('Opcao nao cadastrada. Tente novamente.')

        if option == 0:
            option = 'n'
        else:
            option = 's'

main()