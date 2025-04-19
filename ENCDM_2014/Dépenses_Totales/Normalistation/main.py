from transfo import Transformation
from Cleaning import Donnee
import numpy as np
from scipy import stats
a = Donnee("../cleanedData/Data_wtout_na.xlsx", ".xlsx")
a._load_data()
a.remove_empty(["DAM", "Age_CM"])
a.remove_duplicates()
# a.remove_outliers("DAM")
# a.remove_outliers("Age_CM")
# a.remove_outliers("DAM_G1")
# a.remove_outliers("DAM_G2")
# a.remove_outliers("DAM_G3")
# a.remove_outliers("DAM_G4")
# a.remove_outliers("DAM_G5")
# a.remove_outliers("DAM_G6")
# a.remove_outliers("DAM_G7")
# a.remove_outliers("DAM_G8")
# a.remove_outliers("DAM_G9")
#a.remove_outliers("Age_CM")

def box_cox(data, lambda_param=0.5):
    transformed_data, optimal_lambda = stats.boxcox(data)    
    return transformed_data.tolist()
def square(x):
    return x**2
def log(x):
    return np.log(x)
def inverse(x):
    return 1/x
def racine(x):
    return x**(1/2)
def z_score(x):
    return (x - x.mean()) / x.std()
def func_gauss(x):
    return 10000/(x.std() * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - x.mean()) / x.std())**2)
b = Transformation(a.df, [square, log, racine, inverse, z_score, func_gauss, box_cox], ["DAM"])
b.transformation()
b.save_excel()