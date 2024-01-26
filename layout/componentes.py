from dash import html, dcc
import dash_bootstrap_components as dbc
from script.connectx import states_list



def create_navbar():
    
    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Pesquisar")),
            dbc.Col(dbc.Button("Pesquisar", color="primary", className="ms-2", n_clicks=0), width="auto",),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )
    
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="https://images.plot.ly/logo/new-branding/plotly-logomark.png", height="30px")),
                            dbc.Col(dbc.NavbarBrand("ORION - Dashboard Clima", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="http://127.0.0.1:8050/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )

    return navbar


def create_formulario_estações(lista_estados=states_list):
    
    dropdown_state = html.Div(
        [
            dbc.Label('Estado'),
            dcc.Dropdown(
                options=[
                    {
                       "label": 'estado',
                        "value": 'estado'
                    }
                    #for estado in lista_estados
                ],
                id="estado-dropdown",
                #value=lista_estados[0]
            
            ),
        ] #,className="mb-3"
    )


    dropdown_station = html.Div(
        [
            dbc.Label('Estado'),
            dcc.Dropdown(
                options=[
                    {
                        "label": 'estacao',
                        "value": 'estacao'
                    }
                ],
                id="estacao-dropdown",
                #value=lista_estacoes
            )
        ]
    )


    dropdown_grandeza = html.Div(
        [
            dbc.Label("Grandeza"),
            dcc.Dropdown(
                options=[{"label": 'option', "value": 'option'}],# for option in list_quantity],
                id="grandeza-dropdown",# value=list_quantity[4]
            ),
        ]
    )


    radio_period = html.Div(
        [
            dcc.RadioItems(
                ['Mês', 'Dia', 'Periodo'],
                'Dia',
                id='radio-input-date',
                inline=True,
            ),
        ]
    )


    btn_send = dbc.Button("Limpar", id="reset-button", color="primary", className="ms-3", n_clicks=0)

                                                
    btn_table = dbc.Button("Tabela", id="collapse-button", color="primary", className="ms-3", n_clicks=0)

    
    formulario = dbc.Form([
        
        dropdown_state,
        dropdown_station,
        dropdown_grandeza,
        radio_period,
        btn_send,
        btn_table
        
    ])
    
    return formulario


def create_grafico():
    grafico = html.Div([
        dcc.Graph(id="graph", config={"displayModeBar": False})
    ], style={'width': '70%', 'display': 'inline-block'})
    
    return grafico



dcc.Loading([html.Div(id='loading-demo')])

dcc.Store(id='period-store',data=None)
                                                        
dcc.Store(id='day-store',data=None)

dcc.Store(id='month-store',data=None)

