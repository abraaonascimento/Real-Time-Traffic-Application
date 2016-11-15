# coding: utf-8

# In[ ]:

import requests
import json

class requestRealTimeBusLocation(object):

    sptransLines = [1273, 34041]

    def __init__(self, getRealTimeLocation=True):

        self.post()
        self.getRealTimeLocation = getRealTimeLocation

    def post(self):

        url = 'http://api.olhovivo.sptrans.com.br/v0/Login/Autenticar?token='
        key = 'YOUR KEY'

        self.session = requests.Session()

        response = self.session.post(url + key)

        return response

    def get(self, busID):

        url = 'http://api.olhovivo.sptrans.com.br/v0/Posicao?codigoLinha=' + str(busID)

        response = self.session.get(url)

        return response

    def getBusLocation(self, busID):

        try:
            response = self.get(busID)
            data = response.text
            js = json.loads(str(data))

            return js

        except Exception as error:
            print (error)

    def getNetworkBusLocation(self, sptransLines=sptransLines):

        if self.getRealTimeLocation == True:

            networkBusLocation = []

            for line in sptransLines:

                busLocation = self.getBusLocation(line)
                networkBusLocation.append(busLocation)

        return networkBusLocation
