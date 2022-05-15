print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um trinagulo')

    try:
        if s1 == s2 == s3:
            print('Triangulo equilatero: todos os lados iguais')
        elif s1 != s2 != s3 != s1:
            print('Triangulo escaleno: todos os lados diferentes')
        else:
            print('Triangulo isosceles: dois lados iguais')
    finally:
        print('')
else:
    print('Os segmentos acima nao podem formar um triangulo')








