import pandas as pd

def calculate_average(data):
    return sum(marks) / len(marks)

names = ["Swarup","Krushna","Kunal","Sayali","Rutuja","Rohit"]
marks = [90, 80, 70, 60, 50, 40]

df = pd.DataFrame({
      "Name": names,
      "Marks": marks
      })

def result(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Marks"].apply(result)

print("\nStudent Dataset:\n")
print(df)

print("\nStudent Analysis:\n")
for mark in marks:
    if mark >= 75:
        print(f"Marks: {mark} - Result: Distinction")
    elif mark >= 60:    
        print(f"Marks: {mark} - Result: Pass")
    else:
        print(f"Marks: {mark} - Result: Fail")

print("\nAverage Marks:", calculate_average(marks))
print("\nHighest Marks:", max(marks)) 
print("Lowest Marks:", min(marks))       