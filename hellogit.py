# Archivo de prueba para probar git
#%% cargar librerias

import numpy as np
import matplotlib.pyplot as plt
from funciones import resumen
from graficas import histograma
from hipotesis import z_test

#%load_ext autoreload
#%autoreload 2
# %% histograma
x = np.random.normal(loc=50, scale=3, size=1000)

#%%
histograma(x)

# %% resumen estadístico
resumen(x)

# %% prueba de hipótesis
z_test(x, mu=54, sigma=4)
# %%
