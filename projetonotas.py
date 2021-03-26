from time import sleep

#Definir as funcoes de entrada e das notas
def entrada():
    print("Olá, esse é o progama para facilitar o calculo da sua nota. Escolha uma das opções de matérias ja cadastradas: ")
    print("-="*56)
    print(" [1] CÁLCULO 1")
    print(" [2] GEOMETRIA ANALÍTICA ")
    print(" [3] LNF ")
    print(" [4] ADICIONAR MATÉRIA ")
    print("-="*56)
def calculo1():
        formcalc1 = []
        somcalc1 = []
        for pos in range (1,7):
            notacalc1 = float(input("Qual sua nota na {}º formativa? ".format(pos)))
            formcalc1.append(notacalc1) #salvar notas formativa
        print("Agora preciso saber sobre suas outras provas... ")
        sleep(2)
        for pos2 in range (1,3):   
            notacalc2 = float(input("Qual suas notas na {}º somativa? ".format(pos2)))
            somcalc1.append(notacalc2) #salvar notas somativas
        soma1= sum(formcalc1)   
        soma2 = sum(somcalc1)
        k = ((soma1/4)*0.4 + (soma2/4)*0.6)
        print("Sua nota final, em CÁLCULO 1 é: {:.2f}".format(k))
def geometria_analitica():
    listasgma = int(input("Das 7 listas do semestre, quantas voce fez? "))
    sleep(1)
    notalistagma = round(listasgma*0.71428,2)
    print("Ok, agora preciso saber suas notas nas provas P1 e P2: ")
    sleep(1)
    p1 = float(input("Diga sua nota na P1: "))
    p2 = float(input("Diga sua nota na P2: "))
    finalgma = notalistagma + (p1+p2)/4
    print("Sua nota final em Geometria Analitica é {:.2f}".format(finalgma))
def lnf():
    testes_listalnf = []
    for pos in range (1,13):
        testes_lnf = int(input("Qual sua nota no {}º teste de LNF: ".format(pos)))
        testes_listalnf.append(testes_lnf) #salvar notas dos testes 
    testes_listalnf.sort() #ordenar em ordem crescente
    oitotestes_lnf = testes_listalnf[4:]
    notarealtestes = (sum(oitotestes_lnf))/10
    t = (round((notarealtestes/8),3))*0.8

    presenca = str(input("Voce é presente nos questionarios e debates? [S/N] ")).upper()
    if presenca=="S":
        print("Sua nota final em LNF  {}".format(t+2))
    else:
        print("Sua nota final em LNF é {}".format(t))

#execuçao no painel para o usuario
entrada()
resp = int(input("Escolha uma das opçoes: "))
if resp==1:
    calculo1()
elif resp==2:
    geometria_analitica()
elif resp==3:
    lnf()
#sleep(5)  #ativar se for usar no cmd (esperar a mensagem sobre a nota final na materia e n fechar direto)