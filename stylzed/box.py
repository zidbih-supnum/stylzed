import matplotlib.pyplot as plt
from .style import apply_style

def styled_box(data, title=""):
    apply_style()

    plt.boxplot(data)
    plt.title(title)
    plt.tight_layout()
    plt.show()
