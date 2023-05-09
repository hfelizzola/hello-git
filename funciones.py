# Crear un resumen estadístico
import numpy as np

def resumen(x):
    n = len(x)
    mean = np.mean(x)
    desv_est = np.std(x, ddof=n-1)
    rango = np.max(x) - np.min(x)
    return mean, desv_est, rango, n