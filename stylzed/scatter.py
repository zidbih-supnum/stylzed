import matplotlib.pyplot as plt
from .style import apply_style

def styled_scatter(x, y, title=""):
    apply_style()

    plt.scatter(x, y, s=60)
    plt.title(title)
    plt.tight_layout()
    plt.show()
