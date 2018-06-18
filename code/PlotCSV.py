import csv
#Import plot
import matplotlib.pyplot as plt
import numpy as np

with open ('DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv', 'r') as csv_file:
    #Read csv data using dictionary reader and writer
    csv_reader = csv.DictReader(csv_file)
    i = 0
    #Access to graph
    y = []
    x=[]
    for row in csv_reader:
        #Plot 1000 rows
        if i < 1000:
            i=i+1
            #Build array to graph
            if row['CLM_FROM_DT'] <> '':
                #Choice of CLM_PMT_AMT as a characteristic
                y.append(float(row['CLM_PMT_AMT']))
                #The column CLM_FROM_DT has the year
                x.append(int(row['CLM_FROM_DT']))

#Setting up 'x' axis to length of 'y'
plt.scatter(x, y)
plt.xlabel('Time')
plt.xlim([20060000, 20180000])
plt.ylabel('CLM_PMT_AMT')
plt.title('CLM_PMT_AMT')
plt.show()
