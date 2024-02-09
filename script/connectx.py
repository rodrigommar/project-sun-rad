from script.manipula_api import ConnectAPI
from script.manipula_dataframe import create_df, states_list, stations_list, obtem_codigo_da_estacao
from script.manipula_mongodb import connect_mongodb


# Create connection with API 
cnx = ConnectAPI()
data_stations = cnx.get_all_stations()
data_of_station_one = cnx.obtem_dados_de_hoje()



# create a variables of dataframe
df_stations = create_df(data_stations)
lista_de_estado = states_list(df_stations)
lista_de_estacoes = stations_list(df_stations)
obtem_codigo = obtem_codigo_da_estacao(df_stations)


# salvar dados no mongodb atlas
start_date = '2024-01-21'
cod_estacao = 'A101'

# create dataframe



# connect with mongodb atlas






