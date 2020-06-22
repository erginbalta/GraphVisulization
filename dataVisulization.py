import matplotlib.pyplot as plt


def numericVisulizationGeneralCases(liste,country):
    fileName = "graphics/"+country +"cases.png"
    cases = []
    date = []
    plt.figure(figsize=(25, 8))
    for row in liste:
        if row["country"] == country:
            cases.append(int(row["cases"]))
            date.append(row["dateRep"])

    plt.plot(date,cases, color="red")
    plt.xlabel("date")
    plt.ylabel("cases")
    plt.savefig(fileName)

def numericVisulizationGeneralDeathAndCases(liste,country):
    fileName = "graphics/" + country + "casesAndDeath.png"
    cases = []
    death = []
    plt.figure(figsize=(25, 8))
    for row in liste:
        if row["country"] == country:
            cases.append(int(row["cases"]))
            death.append(row["deaths"])

    plt.plot(death, cases, color="red")
    plt.xlabel("deaths")
    plt.ylabel("cases")
    plt.savefig(fileName)

def scatterCountryData(liste,country):
    fileName = "graphics/" + country + "casesAndDateUsingScatter.png"
    cases= []
    date= []
    plt.figure(figsize=(25, 8))
    for row in liste:
        if row["country"] == country:
            cases.append(int(row["cases"]))
            date.append(row["deaths"])
    plt.scatter(cases,date)
    plt.xlabel("Cases")
    plt.ylabel("Date")
    plt.savefig(fileName)