# Archivo de prueba para probar git
#%% cargar librerias

import numpy as np
import matplotlib.pyplot as plt
from funciones import resumen

#%load_ext autoreload
#%autoreload 2
# %%
x = np.random.normal(loc=50, scale=3, size=1000)
plt.hist(x, edgecolor="w", color="red")

# %%
resumen(x)

# %%
