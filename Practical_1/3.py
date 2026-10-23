#using pandas library as pd
import pandas as pd

#Creating a DataFrame Friends
df = pd.DataFrame({
"Name":["Swarup","Krishna","Kunal","Kartik","Parth"],
"Age":[20,21,24,25,23],
"City":["Pune","Mumbai","Pune","Bangalore","Mumbai"],
"Mobileno":[1234567890,9876543210,5678901234,6789012345,7890123456],
"Zodiac Sign":["Aries","Taurus","Gemini","Cancer","Leo"],
"Hobby":["Reading","Traveling","Gaming","Cooking","Photography"]
})

print("Original Dataframe:",df,sep="\n")

#data subseting
print("\nSubset Age greater than 22:",df[df["Age"]>22],sep="\n")

#Sorting in ascending order
print("\nSorting by Age in ascending order:",df.sort_values(by="Age"),sep="\n")

#Sorting in descending order
print("\nSorting by Age in descending order:",df.sort_values(by="Age",ascending=False),sep="\n")

#Grouping using the for loop and groupby() function
print("\nGrouping by City:",df.groupby("City"),sep="\n")

#Statistical operations
print("\nStatistical Operations:")
print("\nMean Age:",df["Age"].mean())
print("\nMedian Age:",df["Age"].median())
print("\nMode of Age:",df["Age"].mode())