from layout.componentes import dcc, create_navbar, create_formulario_estações, dbc

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
                            dcc.Graph(id="graph")                  
   
                        ],sm=9
                    )
                ]    
            ),      
        ], fluid=True
    )


    return layout
