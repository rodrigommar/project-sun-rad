import requests
import os
from dotenv import load_dotenv

class ConnectAPI:
    
    def __init__(self) -> None:
        
        self.url_base = 'https://apitempo.inmet.gov.br'
        self.token = self.get_token()
        #self.status = self.test_connection()
        
        
    # obtem estações do tipo automatico
    def get_stations_automatic(self):
        
        url = f'{self.url_base}/estacoes/T'
        response = requests.get(url)
        
        if self.test_connection(response):          
            data = response.json()           
            return data
        
    
    # obtem estações do tipo manual
    def get_stations_manual(self):
        
        url = f'{self.url_base}/estacoes/M'
        response = requests.get(url)
        
        if self.test_connection(response):          
            data = response.json()           
            return data


    # valida a conexão com API
    def test_connection(self, response):
        
        if response.status_code == 200:          
            return True
        
    
    # concatena as listas de dados JSON e retorna todas as estações do tipo automatico e manaual
    def get_all_stations(self):
        
        data = []
        datat = self.get_stations_automatic()
        datam = self.get_stations_manual()
        
        data.extend(datat)
        data.extend(datam)
        
        return data
        

    # obter token
    def get_token(self):
        
        load_dotenv()
        
        token1 = os.getenv('TOKEN1')
        token2 = os.getenv('TOKEN2')
        
        if token1 and token2 is not None:
            self.token = True
        else:
            raise ValueError('Token não encontrado.')
        
        return f'{token1}={token2}'


    # obtem dados horarios baseados nos parametros
    def get_data_hour_of_all_station(self, data_inicial, data_final, station):

    
        url = f'{self.url_base}/token/estacao/{data_inicial}/{data_final}/{station}/{self.token}'
        print(url)
        response = requests.get(url) 

        if self.test_connection(response):
            dados_horarios = response.json()
            return dados_horarios



    # obtem dados horarios baseados nos parametros
    def get_data_climate_of_station(self, station):
       
        url = f'{self.url_base}/token/estacao/2024-01-10/2024-01-17/{station}/{self.token}'
        print(url)
        response = requests.get(url) 

        if self.test_connection(response):
            dados_horarios = response.json()
            return dados_horarios
        
        
        

if __name__ == '__main__':
    connect = ConnectAPI()
    #data = connect.get_data_hour_of_all_station('2024-01-15','2024-01-15', 'A101')
    data = connect.get_data_climate_of_station('A101')
    #token = connect.get_token()
    print(data)
    

    
    
    
    

