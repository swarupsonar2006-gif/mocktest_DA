import pandas as pd

n = int(input("Enter the number of students :"))

names=[]
ages=[]
departments=[]
dates=[]

for i in range(n):
    print(f"\nEnter details for students {i+1}:")

    name = input("Enter the name:")
    age = input("Enter the age:")
    department = input("Enter the deaprtment:")
    date = input("Enter the date:")

    names.append(name)
    ages.append(age)
    departments.append(department)
    dates.append(date)

data ={
    'Name':names,
    'Age':ages,
    'Department':departments,
    'Admission_Date':dates
}    

df = pd.DataFrame(data)

print("\nStudent data:\n")
print(df)

print("\nOriginal data types:\n")
print(df.dtypes)

#1.Data type conversion
df['Age']=df['Age'].astype(int)

#2.String Manipulation
df['Name']=df['Name'].str.strip()

df['Name']=df['Name'].str.title()

df['Department']=df['Department'].str.title()

#3.Date type transformation
df['Admission_Date']=pd.to_datetime(df['Admission_Date'],format='%d-%m-%y')

#extracting year ,month ,and day from the date

df['Year']=df['Admission_Date'].dt.year
df['Month']=df['Admission_Date'].dt.month
df['Day']=df['Admission_Date'].dt.day

#display transformed dataset

print("\nTransformed Dataset:\n")
print(df)

print("\nTransformed data types:\n")
print(df.dtypes)




