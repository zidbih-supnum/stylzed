# stylviz

A personal Python visualization library with a consistent visual style.

## Installation
pip install stylzed

## Usage

```python
import stylviz

stylviz.styled_line(
    x=[1, 2, 3],
    y=[4, 2, 5],
    title="My styled plot"
)

stylzed.styled_bar(
    categories=["A", "B", "C"],
    values=[10, 5, 8],
    title="Test Styled Bar"
)

stylzed.styled_scatter(
    x=[1, 2, 3, 4],
    y=[10, 20, 15, 25],
    title="Test Styled Scatter"
)

stylzed.styled_hist(
    data=[1, 2, 2, 3, 3, 3, 4, 4, 5],
    bins=5,
    title="Test Styled Histogram"
)

stylzed.styled_box(
    data=[10, 12, 15, 14, 18, 20],
    title="Test Styled Box"
)


