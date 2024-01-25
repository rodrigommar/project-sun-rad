import dash
from layout.layout import create_layout
from callbacks.callbacks import update_estacao_callback
import dash_bootstrap_components as dbc


# Inicialize o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Use o layout criado no módulo layout.py
app.layout = create_layout()


# Adicione a callback definida no módulo callbacks.py
update_estacao_callback(app)


# Execute o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
