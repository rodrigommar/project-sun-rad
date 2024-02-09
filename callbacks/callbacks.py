from dash.dependencies import Input, Output
from script.connectx import lista_de_estacoes, data_of_station_one, create_df, obtem_codigo
import plotly.subplots as sp
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.express as px



def update_estacao_callback(app):
    
    @app.callback(
        Output('estacao-dropdown', 'options'),
        Input('estado-dropdown','value')
    )
    def update_dropdown_stations(selected_estado):
        stations = lista_de_estacoes(selected_estado)
        return stations



def update_graph(app):
    
    @app.callback(
        Output('graph','figure'), 
        Input('estacao-dropdown', 'value')

    )
    def update_sub_graph1(value_estacao):

        codigo = obtem_codigo(value_estacao)
        
        data = data_of_station_one(codigo)
        df = create_df(data)

        df_grandeza = df[['HR_MEDICAO', 'RAD_GLO', 'TEM_SEN', 'CHUVA', 'VEN_VEL']].astype('float64')

        print(df_grandeza.info())
        
        grafico = create_grafico(df_grandeza)

        return grafico




def update_map_callback(app):
    
    @app.callback(
        Output('graph','figure'), 
        Input('estado-dropdown','value')
    )
    def create_mapa(select_data):
        

        fig = px.choropleth_mapbox(
            lista_de_estacoes,
            locations='SG_ESTADO',
            color='CD_DISTRITO',
            center={'lat': -16.95, 'lon':-47.78},
            geojson='brazil_states',
            color_continuous_scale='Redor',
            hover_data={'SG_ESTADO': True, 'CD_SITUACAO': True, 'CD_DISTRITO': True, 'DC_NOME': True, 'REGIAO': True},
        )
        
        fig.update_geos(fitbounds="locations", visible=True)
        
        fig.update_layout(
            paper_bgcolor='#242424',
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
            mapbox_style='carto-darkmatter'
        )

        return fig




def create_grafico(df):

    fig = sp.make_subplots(rows=2, cols=2)
    
    eixo_x = df['HR_MEDICAO']
    eixo_radicao = df['RAD_GLO']
    eixo_temperatura = df['TEM_SEN']
    eixo_chuva = df['CHUVA']
    eixo_vento = df['VEN_VEL']

    trace1 = go.Scatter(x=eixo_x, y=eixo_radicao, mode='lines+markers', name='Radiação')
    trace2 = go.Scatter(x=eixo_x, y=eixo_temperatura, mode='lines+markers', name='Temperatura')
    trace3 = go.Scatter(x=eixo_x, y=eixo_chuva, mode='lines+markers', name='Chuva')
    trace4 = go.Scatter(x=eixo_x, y=eixo_vento, mode='lines+markers', name='Vento')
    
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=1, col=2)
    fig.add_trace(trace3, row=2, col=1)
    fig.add_trace(trace4, row=2, col=2)
    
    fig.update_layout(title='Quatro Subplots', xaxis_title='Hora', yaxis_title='Grandeza', height=800, showlegend=True)

    return {'data': fig['data'], 'layout': fig['layout']}


if __name__ == '__main__':
    ...
    #estacoes = connectx.stations_list('AM')
    #print(estacoes)
    #print('...')