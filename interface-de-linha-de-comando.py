from projeto import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKilobyte, kilobyteParabyte, KilobyteParaMegabyte, MegabyteParakilobyte, MegabyteParaGigabyte, GigabyteparaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParapetabyte, PetabyteParaTerabyte

print(' -Escreva 1 bitParaByte \n -Escreva 2 byteParaBit \n -Escreva 3 byteParaKilobyte \n -Escreva 4 kilobyteParabyte \n -Escreva 5 KilobyteParaMegabyte \n -Escreva 6 MegabyteParakilobyte \n- Escreva 7 MegabyteParaGigabyte \n -Escreva 8 GigabyteparaMegabyte \n -Escreva 9 GigabyteParaTerabyte \n -Escreva 10 TerabyteParaGigabyte \n -Escreva 11 TerabyteParapetabyte \n -Escreva 12 PetabyteParaTerabyte ') 
funcEscolha = input()
if(funcEscolha =='1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='3'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaKilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='4'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kilobyteParabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='5'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KilobyteParaMegabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='6'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = MegabyteParakilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='7'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = MegabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='8'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GigabyteparaMegabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='9'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = GigabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='10'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TerabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='11'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = TerabyteParapetabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

if(funcEscolha =='12'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = PetabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)