from manipula_api import ConnectAPI
from manipula_dataframe import create_df, states_list, stations_list
from manipula_mongodb import connect_mongodb


# Create connection with API 
cnx = ConnectAPI()
data_stations = cnx.get_all_stations()



# create a variables of dataframe
df_stations = create_df(data_stations)
lista_de_estado = states_list(df_stations)
lista_de_estacoes = stations_list(df_stations, 'AM')


# salvar dados no mongodb atlas
start_date = '2024-01-21'
cod_estacao = 'A101'
dados = cnx.set_start_day_to_get_data(start_date, cod_estacao)

# create dataframe
df_dados_horarios = create_df(dados)


# connect with mongodb atlas






