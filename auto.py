import subprocess, platform, csv, random, string

filnamn = input("Ange .csv filnamn: ")
lista = []
listRow = 1
with open(str(filnamn), newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        lista.append(row)

def listAssign():
    uName = str(lista[1][0])
    uGivenName = str(lista[1][1])
    uSurname = str(lista[1][2])
    uAccountName = str(lista[1][3])
    return (uName,uGivenName,uSurname,uAccountName)

def createPassword():
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars2 = "1234567890"
    chars3 = "!%&/()=#"
    uPassword = ""
    for c in range (3):
        uPassword += random.choice(chars)
        uPassword += random.choice(chars1)
        uPassword += random.choice(chars2)
        uPassword += random.choice(chars3)    

    uPassword = ''.join(random.sample(uPassword,len(uPassword)))
    return uPassword

uPassword = createPassword()
uName, uGivenName, uSurname, uAccountName = listAssign()
listAssign()
createPassword()
cmd = 'New-ADUser -name "' + uName + '" -GivenName "' + uGivenName + '" -Surname "' + uSurname + '" -SamAccountName "' + uAccountName + '" -AccountPassword "' + uPassword + '" -Enable $true'
print(cmd)