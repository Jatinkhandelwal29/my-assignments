# ================================================= 1. Practise Pandas Series ============================================

  
  

import pandas as pd




                                  # ==========  '''Create a Series from dictionary''' ============

dir={"Math": 90, "Science": 85, "English": 88}
s1 = pd.Series(dir)
print(s1,"\n")


                                  # ==========  '''Create a Series from list ''' ===========

list=[100, 95, 80, 75]
s2 = pd.Series(list)
print(s2,"\n")


                                  # =========== '''Access Series elements ''' ============


print(s2[0],"\n")
print(s2[1:3],"\n")




# ========================================== 2.DATA FRAMES ================================================




                                   # ====== Make a Pandas DataFrame with a two-dimensional Python list  ======
 

data = {
    'Field': ["Roll No", "Name", "Grade"],
    'Value': ["101", "Gourav", "A"]
}

df = pd.DataFrame(data)
print(df,"\n")


                                    # ====== Create DataFrame from Python dict ======


data2 = {
    'Name': ["Jatin", "Rohit", "Aman"],
    'Age': [19, 20, 21]
}

df = pd.DataFrame(data2)
print(df,"\n")


                                    # ====== Create Pandas DataFrame using list of lists ======



data3 = [
    ["Jatin", 19, "3rd Year"],
    ["Kannu", 20, "2nd Year"]
]

columns = ["Name", "Age", "Class"]

df = pd.DataFrame(data3, columns=columns)
print(df,"\n")



                                    # ====== Create a Pandas DataFrame using list of tuples ======


data4 = [
    ("Jatin", 19, "3rd Year"),
    ("Jhanvi", 20, "2nd Year"),
    ("Aman", 21, "1st Year")
]

columns = ["Name", "Age", "Class"]

df = pd.DataFrame(data4, columns=columns)
print(df,"\n")


                                    # ====== Create a Pandas DataFrame from List of Dicts ======


data5 = [
    {"Name": "Jatin", "Age": 22},
    {"Name": "Nanu", "Age": 21},
    {"Name": "Kannu", "Age": 23}
]

df = pd.DataFrame(data5)
print(df,"\n")




# ============================================3.DATA ITERATION =============================================




                                     # Show different ways to iterate over rows in a Pandas




data6 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df1 = pd.DataFrame(data6)

for i, row in df1.iterrows():
    print(row["Name"], row["Age"], row["City"],"\n")


                                     #  Select rows in Pandas DataFrame based on a condition


data2 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df2 = pd.DataFrame(data2)

print(df2[df2["Age"] > 20],"\n")


                                     #  Select any row from a DataFrame using iloc[] 
                                           
                                           
data3 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df3 = pd.DataFrame(data3)

print(df3.iloc[2],"\n")


                                      # Select limited rows with a given column
                                            

data4 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df4 = pd.DataFrame(data4)

print(df4["City"][1:3],"\n")


                                       #  Drop rows from the DataFrame based on a condition applied to a column
                                            

data5 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df5 = pd.DataFrame(data5)

df_drop = df5[df5["Age"] != 22]
print(df_drop,"\n")


                                       # Insert a row at a given position in a Pandas DataFrame
                                            
 
data6 = {
    'Name': ['Jatin', 'Kannu', 'Aman', 'Nanu'],
    'Age': [20, 22, 19, 25],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Kolkata']
}

df6 = pd.DataFrame(data6)

new_row = pd.DataFrame([["Kanishk", 23, "Bangalore"]], columns=["Name", "Age", "City"])
df_insert = pd.concat([df6.iloc[:2], new_row, df6.iloc[2:]]).reset_index(drop=True)
print(df_insert,"\n")
                                            
                                         
