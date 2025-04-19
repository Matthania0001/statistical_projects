import pandas as pd
import plotly.express as px

class Histogramme:
    def __init__(self, fichier, sheet_name="Sheet1"):
        """
        Initialise et charge les données depuis un fichier Excel.
        """
        self.fichier = fichier
        self.sheet_name = sheet_name
        self.df = None
    
    def charger_donnees(self):
        """
        Charge les données dans un DataFrame.
        """
        self.df = pd.read_excel(self.fichier, sheet_name=self.sheet_name)

    def tracer_histogramme(self, colonne, nbins=None, couleur='black', epaisseur_bordure=1,
                           titre_graphe="Histogramme", titre_x=None, titre_y="Fréquence"):
        """
        Trace un histogramme interactif avec Plotly.

        Args:
            colonne (str): Nom de la colonne à tracer.
            nbins (int, optional): Nombre de classes. Défaut = auto.
            couleur (str, optional): Couleur de la bordure. Défaut = 'black'.
            epaisseur_bordure (int, optional): Largeur de la bordure. Défaut = 1.
            titre_graphe (str, optional): Titre principal du graphique.
            titre_x (str, optional): Titre de l'axe X.
            titre_y (str, optional): Titre de l'axe Y.
        """
        if self.df is None:
            raise ValueError("Les données n'ont pas été chargées. Utilisez 'charger_donnees()' d'abord.")
        
        x = self.df[colonne]
        fig = px.histogram(x=x, nbins=nbins)
        fig.update_traces(marker_line_color=couleur, marker_line_width=epaisseur_bordure)
        
        # Mise à jour des titres
        fig.update_layout(
            title=titre_graphe,
            xaxis_title=titre_x if titre_x else colonne,
            yaxis_title=titre_y
        )

        self.fig = fig  # Stocke le graphique pour réutilisation

    def afficher(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if hasattr(self, 'fig'):
            self.fig.show()
        else:
            raise AttributeError("Aucun graphique à afficher. Utilisez 'tracer_histogramme()' d'abord.")

    def enregistrer_html(self, chemin_fichier):
        """
        Enregistre le graphique sous format HTML.
        """
        if hasattr(self, 'fig'):
            self.fig.write_html(chemin_fichier)
        else:
            raise AttributeError("Aucun graphique à enregistrer. Utilisez 'tracer_histogramme()' d'abord.")


# --- Exemple d'utilisation ---
# if __name__ == "__main__":
#     d = Donnee("../cleanedData/Data_wtout_na.xlsx")
#     d.charger_donnees()
#     d.tracer_histogramme(
#         colonne="DAM",
#         titre_graphe="Répartition des valeurs de DAM",
#         titre_x="Valeurs de DAM",
#         titre_y="Nombre d'occurrences"
#     )
#     d.afficher()
#     d.enregistrer_html("histogramme_dam.html")
