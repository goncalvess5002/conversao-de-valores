from calculadora import converterStringParaFloat, bitParaByte, byteParaBit, byteParakilobyte, kilobyteParaByte, kilobyteParaMegabyte, megabyteParaKilobyte, megabyteParaGigabyte, gigabyteParaMegabyte, gigabyteParaTerabyte, terabyteParagigabyte, terabyteParaPetabyte, petabyteParaTerabyte

print(' -Escreva 1 para bitParaByte \n -Escreva 2 byteParaBit \n  - Escreva 3 para byteParakilobyte \n  - Escreva 4 para kilobyteParaByte \n - Escreva 5 para kilobyteParaMegabyte \n - Escreva 6 para megabyteParaKilobyte \n - Escreva 7 para megabyteParaGigabyte \n - Escreva 8 gigabyteParaMegabyte \n - Escreva 9 para gigabyteParaTerabyte \n - Escreva 10 para terabyteParagigabyte \n - Escreva 11 para terabyteParaPetabyte \n - Escreva 12 para petabyteParaTerabyte')
funcEscolha = input ()
if (funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    ValorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print (ValorConvertido)


elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = byteParakilobyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = kilobyteParaByte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = kilobyteParaMegabyte(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = megabyteParaKilobyte (entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = megabyteParaGigabyte (entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = gigabyteParaMegabyte (entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)

elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = gigabyteParaTerabyte (entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)