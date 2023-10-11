'''
Project - Jairo Leal - TI1010664

1.	Open the stm_incidents data file using Excel and get into understanding the structure and meanings
2.	Make a pivot table that sorts the incidents by year
3.	Make a pivot table that sorts the incidents by time (at what time during the day)
4.	Make a pivot table that sorts the incidents by “Symptome”

'''

import pandas as pd

# Task 1: Read the data and understand its structure and meanings
df = pd.read_excel(r"C:\Users\Jairo\OneDrive\Documentos\Data\Trebas\9. Middleware Technology\October_10\Incidents métro.xlsx")

# Task 2: Make a pivot table that sorts the incidents by year
df['Année civile'] = pd.to_datetime(df['Année civile'], format='%Y')
yearly_incidents = df.groupby(df['Année civile'].dt.year).size().reset_index(name="Incident_Count")

# Task 3: Make a pivot table that sorts the incidents by time (hour of the day)
df["Heure de l'incident"] = pd.to_datetime(df["Heure de l'incident"], format='%H:%M:%S').dt.hour
hourly_incidents = df.groupby("Heure de l'incident").size().reset_index(name="Incident_Count")

# Task 4: Make a pivot table that sorts the incidents by "Symptome"
symptoms_incidents = df.groupby('Symptome').size().reset_index(name="Incident_Count")

# Exporting to Excel:

yearly_incidents.to_excel('Incidents by Year.xlsx', index=False)
hourly_incidents.to_excel('Incidents by Time.xlsx', index=False)
symptoms_incidents.to_excel('Incidents by Symptom.xlsx', index=False)

'''
BREAKING DOWN 

1. **Reading Data with pandas (Task 1):** pandas provides efficient data reading capabilities for various file formats,
 including Excel. This makes it straightforward to load data and perform operations on it.

2. **Creating Pivot Tables (Tasks 2, 3, and 4):** pandas allows for easy data aggregation and pivot table creation. 
It's especially well-suited for tasks like grouping and summarizing data by specific attributes, such as year, time, 
or categories like "Symptome." The `groupby` function makes it convenient to group data based on a particular column's 
values, and you can use aggregation functions like `size()` to count the occurrences.

3. **Data Transformation (Tasks 2 and 3):** pandas allows you to manipulate datetime values easily. In Task 2, 
I converted the "Année civile" column to datetime to extract the year for grouping. 
In Task 3, I converted the "Heure de l'incident" column to datetime to extract the hour for grouping.

4. **Data Export to Excel (Phase 5):** pandas supports data export to Excel using the `to_excel()` function. 
It offers the flexibility to save the results in separate Excel files, which aligns with your requirement to create 
individual files for each pivot table.

'''
