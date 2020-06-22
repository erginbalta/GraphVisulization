import networkx as nx
import matplotlib.pyplot as plt
import folium
import csvFileOperations as c
import newsOperations as nws
import dataVisulization as dt


data = "data/cityLatLon.csv"
data2 = "data/coronaNumbers.csv"

circleFillOpacity = 0.2
layerFlights = folium.FeatureGroup(name='<span style="color: black;">Flights</span>')
layerConfirmed = folium.FeatureGroup(name='<span style=\\"color: #EFEFE8FF;\\">Confirmed infected</span>')

newsJson = nws.readJson()

dataOfData = c.readCsv(data)
locationList = c.insertListToDictLocations(dataOfData)
dataOfData2 = c.readCsv(data2)
numberList = c.insertListToDictNumbers(dataOfData2)



def createGraph(liste):
    graph = nx.Graph()
    startedNode = []
    nodeList = []
    id = 0
    for node in liste:
        if node["state"] == "0":
            cnt = node["country"]
            graph.add_node(cnt)
        else:
            graph.add_node(node["state"])

        nodeList.append(node)
        if node["state"] == "Hubei":
            startedNode.append(node)
        id = id+1

    for node in nodeList:
        startPoint = startedNode[0]
        if node["state"] == "0":
            graph.add_edge(startPoint["state"],node["country"])
        else:
            graph.add_edge(startPoint["state"], node["state"])

    nx.draw_networkx(graph)
    plt.savefig("graph/dnm.png")

def popupCreator(lat,lon):
    country = ""
    countryCode = ""
    news = ""
    for i in locationList:
        if lat == i["lat"] and lon == i["lon"]:
            country = i["country"]
            break
    for i in numberList:
        if country == i["country"]:
            countryCode = i["countryCode"]
            break
    for i in newsJson:
        if countryCode == i["country"]:
            news = i["news"]
            break
    return news

def showMap(liste):
    startLocation = []
    for nodes in liste:
        if nodes["state"]=="Hubei":
            startLocation.append(nodes)

    startPoint = startLocation[0]
    startLat = startPoint["lat"]
    startLon = startPoint["lon"]
    map = folium.Map(location=[startLat,startLon],
                     tiles="CartoDB dark_matter",
                     zoom_start=2)

    for node in liste:
        popup = popupCreator(node["lat"],node["lon"])
        folium.PolyLine(locations=[[startPoint["lat"],startPoint["lon"]], [int(node["lat"]),int(node["lon"])]],
                        color='white',
                        weight=0.8,
                        opacity=0.3,
                        popup=popup
                        ).add_to(layerFlights)

        folium.CircleMarker(location=[node["lat"],node["lon"]],
                            radius=5,
                            popup=popup,
                            color='#ffbf80',
                            fill_opacity=0.3,
                            weight=1,
                            fill=True,
                            fillColor='#ffbf80'
                            ).add_to(layerConfirmed)
    layerFlights.add_to(map)
    layerConfirmed.add_to(map)
    folium.map.LayerControl('bottomleft', collapsed=False).add_to(map)
    map.save("graph/mapGraphDark.html")


def showMapNormal(liste):
    startLocation = []
    for nodes in liste:
        if nodes["state"]=="Hubei":
            startLocation.append(nodes)

    startPoint = startLocation[0]
    startLat = startPoint["lat"]
    startLon = startPoint["lon"]
    map = folium.Map(location=[startLat,startLon],
                     zoom_start=2)

    for node in liste:
        popup = popupCreator(node["lat"],node["lon"])
        folium.PolyLine(locations=[[startPoint["lat"],startPoint["lon"]], [int(node["lat"]),int(node["lon"])]],
                        color='red',
                        weight=0.8,
                        opacity=0.3,
                        popup=popup
                        ).add_to(layerFlights)

        folium.CircleMarker(location=[node["lat"],node["lon"]],
                            radius=5,
                            popup=popup,
                            color='#ffbf80',
                            fill_opacity=0.3,
                            weight=1,
                            fill=True,
                            fillColor='#ffbf80'
                            ).add_to(layerConfirmed)
    layerFlights.add_to(map)
    layerConfirmed.add_to(map)
    folium.map.LayerControl('bottomleft', collapsed=False).add_to(map)
    map.save("graph/mapGraphNormal.html")


showMap(locationList)
showMapNormal(locationList)
"""
createGraph(locationList)

dt.numericVisulizationGeneralCases(numberList,"Germany")
dt.numericVisulizationGeneralCases(numberList,"Turkey")
dt.numericVisulizationGeneralCases(numberList,"Spain")
dt.numericVisulizationGeneralCases(numberList,"China")

dt.numericVisulizationGeneralDeathAndCases(numberList,"Turkey")
dt.numericVisulizationGeneralDeathAndCases(numberList,"Spain")
dt.numericVisulizationGeneralDeathAndCases(numberList,"China")
dt.numericVisulizationGeneralDeathAndCases(numberList, "Germany")

dt.scatterCountryData(numberList,"Turkey")
dt.scatterCountryData(numberList,"Spain")
dt.scatterCountryData(numberList,"China")
dt.scatterCountryData(numberList,"Germany")
"""
