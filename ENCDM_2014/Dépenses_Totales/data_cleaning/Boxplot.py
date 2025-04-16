import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Cleaning import Donnee

def save_plot(fig: plt.Figure, save_path: str, dpi: int = 300) -> None:
    """
    Sauvegarde un graphique matplotlib.

    Paramètres:
    -----------
    fig : matplotlib.figure.Figure
        La figure matplotlib à sauvegarder.
    save_path : str
        Chemin pour sauvegarder le graphique (ex: 'output/boxplot.png').
    dpi : int
        Résolution pour l'export (points par pouce).
    """
    if save_path:
        fig.savefig(save_path, dpi=dpi, bbox_inches='tight')
        print(f"Graphique sauvegardé à l'emplacement : {save_path}")

def plot_boxplot(data: pd.DataFrame, columns='all', orientation='vertical', figsize=(10, 6), 
                 save_path: str = None, dpi: int = 300, show_stats: bool = True) -> None:
    """
    Génère un boxplot professionnel pour une ou plusieurs colonnes.
    
    Paramètres:
    -----------
    data : DataFrame
        Votre jeu de données
    columns : str/list
        'all' pour toutes les colonnes numériques, ou liste des colonnes cibles
    orientation : str
        'vertical' (par défaut) ou 'horizontal'
    figsize : tuple
        Taille du graphique (largeur, hauteur)
    save_path : str
        Chemin pour sauvegarder le graphique (ex: 'output/boxplot.png')
    dpi : int
        Résolution pour l'export (points par pouce)
    show_stats : bool
        Affiche les statistiques clés si True
    """
    
    # Sélection des colonnes
    if columns == 'all':
        numeric_cols = data.select_dtypes(include=['number']).columns
        if len(numeric_cols) == 0:
            raise ValueError("Aucune colonne numérique trouvée dans le DataFrame.")
        cols = numeric_cols
    else:
        if isinstance(columns, str):
            cols = [columns]
        else:
            cols = columns
        
        # Vérification que les colonnes existent
        missing_cols = [col for col in cols if col not in data.columns]
        if missing_cols:
            raise ValueError(f"Colonnes non trouvées: {missing_cols}")

    # Vérification des données numériques
    for col in cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')  # Convertir en numérique
        if data[col].isna().all():
            raise ValueError(f"La colonne '{col}' ne contient aucune donnée numérique après conversion.")
    
    # Configuration du style
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.family'] = 'DejaVu Sans'
    
    # Création de la figure
    fig, ax = plt.subplots(figsize=figsize)
    
    # Boxplot pandas (gère automatiquement single/multiple columns)
    if orientation == 'horizontal':
        data[cols].plot.box(vert=False, patch_artist=True, ax=ax)
        ax.set_xlabel('Valeurs', fontsize=12)
        ax.set_ylabel('Variables', fontsize=12)
    else:
        data[cols].plot.box(vert=True, patch_artist=True, ax=ax)
        ax.set_ylabel('Valeurs', fontsize=12)
        ax.set_xlabel('Variables', fontsize=12)
    
    # Personnalisation
    ax.set_title('Distribution des valeurs', fontsize=14, pad=20)
    
    # Ajout des statistiques
    if show_stats:
        for i, col in enumerate(cols):
            stats = data[col].describe()
            textstr = (f"{col}\n"
                       f"Médiane = {stats['50%']:.2f}\n"
                       f"Q1 = {stats['25%']:.2f}\n"
                       f"Q3 = {stats['75%']:.2f}")
            
            if orientation == 'horizontal':
                ax.text(0.95, 0.85 - i*0.1, textstr,
                        transform=ax.transAxes,
                        bbox=dict(facecolor='white', alpha=0.8),
                        ha='right')
            else:
                ax.text(i+1, stats['max']*1.05, textstr,
                        bbox=dict(facecolor='white', alpha=0.8),
                        ha='center')

    # Ajustements finaux
    plt.xticks(rotation=45 if len(cols) > 3 else 0)
    plt.tight_layout()
    
    # Sauvegarde via la fonction dédiée
    save_plot(fig, save_path, dpi)

    # Affichage du graphique
    plt.show()

