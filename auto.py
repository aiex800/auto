import subprocess, platform, csv, random, string

filnamn = input("Ange .csv filnamn: ")


with open(str(filnamn), ".csv", newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        lista.append(row)

def listAssign():
    