import jupytext

markdown = jupytext.read("main.md")
jupytext.write(markdown, "output.ipynb")