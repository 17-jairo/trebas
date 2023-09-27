import pandas as pd
#import openpyxl


trebas = pd.read_excel(r"C:\Users\Jairo\OneDrive\Documentos\Data\Trebas\9. Middleware Technology\Sept 26 -  exercise\TREBAS.xlsx")
concordia = pd.read_excel(r"C:\Users\Jairo\OneDrive\Documentos\Data\Trebas\9. Middleware Technology\Sept 26 -  exercise\Concordia.xlsx")
print(trebas.head(10))
print(concordia.head(10))

resultado = pd.concat([trebas, concordia], axis=1)
print(resultado.head(10))

resultado.to_excel('trebas_concordia.xlsx', index=False)

