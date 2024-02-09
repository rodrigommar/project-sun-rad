import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time
import json
import csv
from pathlib import Path

class ConnectAPI:
    
    def __init__(self) -> None:
        
        self.url_base = 'https://apitempo.inmet.gov.br'
        self.token = self.get_token()
        


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
        

    # Obter os dados de uma url
    def get_data(self, url):
        response = requests.get(url)
        
        if response.status_code == 200:
            data_url = response.json()
            
        return data_url
    

    # obtem dados horarios baseados nos parametros
    def get_data_hour_of_station(self, data_inicial, data_final, station):

        url = f'{self.url_base}/token/estacao/{data_inicial}/{data_final}/{station}/{self.token}'
        print(url)
        
        data = self.get_data(url) 
        
        return data
    
    
    def obtem_dados_de_hoje(self):
        
        data_hora_atual = datetime.now()
        data_de_hoje = data_hora_atual.date()
        date = data_de_hoje.strftime('%Y-%m-%d')
        
        def get_station(station):
            
            url = f'{self.url_base}/token/estacao/{date}/{date}/{station}/{self.token}'
            print(url)
            
            #data = self.get_data(url)
            
            response = requests.get(url)
        
            if response.status_code == 200:
                data = response.json()
                return data
            

        
        return get_station


        


    #  retorna dados de um tipo de estacão 
    def estation_type(self, type_estation):
        
        url = f'https://apitempo.inmet.gov.br/estacoes/{type_estation}'
        
        data = self.get_data(url)
        
        return data


    # concatenar os dados das estações Automaticas e Manauais
    def get_all_stations(self):
        
        estacoes_automaticas = self.estation_type('T')
        estacoes_manuais = self.estation_type('M')

        todas_estacoes = []
        todas_estacoes.extend(estacoes_automaticas)
        todas_estacoes.extend(estacoes_manuais)
        
        return todas_estacoes
    
    
    
    # incrementa o dia
    def incrementar_dia(self, start_day):
        
        # converte a data (string) para data(datetime)
        date_curent = datetime.strptime(start_day, '%Y-%m-%d').date()
        
        # recuperar a data de hoje
        data_hora_atual = datetime.now()
        data_de_hoje = data_hora_atual.date()
        
        # indentificar o interevalo entre data de hoje e a data inicial
        intervalo = (data_de_hoje - date_curent).days
            
        if intervalo >= 7:
            
            date_curent += timedelta(days=6)
        
        else:
            
            date_curent += timedelta(days=intervalo-1)
        
        new_start_day = date_curent.strftime('%Y-%m-%d')
        
        return new_start_day
      


    def get_data_hour_of_api(self, start_date, cod_estacao):
        
        dados_diarios = []
        
        temp_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        
        # recuperar a data de hoje
        data_hora_atual = datetime.now()
        data_de_hoje = data_hora_atual.date()
        
        while temp_date < data_de_hoje:
            
            end_date = self.incrementar_dia(start_date)
            
            dados_horarios_de_estacao = self.get_data_hour_of_station(start_date,end_date,cod_estacao)
            
            # aplicar transfomação dos dados  
            print({len(dados_horarios_de_estacao)})
            print(start_date, end_date)
            
            dados_diarios.extend(dados_horarios_de_estacao)
            
            temp_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            temp_date = temp_date + timedelta(days=1)
            
            start_date = temp_date.strftime('%Y-%m-%d')
            time.sleep(30)
        
        return dados_diarios
    
    

    def obter_diretorio_data(self):
        try:
            # Obtém o caminho absoluto do script atual
            caminho_do_diretorio_data = Path(__file__).parent.parent

            caminho_completo = caminho_do_diretorio_data / 'data'

            return caminho_completo
            
        except Exception as e:
            return f"Erro ao obter o diretório atual: {e}"
    
    
    
    # salva dados da api em um arquivo json
    def salvar_dados_brutos_de_uma_api_em_json(self, data, file_name):
        try:
            
            json_str = json.dumps(data, default=str)
            
            diretorio = self.obter_diretorio_data()
            caminho_completo = diretorio/f'{file_name}.json'

            with open(caminho_completo, 'w') as file:
                file.write(json_str)
            
            print('Arquivo salvo com sucesso!!')
            
        except (IOError, PermissionError) as e:
            print(f"Erro ao salvar dados em JSON: {e}")
            # Adicione aqui qualquer tratamento adicional que desejar



    # salva dados da api em um arquivo csv
    def export_csv(data, file_name):
        colunas = data[0].keys()

        with open(f'../data/{file_name}.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=colunas)      
            writer.writeheader()
            
            for linha in data:
                writer.writerow(linha)


    # função responsavel por transformar dados brutos do dataframe de estações
    def transfomar_dados_de_estacoes(self, df):
        
        # 1 - Exluir colunas ['SG_ENTIDADE']
        df.drop('SG_ENTIDADE', axis=1, inplace=True)
      
        # 2 - Tratar valores Nan nas colunas ['DT_FIM_OPERACAO']
        df['DT_FIM_OPERACAO'] = df['DT_FIM_OPERACAO'].fillna(0).astype('int64')
           
        # 3 - Preencher os valores Nan da coluna ['FL_CAPITAL'] com o valor 'N'
        df['FL_CAPITAL'] = df['FL_CAPITAL'].fillna('N')
        
        # 4 - Formatar a coluna ['DT_INICIO_OPERACAO'] para exibir apenas a data no formato YYYY-MM-DD
        df['DT_INICIO_OPERACAO'] = df['DT_INICIO_OPERACAO'].str.split('T').str[0]
    
  
    
    # função responsavel por  exlcuir duas colunas do dataframe 
    def excluir_colunas_dados_LATITUDE_LONGITUDE_horarios(self, df):
         # 1 - Exluir colunas ['SG_ENTIDADE']
        df.drop(['VL_LATITUDE', 'VL_LONGITUDE'], axis=1, inplace=True)



    # função responsável por salvar dataframe em um arquivo json
    def salvar_dados_em_um_arquivo_json(self, df, nome_arquivo):
        
        path = self.obter_diretorio_data()
        
        df.to_json(f'{path}\{nome_arquivo}.json',orient='records')

      

    # função que retorna o ome da região ao passar a sigla como argumento
    def select_regiao_a_partir_do_estado(self, estado):
        
        mapa_regioes = {
            'NORTE': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
            'NORDESTE': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
            'CENTRO-OESTE': ['DF', 'GO', 'MT', 'MS'],
            'SUDESTE': ['ES', 'MG', 'RJ', 'SP'],
            'SUL': ['PR', 'RS', 'SC']
        }

        for regiao, estados in mapa_regioes.items():
            if estado in estados:
                return regiao

        return 'Região não encontrada'
    
    
    
    # função que adiciona nova coluna 'REGIAO' no dataframe
    def cria_coluna_regiao_no_dataframe(self, df):

        df['REGIAO'] = df['SG_ESTADO'].apply(lambda estado:  self.select_regiao_a_partir_do_estado(estado))



    # função quue ler os dados de um arquivo json
    def ler_arquivo_json(self, nome_arquivo):
        
        path_ = self.obter_diretorio_data()
        full_path = f'{path_}\{nome_arquivo}.json'
        
        with open(full_path, 'r') as file:
            document = json.load(file)
            
        return document




if __name__ == '__main__':
    from manipula_dataframe import create_df
    
    connect = ConnectAPI()
    
    # PROCESSO: Extrai dados da API, baseado é uma data inicial e código de uma estação.
    # --------------------------------------------------------------------------------
    # 1 - Defini os parametros de entrada 'data_incial' e 'codigo_estacao'
    # 2 - Obtem os dados e guarda em uma variavel dados
    # 3 - Salva os dados em um arquivo json
    #----------------------------------------------------------------------------------
    #start_date = '2024-01-21'
    #cod_estacao = 'A101'   
    #dados = connect.set_start_day_to_get_data(start_date, cod_estacao)
    #connect.salvar_dados_em_um_arquivo_json(dados, 'dados_brutos_de_estacao_A101_mamaus')
    #print(len(dados), type(dados))
    


    # PROCESSO: Adiciona coluna 'REGIAO' no arquivo referente as estações. 
    # -------------------------------------------------------------------
    # 1 - Ler dados de um arquivo json
    # 2 - cria um dataframe
    # 3 - adicinoa uma nova cluna 'REGIAO' no dataframe
    # 4 - salva o dataframe em um arquivo json
    # ---------------------------------------------------------
    #dados = connect.ler_arquivo_json('data_processed_all_stations_bkp')
    #df = create_df(dados)
    #connect.cria_coluna_regiao_no_dataframe(df)
    #connect.salvar_dados_em_um_arquivo_json(df, 'data_processed_all_stations')
    #print(df.info())

