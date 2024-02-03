from dash.dependencies import Input, Output


#TODO corrigir o error ModuleNotFoundError
from script.connectx import lista_de_estacoes
# ModuleNotFoundError: No module named 'script'

def update_estacao_callback(app):
    
    @app.callback(
        Output('estacao-dropdown', 'options'),
        Input('estado-dropdown','value')
    )
    def update_dropdown_stations(selected_estado):
        stations = lista_de_estacoes(selected_estado)
        return stations




if __name__ == '__main__':
    ...
    #estacoes = connectx.stations_list('AM')
    #print(estacoes)
    #print('...')