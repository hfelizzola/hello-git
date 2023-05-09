import matplotlib.pyplot as plt

def histograma(x, title="Histograma"):
    plt.hist(x)
    plt.title(title)
    plt.show()