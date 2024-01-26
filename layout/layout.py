from layout.componentes import create_navbar, create_formulario_estações, create_grafico, dbc

def create_layout():
    
    layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    create_navbar(),
                    sm=12
                )
            ),
            
            dbc.Row(
                [
                    dbc.Col(
                        [
                            create_formulario_estações()
                        ],sm=3
                    ),
                    
                    dbc.Col(
                        [
                            create_grafico()
                        ],sm=9
                    )
                ]    
            ),      
        ], fluid=True
    )

    return layout
