# coding: utf-8

# In[ ]:

import requests
import json

class sptransRequest(object):
    
    def post(self):
    
        url = 'http://api.olhovivo.sptrans.com.br/v0/Login/Autenticar?token='
        key = 'your key'
    
        response = requests.post(url + key)
    
        return response

    def getLocationLine(self, codigoLinha):
        
        url = 'http://api.olhovivo.sptrans.com.br/v0/Posicao?' + str(codigoLinha)
        
        response = requests.get(url, {"codigoLinha":str(codigoLinha)}

        return response

    def coordsLine(codigoLinha):

        try:
            response = self.getLocationLine(codigoLinha)
            data = response.txt
            js = json.loads(str(data))

            return js
            
        except Exception as error:
            print (error)
