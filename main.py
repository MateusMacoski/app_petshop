# Boas-vindas
print("Bem-vindo, você está no app do petshop do Mateus Macoski")

# Peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro (em kg): "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Peso acima de 50 kg. Peso máximo suportado é 50 kg.")
        except ValueError:
            print("Por favor, digite um valor numérico para o peso.")

# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro:\n c - curto\n m - médio\n l - longo\n ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção de pelo inválida. Digite 'c', 'm' ou 'l'.")

# Função para obter serviços adicionais
def cachorro_extra():
    extra_total = 0
    while True:
        try:
            extra = int(input("Escolha um serviço adicional:\n 1 - cortar unhas\n 2 - escovar os dentes\n 3 - limpar as orelhas\n 0 - Prosseguir\n "))
            if extra == 0:
                return extra_total
            elif extra == 1:
                extra_total += 10
            elif extra == 2:
                extra_total += 12
            elif extra == 3:
                extra_total += 15
            else:
                print("Opção de serviço adicional inválida. Digite 0, 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um valor numérico para o serviço adicional.")

# Função principal
def main():
    peso = cachorro_peso()
    pelo = cachorro_pelo()
    extras = cachorro_extra()

    total = peso * pelo + extras

    print("\nTotal a pagar: R${:.2f}".format(total))

if __name__ == "__main__":
    main()
