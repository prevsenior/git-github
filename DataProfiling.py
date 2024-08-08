#%%
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# Verifique a versão do NumPy
print("NumPy version:", np.__version__)

# Crie um DataFrame de exemplo
df = pd.read_csv("customers-1000.csv")

# Gere o relatório de profiling
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# Salve o relatório como um arquivo HTML
profile.to_file("report.html")

# %%
import pandas as pd
import sweetviz as sv

# Crie um DataFrame de exemplo
df = pd.read_csv("customers-1000.csv")

# Gere o relatório de Sweetviz
report = sv.analyze(df)

# Para visualizar o relatório no notebook (se você estiver usando Jupyter Notebook)
report.show_html("sweetviz_report.html")
