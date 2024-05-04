inputBilangan = input("Faktor bilangan dari : ")
bilangan = int(inputBilangan)

for i in range(1, bilangan + 1) :
    if bilangan % i == 0 :
        print(i)