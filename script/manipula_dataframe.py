import pandas as pd
from datetime import datetime

def create_df(data):
    data =  pd.DataFrame(data)   
    return  data



def create_df_list(lista):
    data = pd.DataFrame(lista)
    return data



def create_df_csv(csv_file):
    data = pd.read_csv(csv_file)
    return data



def create_df_json(json_file):
    data = pd.read_json(json_file)
    return data



def retornar_lista_de_estado(regioes_estados_br, lista=None):
    for regiao in regioes_estados_br:
        for estado in regiao['regioes_estados_br']:
                lista = criar_nova_lista(estado['estado'].upper(), lista)
    return lista


# Função responsável por criar nova lista (ATENÇAO: precisa setar a lista vazia no inicio do bloco do codigo)
def criar_nova_lista(valor, lista=None):
    if lista == None:
        lista = []
    lista.append(valor)
    return lista



def states_list(df) -> list:
    lista = df['SG_ESTADO'].sort_values().unique()
    return lista




def stations_list(df):
    def define_state(sg_state):       
        filter = df.loc[df['SG_ESTADO'] == sg_state]
        list_of_stations = filter['DC_NOME'].tolist()
        return list_of_stations
    return define_state



def obtem_codigo_da_estacao(df):
    
    def codigo_estacao(dc_nome):
        filter = df[df['DC_NOME'] == dc_nome]
        if not filter.empty:
            codigo = filter['CD_ESTACAO'].iloc[0]
            print(codigo)
            return codigo
        else:
            return None
    
    return codigo_estacao


def data_de_hoje_str():
    data_hora_atual = datetime.now()
    data_de_hoje = data_hora_atual.date()
    convert_data_de_hoje_str = data_de_hoje.strftime('%Y-%m-%d')
    return convert_data_de_hoje_str



def update_df(df):
    def retorna_coluna_radicao(sigla_estado, estacao):
        dia = data_de_hoje_str()
        df_estado = df[df['UF'] == sigla_estado]
        df_cidade = df_estado[df_estado['CD_ESTACAO'] == estacao]
        grandeza = df_cidade['RAD_GLO'] [df_cidade['DT_MEDICAO'] == dia]
        return grandeza
    return retorna_coluna_radicao



if __name__ == '__main__':
    
    from manipula_api import ConnectAPI
    
    # Create connection with API 
    cnx = ConnectAPI()
    data_stations = cnx.get_all_stations()
    df_stations = create_df(data_stations)
    obtem_codigo = obtem_codigo_da_estacao(df_stations)
    codigo = obtem_codigo('MANAUS')
    print(codigo)
    
    
    
   