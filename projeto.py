padrão = 1024 


def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    ByteCalculado = valorASerConvertido / 8
    return ByteCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    BitCalculado = valorASerConvertido * 8
    return BitCalculado

def byteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    KilobyteCalculado = valorASerConvertido / padrão
    return KilobyteCalculado

def kilobyteParabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para byte')
    byteCalculado = valorASerConvertido * padrão
    return byteCalculado

def KilobyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para megabyte')
    MegabyteCalculado = valorASerConvertido / padrão
    return MegabyteCalculado

def MegabyteParakilobyte(valorASerConvertido):
    print('Valor convertido de Megabyte para kilobyte')
    kilobyteCalculado = valorASerConvertido * padrão
    return kilobyteCalculado

def MegabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de Megabyte para Gigabyte')
    GigabyteCalculado = valorASerConvertido / padrão
    return GigabyteCalculado

def GigabyteparaMegabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Megabyte')
    MegabyteCalculado = valorASerConvertido * padrão
    return MegabyteCalculado

def GigabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de Gigabyte para Terabyte')
    TerabyteCalculado = valorASerConvertido / padrão
    return TerabyteCalculado

def TerabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de Terabyte para Gigabyte')
    GigabyteCalculado = valorASerConvertido * padrão
    return GigabyteCalculado

def TerabyteParapetabyte(valorASerConvertido):
    print('Valor convertido de Terabyte para Petabyte')
    petabyteCalculado = valorASerConvertido / padrão
    return petabyteCalculado

def PetabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de Petabyte para Terabyte')
    TerabyteCalculado = valorASerConvertido * padrão
    return TerabyteCalculado

print("insira um valor: ")
valorInicial = converterStringParaFloat(input())
valorConvertido = PetabyteParaTerabyte(valorInicial)
print(valorConvertido)