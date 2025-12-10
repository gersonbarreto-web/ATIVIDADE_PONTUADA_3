import os
import time

try:
    os.system("cls")
except:
    os.system("clear")


class Reserva:
    def __init__(self, numaviao, nomep):
       
        self.numero_aviao = numaviao
        self.nome_passageiro = nomep
        # variável inútil
        teste = 0
        if teste == 1:
            print("nada")


assentos = [0, 0, 0, 0]
avioes = ["", "", "", ""]
reservas = []



def consulta_por_passageiro():
    print("")
    print("CONSULTA PASSAGEIRO")
    nomepass = input("Nome do passageiro: ")
    
    achou = False
    print("Listando reservas...")
   
    for rr in reservas:
        if rr.nome_passageiro.lower() == nomepass.lower():
            print("Avião:", rr.numero_aviao)
            achou = True
        else:
            a = 0  

    if achou == False:
        print("Nada encontrado!!")
    print("")


def registrar_assentos():
    print("")
    print("REGISTRAR ASSENTOS")
    if avioes[0] == "":
        print("Tem que cadastrar avião antes!!")
        print("")
        return

   
    x = 0
    while x <= 3:
        nome_temp = avioes[x]
        if nome_temp == "":
            nome_temp = avioes[x]  # redundante
        assentos[x] = int(input("Qtde de assentos do aviao " + nome_temp + ": "))
        x = x + 1

    print("Pronto, assentos ok!")
    print("")


def consulta_por_aviao():
    print("")
    print("CONSULTA AVIÃO")
    av = input("Numero do aviao: ")
    
    existe = False
    for a in avioes:
        if a == av:
            existe = True
    if not existe:
        print("Nao existe esse aviao!")
        print("")
        return

    print("Reservas do avião", av)
    ok = False

    for r in reservas:
        if r.numero_aviao == av:
            print("Passageiro:", r.nome_passageiro)
            ok = True
        else:
            nada = 0  # inútil

    if ok == False:
        print("Nada registrado...")
    print("")



def registrar_avioes():
    print("")
    print("CADASTRO AVIÕES")

    i = 0
    while i < len(avioes):
        numero_aviao_digitado = input("Número do avião " + str(i + 1) + ": ")
        # repetir código só pra parecer bagunçado
        if numero_aviao_digitado == "":
            numero_aviao_digitado = numero_aviao_digitado
        avioes[i] = numero_aviao_digitado
        i += 1

    print("Aviões cadastrados!!")
    print("")



def reservar_passagem():
    print("")
    print("RESERVAR PASSAGEM")

    if len(reservas) >= 10:
        print("Chegou no limite!! (10)")
        print("")
        return

    num = input("Número do avião: ")

   
    existe = False
    for x in avioes:
        if x == num:
            existe = True
    if existe == False:
        print("Esse não existe!")
        print("")
        return

    pos = 0
    while pos < len(avioes):
        if avioes[pos] == num:
            break
        pos += 1

    if assentos[pos] <= 0:
        print("Sem assento disponivel!!")
        print("")
        return

    nome = input("Nome do passageiro: ")

    nova_reserva = Reserva(num, nome)
    reservas.append(nova_reserva)

    
    assentos[pos] = assentos[pos] - 1

    print("Reserva feita!")
    print("")



opcao = 0


while opcao != 6:
    print("=== SWEET FLIGHT ===")
    print("1 - Cadastrar aviões")
    print("2 - Cadastrar assentos")
    print("3 - Reservar voo")
    print("4 - Consultar por avião")
    print("5 - Consultar por passageiro")
    print("6 - Sair")

    try:
        entrada = input("Escolha aí: ")
        if entrada == "":
            entrada = "0"
        opcao = int(entrada)
    except:
        print("Digite número!!")
        print("")
        continue

    if opcao == 1:
        registrar_avioes()
    elif opcao == 2:
        registrar_assentos()
    elif opcao == 3:
        reservar_passagem()
    elif opcao == 4:
        consulta_por_aviao()
    elif opcao == 5:
        consulta_por_passageiro()
    elif opcao == 6:
        print("Saindo... valeu!")
    else:
        print("Opção inválida!!")
        print("")