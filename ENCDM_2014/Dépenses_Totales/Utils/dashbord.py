from dash import Dash, dcc, html, Input, Output, State, callback_context
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.exceptions import PreventUpdate

def create_px_dashboard(px_figures, title="Dashboard Plotly Express", cols=2):
    """
    Crée un dashboard à partir de graphiques Plotly Express existants.
    
    Args:
        px_figures (list): Liste de figures créées avec plotly.express
        title (str): Titre du dashboard
        cols (int): Nombre de colonnes pour la disposition
        
    Returns:
        Dash: Application Dash configurée
    """
    app = Dash(__name__)
    
    # Convertir les figures px en figures go
    figures = [go.Figure(fig) for fig in px_figures]
    
    # Création de la disposition en grille
    app.layout = html.Div([
        html.H1(title, style={'textAlign': 'center', 'marginBottom': '30px'}),
        
        # Conteneur principal avec la grille
        html.Div([
            html.Div([
                dcc.Graph(
                    id=f'graph-{i}',
                    figure=fig,
                    config={
                        'displayModeBar': True,
                        'scrollZoom': True,
                        'toImageButtonOptions': {
                            'format': 'png',
                            'filename': f'graph_{i+1}',
                            'height': 500,
                            'width': 700,
                            'scale': 1
                        }
                    },
                    style={
                        'height': '400px',
                        'border': '1px solid #ddd',
                        'borderRadius': '5px',
                        'padding': '10px',
                        'cursor': 'pointer'
                    }
                )
            ], style={
                'width': f'{100/cols}%',
                'display': 'inline-block',
                'padding': '10px',
                'boxSizing': 'border-box'
            }) for i, fig in enumerate(figures)
        ], style={
            'display': 'flex',
            'flexWrap': 'wrap',
            'justifyContent': 'center',
            'maxWidth': '1200px',
            'margin': '0 auto'
        }),
        
        # Modal pour l'affichage agrandi
        dcc.Store(id='current-fig-index', data=None),
        html.Div(
            id='modal',
            style={
                'position': 'fixed',
                'top': 0,
                'left': 0,
                'width': '100%',
                'height': '100%',
                'backgroundColor': 'rgba(0,0,0,0.5)',
                'zIndex': 1000,
                'display': 'none',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            children=[
                html.Div(
                    style={
                        'backgroundColor': 'white',
                        'padding': '20px',
                        'borderRadius': '10px',
                        'width': '90%',
                        'maxWidth': '1200px',
                        'maxHeight': '90vh',
                        'position': 'relative'
                    },
                    children=[
                        html.Button(
                            '×',
                            id='close-modal',
                            style={
                                'position': 'absolute',
                                'right': '15px',
                                'top': '10px',
                                'fontSize': '24px',
                                'background': 'none',
                                'border': 'none',
                                'cursor': 'pointer',
                                'zIndex': 1001
                            }
                        ),
                        dcc.Graph(
                            id='expanded-graph',
                            style={
                                'height': '90vh',
                                'width': '100%'
                            },
                            config={
                                'displayModeBar': True,
                                'scrollZoom': True,
                                'toImageButtonOptions': {
                                    'format': 'png',
                                    'filename': 'expanded_graph',
                                    'height': 800,
                                    'width': 1200,
                                    'scale': 1
                                }
                            }
                        )
                    ]
                )
            ]
        )
    ])
    
    # Callbacks pour la fonctionnalité d'agrandissement
    @app.callback(
        Output('modal', 'style'),
        Output('expanded-graph', 'figure'),
        Output('current-fig-index', 'data'),
        [Input(f'graph-{i}', 'clickData') for i in range(len(figures))],
        [Input('close-modal', 'n_clicks')],
        [State('current-fig-index', 'data')]
    )
    def handle_graph_clicks(*args):
        ctx = callback_context
        
        if not ctx.triggered:
            raise PreventUpdate
        
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        # Fermer le modal
        if trigger_id == 'close-modal':
            return {'display': 'none'}, go.Figure(), None
        
        # Ouvrir le modal avec le bon graphique
        if trigger_id.startswith('graph-'):
            fig_index = int(trigger_id.split('-')[1])
            return (
                {'display': 'flex'},
                figures[fig_index],
                fig_index
            )
        
        raise PreventUpdate
    
    return app

# Exemple d'utilisation
