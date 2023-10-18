import csv
import matplotlib.pyplot as plt
zipcodes=[]
district_count={}
district_name={}
with open('Dataset/Maharashtra.csv',newline='',encoding='ISO-8859-1') as csvfile:
    dataset= csv.DictReader(csvfile)
    for row in dataset:
        row['DATE_OF_REGISTRATION']=str(row['DATE_OF_REGISTRATION'])
        if row['DATE_OF_REGISTRATION'][-2:]=='15' and row['Registered_Office_Address'][-6:]!='000000':
            val=row['Registered_Office_Address'][-6:]
            zipcodes.append(val)
            
print(len(zipcodes))
with open('Dataset/pincode.csv',newline='',encoding='ISO-8859-1') as csvfile:
    dataset= csv.DictReader(csvfile)
    
    for row in dataset:
        district_name[row['Pin Code']]=row['District']
        district_count[row['District']]=0
for i in zipcodes:
    if i in district_name.keys():
        district_count[district_name[i]]+=1

plt.bar(district_count.keys(),district_count.values())
plt.show()