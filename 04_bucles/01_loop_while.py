###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

num1=10
while num1>=1:
    print(num1)
    num1-=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

num2=1
pars=0
while num2<=20:
    if num2%2==0:
        pars+=num2
    num2+=1
print(f"La suma de parells dona {pars}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

num3=int(input("Posa un enter positiu: "))
counter=1
factorial=1
while counter<=num3:
    factorial*=counter
    counter+=1
print(f"El factorial de {num3} és {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contra=""
while len(contra)<8:
    contra=input("Contrasenya de mín 8 caràcters: ")
    if len(contra)<8:
        print("Que no, torna a provar")
print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num5=int(input("Posa un número: "))
multiplier=1
while multiplier<=10:
    resultat=num5*multiplier
    print(f"{num5}x{multiplier}={resultat}")
    multiplier+=1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

suma=0
num7=int(input("Posa un enter: "))
while num7!=0:
    suma+=num7
    num7=int(input("Posa un altre (acaba amb 0): "))
print(f"La suma dona {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

num8=int(input("Posa un enter positiu: "))
length=0
while num8>0:
    num8//=10
    length+=1
print(f"El número té {length} xifres")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

num_secret=7
attempt=int(input("Adivina el número: "))
while attempt!=num_secret:
    if attempt<num_secret:
        print("És major")
    else:
        print("És menor")
    attempt=int(input("Torna a provar: "))
print("YAAAY, SIII")