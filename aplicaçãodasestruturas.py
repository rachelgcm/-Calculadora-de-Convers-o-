medidas_unidade = [ 'bit', 'byte', 'megabyte', 'gigabyte', 'terabyte', 'tetabyte']

unidade_final= input ("selecione a unidade final")
unidade_atual= int (input("selecione o valor a ser escolhido"))
unidade_atual= int (input("selecione a unidade de medida"))


while unidade_atual not in medidas_unidade :
    print("unidade não encontrada , tente novamente") 
    
    unidade_atual= input()

    while unidade_final in medidas_unidade :
        print ("unidade não encontrada , tente novamente")
        unidade_final = input() 

def conversao (valor_atual, unidade_atual, unidade_final):
    valor_final= valor_atual
    if unidade_atual== 'bit':
            valor_final = valor_final/8
    unidade_atual = 'byte'

    if medidas_unidade. index (unidade_atual) <medidas_unidade.index (unidade_final) :
        
        for i in range (medidas_unidade. index (unidade_atual), medidas_unidade.index (unidade_final)) :
                valor_final =valor_final/1024

    else:
        for i in range (medidas_unidade.index (unidade_atual), medidas_unidade.index (unidade_final),-1) :

            valor_final= valor_final *1024

        if unidade_atual== 'bit' :

            valor_final = (valor_final/1024)*8

    print (valor_final)

    conversao(valor_atual, unidade_atual, unidade_final)