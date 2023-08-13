#import resource data
import csv
csv_path = 'Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv'

#open the file
profit = 0
total_profit = 0
months = 0
profit_list = []
with open(csv_path) as bank_file:
    #create a csv reader
    csv_reader = csv.reader(bank_file)
    #get the header
    header = next(csv_reader)
    print(header)
    #loop through the data
    for line in csv_reader:
        #count months
        months = months+1
        #count total profit
        profit = int(line[1])
        profit_list.append(profit)
        total_profit = int(total_profit) + int(profit)
    
    max_profit = int(max(profit_list))
    min_profit = int(min(profit_list))     
        

print(total_profit)
print(months)
print(max_profit)
print(min_profit)
print(round(total_profit/months))