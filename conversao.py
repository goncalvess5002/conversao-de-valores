from calculadora import converterStringParaFloat, bitParaByte, byteParaBit

print(' -Escreva 1 para bitParaByte \n -Escreva 2 byteParaBit')
funcEscolha = input ()
if (funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    ValorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print (ValorConvertido)


elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    ValorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(ValorConvertido)