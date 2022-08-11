nome = str(input("Informe seu nome completo: "))
ano = int(input("Informe seu ano de nascimento: "))
idade = 2022 - ano

while ano != str:
    try:
        if (ano >= 1922 or ano <= 2021):
            print("Seja bem vindo {}, sua idade é {} anos.".format(nome, idade))
        else:
            raise Exception ("Ano de nascimento não compatível.")
    except:
        print("Caracter inválido, por gentileza digite corretamente!")