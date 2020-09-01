import requests
from lxml import html, etree
import pandas as pd
def parseStation(stationID):
    url="https://mobile.ettu.ru/station/"+str(stationID)
    r = requests.get(url)
    page=r.text

    tree=html.fromstring(page)
    routes=tree.xpath('//div[@style="width: 3em;display:inline-block;text-align:center;"]/b/text()')
    distances=tree.xpath('//div[@style="width: 4em;display:inline-block;text-align:right;"]/text()')
    arrivesAt=tree.xpath('//div[@style="width: 5em;display:inline-block;text-align:right;"]/text()') 
    data={'Route': routes, 'Distances': distances, 'Arrival': arrivesAt}
    dataframe=pd.DataFrame(data=data)
    return dataframe

print(parseStation(962933))
