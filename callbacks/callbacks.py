from dash.dependencies import Input, Output
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from script.manipula_dataframe import stations_list



def update_estacao_callback(app):
    
    @app.callback(
        Output('estacao-dropdown', 'options'),
        Input('estado-dropdown','value')
    )
    def update_dropdown_stations(selected_estado):
        stations = stations_list(selected_estado)
        return stations


if __name__ == '__main__':
    estacoes = stations_list('AM')
    print(estacoes)