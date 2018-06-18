import csv

#Read main .CSV file
#Read the complete data set into memory
with open ('DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv', 'r') as csv_file:
    #Read csv data using dictionary reader and writer
    csv_reader = csv.DictReader(csv_file)

    #Write out a new .CSV file
    with open ('new_csv.csv', 'wb') as new_file:
        #Choose especific columns
        fieldnames = ['DESYNPUF_ID', 'CLM_ID', 'SEGMENT', 'CLM_FROM_DT', 'CLM_THRU_DT', 'PRVDR_NUM', 'CLM_PMT_AMT', 'NCH_PRMRY_PYR_CLM_PD_AMT']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, lineterminator='\n')
        #Write specific header
        csv_writer.writeheader()

        #Start counting 0 to 1000
        i = 0
        #Read rows in complete data
        for row in csv_reader:
            #Limit first 1000 rows
            if i < 1000:
                #Write specific columns
                csv_writer.writerow({'DESYNPUF_ID':row['DESYNPUF_ID'],
                                     'CLM_ID':row['CLM_ID'],
                                     'SEGMENT':row['SEGMENT'],
                                     'CLM_FROM_DT':row['CLM_FROM_DT'],
                                     'CLM_THRU_DT':row['CLM_THRU_DT'],
                                     'PRVDR_NUM':row['PRVDR_NUM'],
                                     'CLM_PMT_AMT':row['CLM_PMT_AMT'],
                                     'NCH_PRMRY_PYR_CLM_PD_AMT':row['NCH_PRMRY_PYR_CLM_PD_AMT']
                                     })
                i=i+1

               
                
