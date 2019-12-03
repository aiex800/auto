import subprocess, platform, csv, random, string, time

try:
    filnamn = str(input("Ange .csv filnamn: "))
except:
    print("Error")
    time.sleep(1)
    exit
try:
    amountOfUsers = int(input("Ange antal av användare att läsa in: "))
except:
    print("error")
    print("Antal användare automatiskt angivet som 1")
    amountOfUsers = 1
lista = []
listRow = 1
command = "None"
with open(str(filnamn), newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        lista.append(row)

def listAssign(listRow):
    uName = str(lista[listRow][0])
    uGivenName = str(lista[listRow][1])
    uSurname = str(lista[listRow][2])
    uAccountName = str(lista[listRow][3])
    return (uName,uGivenName,uSurname,uAccountName)

def createPassword():
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars2 = "1234567890"
    chars3 = "!%&/()=#"
    uPassword = ""
    for bomboclaat in range (3):
        uPassword += random.choice(chars)
        uPassword += random.choice(chars1)
        uPassword += random.choice(chars2)
        uPassword += random.choice(chars3)    

    uPassword = ''.join(random.sample(uPassword,len(uPassword)))
    return uPassword



uPassword = createPassword()
uName, uGivenName, uSurname, uAccountName = listAssign(listRow)
global cmd
cmd = 'New-ADUser -name "' + uName + '" -GivenName "' + uGivenName + '" -Surname "' + uSurname + '" -SamAccountName "' + uAccountName + '" -AccountPassword "' + uPassword + '" -Enable $true'

if platform.system() == "Windows":
    command = cmd
    print("Windows system detected...")
    time.sleep(1.5)
elif platform.system() == "Linux":
    command = unix
    print("Linux system detected...")
    time.sleep(1.5)
else:
    print("ERR0R0R PICNIC: Köp ny dator")

while listRow < amountOfUsers:
    createPassword()
    listAssign(listRow)
    print(command)
    listRow += 1
    print(listRow)