import pandas as pd

#Creating the demo data
df = pd.DataFrame({
    "Name": ["Swarup","Krushna","Kunal","Sayali","Rutuja","Rohit"],
    "Dept": ["CSE","MEC","CHEM","IT","ENTC","CSE"],
    "Marks": [90, 80, 70, 60, 50, 40]
})

#Original Data
print("\nStudent Dataset:\n",df)

#Subsetting the data
print("\nSubset (Marks > 60):\n",df[df["Marks"] > 60])

#Sorting in ascending order 
print("\nSorted by marks (Ascending):\n",df.sort_values(by="Marks"))

#Sorting in descending order
print("\nSorted by marks (Descending):\n",df.sort_values(by="Marks", ascending=False))

#Grouping 
print("\nGrouped(AVerage Marks by Dept):\n",df.groupby("Dept")["Marks"].mean())

#Statistical Data
print("\nMean =",df["Marks"].mean())
print("Median =",df["Marks"].median())
print("Mode =")
print(df["Marks"].mode())

