import csv

def readCsv(data):
    with open(data,"r") as file:
        reader =csv.reader(file)
        csvList = []
        i = 0
        for row in reader:
            if i > 0:
                csvList.append(row)
            i = i+1
    return csvList

def listEditor(list):
    newList = []
    for listAttr in list:
        newList.append(listAttr[0].split(";"))
    return newList

def insertListToDictNumbers(liste):
    dictList = []
    for row in liste:
        dbRow ={
            "dateRep":row[0],
            "day":row[1],
            "month":row[2],
            "year":row[3],
            "cases":row[4],
            "deaths":row[5],
            "country":row[6],
            "countryCode":str(row[7]).lower()
        }
        dictList.append(dbRow)
    return dictList


def insertListToDictLocations(liste):
    list = listEditor(liste)
    dictList = []
    id = 0
    for row in list:
        dbRow = {
            "countryId":id,
            "state":row[0],
            "country":row[1],
            "lat":round(float(row[2])),
            "lon":round(float(row[3]))
        }
        dictList.append(dbRow)
        id = id+1

    return dictList
