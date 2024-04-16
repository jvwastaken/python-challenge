import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # list for months
    months=[]
    # list for integer-value of the profits/losses
    OverallTotal=[]


    for row in csvreader:
            months.append (row[0])
            # I want the integer value of everything in the 2nd column to be dumped into the OverallTotal list.
            OverallTotal.append (int(row[1]))
            # I got help from XPert Learning Assistant for calculating the change and average_change.
            Change = [OverallTotal[row] - OverallTotal[row-1] for row in range(1,len(OverallTotal))]
            
   
   
   
    average_change = sum(Change)/len(Change)
    max_change_index = Change.index(max(Change))
    max_change_month = months[max_change_index + 1]

    min_change_index = Change.index(min(Change))
    min_change_month = months[min_change_index + 1]

    print("Financial Analysis")
    print("------------------------------------------------------------------------")
    print("Total Months: ", len(months))

    # I got the sum() command from StackOverflow
    print("Total: ","$", sum(OverallTotal))
    # I got round(), from W3Schools
    print("Average Change: ","$", round(average_change,2))
    print("Greatest Increase in Profits:", max_change_month, "($", max(Change), ")")
    print("Greatest Decrease in Profits:", min_change_month, "($", min(Change), ")")