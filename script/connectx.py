from script.manipula_api import ConnectAPI
from script.manipula_dataframe import create_df, states_list, stations_list


# Create connection with API 
cnx = ConnectAPI()
data_stations = cnx.get_all_stations()
df_stations = create_df(data_stations)

print('ConnectX it is OK', type(df_stations))


# create a variables of dataframe
