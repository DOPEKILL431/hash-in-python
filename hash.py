#programm for hash (integer, string, float)

print("si vous voulez hasher un nombre tapez 1")
print("               ")
print("si vous voulez hasher un nombre a virgule tapez 2")
print("               ")
print("si vous voulez hasher une liste de mot tapez 3")


for i in range (3) :
    print("               ")

choix=int(input("saisir votre choix entre 1 et 3 : "))

if choix==1:
    nombrehash=int(input("saisir votre nombre à hasher : "))
    print("Hash for",nombrehash,"est :",hash(nombrehash))

if choix==2:
    nombrevirgulehash=float(input("saisir votre nombre à virgule : "))
    print("Hash for",nombrevirgulehash,"est :",hash(nombrevirgulehash))

if choix==3:
    mothash=str(input("saisir votre mot à hasher : "))
    print("Hash for",mothash,"est :",hash(mothash))