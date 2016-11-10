# coding: utf-8

# In[ ]:

import requests
import json

class sptransRequest(object):

    def post(self):

        url = 'http://api.olhovivo.sptrans.com.br/v0/Login/Autenticar?token='
        key = 'your key'

        self.session = requests.Session()
        
        response = self.session.post(url + key)

        return response

    def getLocationBus(self, busID):

        url = 'http://api.olhovivo.sptrans.com.br/v0/Posicao?codigoLinha=' + str(busID)

        response = self.session.get(url)

        return response

    def coordsBus(self, busID):

        try:
            response = self.getLocationBus(busID)
            data = response.text
            js = json.loads(str(data))

            return js

        except Exception as error:
            print (error)
