# Questão 1)
# Crie uma função que pode somar
# quantidades indeterminadas de números
# soma_valores(1, 2, 3)
# Resposta: 6
# Ex: soma_valores(2, 10, 10, 20)
# Resposta: 42
import random
import string
import secrets

def soma_valores(*n):
    return sum(n)
print(soma_valores(1,2,3))
print(soma_valores(2,10,10,20))

ex1 = soma_valores(1,2,3)
ex2 = soma_valores(2,10,10,20)

print(ex1)
print(ex2)


# Questão 2)
# O usuário deverá informar quantas letras, quantos números e quantos caracteres especiais. 
# A partir disso, deverá ser criada uma senha aleatória de acordo com a quantidade de informada
# de cada um.  



def gerar_senha():

    senha = [] #Lista vazia
    letras = string.ascii_letters
    numeros = string.digits
    caracteres = ['!', '@', '#', '%', '$', '&', '*', '?'] #string.punctuation


    print(letras)
    print(numeros)


#Quantitativo de cada um, letras, numeros e caracteres
    qnt_letras = int(input('Quantidade de Letras'))
    qnt_numeros = int(input('Quantidade de Numeros'))
    qnt_caracteres = int(input('Quantidade de Caracteres'))

    for i in range(qnt_letras):
        l = random.choice(letras) #escolhe râmdomico
        senha.append(l)

    for i in range(qnt_numeros):
        n = random.choice(numeros) #escolhe râmdomico
        senha.append(n)

    for i in range(qnt_caracteres):
        c = random.choice(caracteres) #escolhe râmdomico
        senha.append(c)

    
    # for i in range(qnt_letras):
    #     l = secret.choice(letras) #escolhe râmdomico
    #     senha.append(l)

    # for i in range(qnt_numeros):
    #     n = secret.choice(numeros) #escolhe râmdomico
    #     senha.append(n)

    # for i in range(qnt_caracteres):
    #     c = secret.choice(caracteres) #escolhe râmdomico
    #     senha.append(c)



    random.shuffle(senha) #Embaralhar
    senha = ''.join(senha)

    return senha # inclui o return


nova_senha = gerar_senha()
print('A nova senha: ', nova_senha)














