import pandas as pd


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


def stations_list(df, sg_state):
    filter = df.loc[df['SG_ESTADO'] == sg_state]
    list_of_stations = filter['DC_NOME'].tolist()
    return list_of_stations


def stations_list_test(df):
    def define_state(sg_state):       
        filter = df.loc[df['SG_ESTADO'] == sg_state]
        list_of_stations = filter['DC_NOME'].tolist()
        return list_of_stations
    return define_state

if __name__ == '__main__':
    
    from manipula_api import ConnectAPI
    
    # Create connection with API 
    cnx = ConnectAPI()
    #data_stations = cnx.get_all_stations()
    #df_stations = create_df(data_stations)
    #print(df_stations)
    
    
    
   