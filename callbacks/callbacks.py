from dash.dependencies import Input, Output


#TODO corrigir o error ModuleNotFoundError
# from script.connectx import stations_list
# ModuleNotFoundError: No module named 'script'

def update_estacao_callback(app):
    
    @app.callback(
        Output('estacao-dropdown', 'options'),
        Input('estado-dropdown','value')
    )
    def update_dropdown_stations(selected_estado):
        #stations = stations_list(selected_estado)
        #return stations
        ...


if __name__ == '__main__':
    ...
    #estacoes = connectx.stations_list('AM')
    #print(estacoes)
    #print('...')