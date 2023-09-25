#1.Adding record for csv file
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
# 5 product details print in csv file directly
rows=[
    [1,'Keybord',9500,8500,9600,10000,11000,10500],
    [2,'Mouse',5600,4500,3000,5800,6000,6500],
    [3,'Monitor',15000,10500,18000,9000,8500,12000],
    [4,'CPU',36000,30000,45000,40000,32000,31000],
    [5,'Printer',4500,5600,7500,9000,8500,9500]
     ]
# create empty list to store more 7 product details from user input
l=[] 
for i in range(7):
    n=int(input('Enter Product Id:'))
    name=input('Enter Product Name:')
    jan=int(input('Enter Jan Month Selling:'))
    feb=int(input('Enter Feb Month Selling:'))
    march=int(input('Enter March Month Selling:'))
    april=int(input('Enter April Month Selling:'))
    may=int(input('Enter May Month Selling:'))
    jun=int(input('Enter Jun Month Selling:'))
#   create a list 
    data=[n,name,jan,feb,march,april,may,jun]
    l.append(data)

from csv import writer
file="c://sqlite3//product.csv"
with open(file,"w",newline="")as write_file:
#     create the writer object
    write=writer(write_file)
#     adding header to the csv file
    write.writerow(header)
#     adding 5 record directly
    write.writerows(rows)
#     adding 7 record from user
    write.writerows(l)
    print('successfully file created and data inserted')


#2.Create DATAFRAME
import pandas as pd
df=pd.read_csv(file)
print(df)


#3.Change Column Name

df.columns=['Product No','Product Name','January','February','March','April','May','June']
print(df)


#4.Add column "Total Sell" to count total of all month and "Average Sell"

df['Total Sell']=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
print(df)

#5.Add 2 row at the end.

len(df)

df.loc[12]=[13,'Camera',4500,6000,10000,9500,8500,8000,46500]
df.loc[13]=[14,'Head-phone',6500,7200,3600,4500,9000,6000,36800]
print(df)

#6.Add 2 rows after 3rd row.
#7.Display first 5 rows
df.head()

#8.Display Last 5 rows
df.tail()

#9.Display row 6 to 10
df.loc[6:10]

#10.Display only Product Name
df['Product Name']

#11.Print Sell Of January Month With Product id and Product Name
df[['January','Product No','Product Name']]

#12.print only those Product No,Product Name where January Sell>5000 and February>8000
print(df[(df["January"] > 5000) & (df["February"] > 8000)][["Product No", "Product Name"]])

#13.Print Record in sorting order of Product Name

sorted_name=df.sort_values(by='Product Name')
sorted_name

#14.display in a odd index number
df.loc[1::2]

#15.Print Alternate row.
df.loc[::2]
