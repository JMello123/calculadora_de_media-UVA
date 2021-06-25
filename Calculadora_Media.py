"""Verificações:
AV1 não pode ser igual a 0
AV2 não pode ser menor q 5
Media final deve ser pelo menos 6

Sendo A1 maior que 0,0 (zero) e A2 ou A3 igual ou superior a 5,0 (Cinco),
calcule assim:
NFp = (A1 x 0,4) + (A2 ou A3 x 0,6)

NFp maior ou igual a 6,0 (seis) = Aprovado.
NFp menor que 6,0 (seis) = Reprovado.
Sendo A1 IGUAL a 0,0 (zero) e / ou com a A2 e A3 inferiores a 5,0 (Cinco),
você está reprovado e calculará assim:
NFp = (A1 x 0,4) + (A2 ou A3 x 0,6)/2"""
from time import sleep

def inputNota(texto):
    nota = input(texto)
    while not nota in list(range(0,101)):
        try:
            nota = int(nota)
        except:
                print('Por favor digite um número de 0 a 100 sem utilizar vírgulas')
                nota = input(texto)
    nota = int(nota)
    return nota

print('\n----------Calculadora de média------------\n')
print('OBS: os números usados devem estar na escala de 100. Exemplo se digitar uma nota 10 será considerada 1.\n\n')
sleep(2)

ava1 = inputNota('Insira a sua nota do primeiro trabalho (de 0 a 100): \n')
sleep(1)
ava2 = inputNota('Insira a sua nota do segundo trabalho (de 0 a 100): \n')
sleep(1)
Av2 = inputNota('Insira a sua nota da prova presencial (de 0 a 100): \n')
sleep(1)
Av1 = (ava1 + ava2)/2
Mediafinal = 0.0


while True:
    if Av1 == 0: 
        Mediafinal = (Av1*0.4) + (Av2*0.6)/2
        print('Você está \33[1;31m REPROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
        break
        

    if Av2 < 50:
        Mediafinal = (Av1*0.4) + (Av2*0.6)
        print('Por enquanto você está abaixo da média e deve fazer a AV3. Sua nota final é: {}\n'.format(Mediafinal))
        
        continua = input('Você fez a prova substitutiva AV3? aperte [s] para sim e [n] para não: \n')
        if continua == 'n':
            print('Então, por enquanto, essa é sua nota final: {}\n'.format(Mediafinal))
        if continua == 's':
            Av3 = inputNota('Insira o valor da sua nota da AV3, sua prova substitutiva (de 0 a 100): \n')
            if Av3 < 50:
                Mediafinal = (Av1*0.4) + (Av3*0.6)/2
                print('Você está \33[1;31m REPROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
            else:
                Mediafinal = (Av1*0.4) + (Av3*0.6)
                if Mediafinal >= 60:
                    print('Você está \33[1;32m APROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
                    break
                else:
                    print('Você está \33[1;31m REPROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
                    break
    else:
        Mediafinal = (Av1*0.4) + (Av2*0.6)
        if Mediafinal >= 60:
            print('Você está \33[1;32m APROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
            break
        else:
            print('Por enquanto você está abaixo da média e deve fazer a AV3. Sua nota final é: {}\n'.format(Mediafinal))
            
            continua = input('Você fez a prova substitutiva AV3? aperte [s] para sim e [n] para não: \n')
            if continua == 'n':
                print('Então, por enquanto, essa é sua nota final: {}\n'.format(Mediafinal))
                break
            if continua == 's':
                Av3 = inputNota('Insira o valor da sua nota da AV3, sua prova substitutiva (de 0 a 100): \n')
                if Av3 < 50 and Av2 < 50:
                    Mediafinal = (Av1*0.4) + (Av3*0.6)/2
                    print('Você está \33[1;31m REPROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
                    break
                else:
                    Mediafinal = (Av1*0.4) + (Av3*0.6)
                    if Mediafinal >= 60:
                        print('Você está \33[1;32m APROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
                        break
                    else:
                        print('Você está \33[1;31m REPROVADO.\33[0;37m Sua nota final é: {}\n'.format(Mediafinal))
                        break
            



