import matplotlib.pyplot as plt

def apply_style():
    plt.style.use("default")

    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "axes.titlesize": 14,
        "lines.linewidth": 2.5,
        "font.family": "sans-serif",
    })
