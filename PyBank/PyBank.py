
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

#Financial Analysis
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Total: $38382578
##Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)



import csv
budget_data = ("budget_data.csv")
total_months = 0
total_profit = 0
average_change = 0
monthly_diff = []
previous_month = 0
current_greatest_increase = [0, 0]
current_greatest_decrease = [0, 0]

with open(budget_data, newline ='') as budget_data_file:
    budget_data_filereader = csv.reader(budget_data_file, delimiter = ',')
    next(budget_data_filereader, None)

    for row in budget_data_filereader:
        current_difference = int(row[1])
        #The total number of months included in the dataset
        total_months += 1

        #The net total amount of "Profit/Losses" over the entire period
        total_profit += current_difference

        #the average of the changes in "Profit/Losses" over the entire period
        monthly_diff.append([row[0], current_difference - previous_month])
        previous_month = current_difference

    for difference in monthly_diff:
        #check greatest increase
        if difference[1] > current_greatest_increase[1]:
            current_greatest_increase = difference

        if difference[1]< current_greatest_decrease[1]:
            current_greatest_decrease = difference

#print('Financial Analysis')
#print('----------------------------')
#print(f'Total Months: {total_months}')
#print(f'Profit: ${total_profit}')

newlist = []
for i in monthly_diff[1:]:
    newlist.append(i[1])

average_change = sum(newlist)/(total_months-1)
average_change = round(average_change, 2)
#print(f'Average Change: ${average_change}')
#print(f'Greatest Increase in Profits: {current_greatest_increase[0]} (${current_greatest_increase[1]})')
#print(f'Greatest Decrease in Profits: {current_greatest_decrease[0]} (${current_greatest_decrease[1]})')

string_list = []
string_list.append("Financial Analysis")
string_list.append("----------------------------")
string_list.append(f"Total Months: {total_months}")
string_list.append(f"Profit: ${total_profit}")
string_list.append(f"Average Change: ${average_change}")
string_list.append(f"Greatest Increase in Profits: {current_greatest_increase[0]} (${current_greatest_increase[1]}")
string_list.append(f"Greatest Decrease in Profits: {current_greatest_decrease[0]} (${current_greatest_decrease[1]})")

filename = "Results.txt"
with open (filename, 'w') as file:
    for i in string_list:
        print(i)
