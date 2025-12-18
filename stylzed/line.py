import matplotlib.pyplot as plt
from .style import apply_style

def styled_line(x, y, title="", xlabel="", ylabel=""):
    apply_style()

    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
