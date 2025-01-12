from dash import dcc, Input, Output, State, no_update, callback_context
import dash_bootstrap_components as dbc
from datetime import date
from app import *

layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Stock assets register"), className='modal_header'),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Input(id='nome_ativo', placeholder="Name", type='text')
            ]),
            dbc.Col([
                dbc.Input(id='preco_ativo', placeholder="Price (R$)", type='number', min=0, step=0.1)
            ])
        ]),
        dbc.Row([
            dbc.Col([
                "Date:  ",
                dcc.DatePickerSingle(
                id='data_ativo',
                className='dbc',
                min_date_allowed=date(2005,1,1),
                max_date_allowed=date.today(),
                initial_visible_month=date(2017,8,5),
                date=date.today()
                ),
            ], xs=6, md=6),
            dbc.Col([
                dbc.Input(id='quantidade_ativo', placeholder="Quantity", type='number', min=0, step=1),
            ], xs=6, md=6)
        ], style={'margin-top':'1rem'}),

        dbc.Row([
            dbc.Col([
                dbc.RadioItems(id='compra_venda_radio', options=[{'label':'Buy', 'value':'Buy'}, {'label':'Sell', 'value':'Sell'}], value='Buy')
            ], style={'margin-top':'1rem'})
        ]),
    ], className="Modal_body"),
    dbc.ModalFooter([
        dbc.Row([
            dbc.Col([
                dbc.Button("Save", id="submit_cadastro")
            ])
        ])
    ], className="modal_footer")
], id="modal", is_open=False, size='lg', centered=True)

@app.callback(
    Output('submit_cadastro', 'children'),
    Input('submit_cadastro', 'n_clicks'),
    Input('add_button', 'n_clicks'),
)

def save_asset(n, n2):
    trigg_id = callback_context.triggered[0]['prop_id'].split('.')

    if trigg_id == 'submit_cadastro':
        return[dbc.Spinner(size='sm'), "Processing"]
    elif trigg_id == 'add_button':
        return "Save"
    else:
        return no_update