import csv

#Create new variables to help count rows "ICD9_DGNS_CD_1" and "OT_PHYSN_NPI"
count_ICD9_DGNS_CD_1=0
count_OT_PHYSN_NPI=0

#Read main csv file
#Read the complete data set into memory
with open ('DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv', 'r') as csv_file:
    #Read csv data using dictionary reader and writer
    csv_reader = csv.DictReader(csv_file)

    #Verify each row in complete data
    for row in csv_reader:
        #Count the rows with ICD9_DGNS_CD_1 value of "V5861"
        if (row['ICD9_DGNS_CD_1']) ==  "V5861":
            count_ICD9_DGNS_CD_1 += 1
        #Count the rows without a value for OT_PHYSN_NPI
        if (row['OT_PHYSN_NPI']) == "":
            count_OT_PHYSN_NPI += 1
            
    #Show the results
    #Return the count of rows with ICD9_DGNS_CD_1 value of "V5861"
    print "The count of rows with 'ICD9_DGNS_CD_1' value of 'V5861': ", count_ICD9_DGNS_CD_1
    #Return the count of rows without a value for OT_PHYSN_NPI
    print "The count of rows without a value for 'OT_PHYSN_NPI': ", count_OT_PHYSN_NPI
