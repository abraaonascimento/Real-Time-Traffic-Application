import requests

class sptransRequest(object):
    
    def post(self):
    
        url = 'http://api.olhovivo.sptrans.com.br/v0/Login/Autenticar?token='
        key = 'your key'
    
        r = requests.post(url + key)
    
        return r

    def get(self):
    
        return 'something'
