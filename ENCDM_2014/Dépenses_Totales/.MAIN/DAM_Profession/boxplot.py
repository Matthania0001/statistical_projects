import plotly.graph_objects as go
import pandas as pd

class BoxPlot:
    def __init__(self, data_path, sheet_name="Sheet1", column_name="DAM"):
        self.data_path = data_path
        self.sheet_name = sheet_name
        self.column_name = column_name
        self.df = pd.read_excel(self.data_path, sheet_name=self.sheet_name)
        self.y = self.df[self.column_name]
        self.fig = go.Figure()

    def create_box_plot(self, title="Box Plot Interactif", yaxis_title="Valeurs", boxpoints='all', jitter=0.5, pointpos=-1.8):
        self.fig.add_trace(go.Box(
            y=self.y,
            name=self.column_name,
            boxpoints=boxpoints,
            jitter=jitter,
            pointpos=pointpos
        ))

        self.fig.update_layout(
            title=title,
            yaxis_title=yaxis_title,
            boxmode="group"
        )

    def save(self, filename, file_format="html"):
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")

    def show(self):
        self.fig.show()

# # Créer l'objet BoxPlotDAM
# box_plot = BoxPlot(data_path="../cleanedData/Data_wtout_na.xlsx")

# # Créer le box plot avec des titres personnalisés
# box_plot.create_box_plot(title="Distribution de DAM", yaxis_title="Valeurs de DAM")

# # Afficher le graphique
# box_plot.show()

# # Enregistrer le graphique au format HTML
# box_plot.save("box_plot_interactif.html", file_format="html")

# # Enregistrer le graphique au format PNG (nécessite l'installation de Kaleido)
# box_plot.save("box_plot_interactif.png", file_format="png")
