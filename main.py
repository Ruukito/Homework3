import os
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('Resources', 'budget_data.csv')

months = []
profit_losses = []
total = 0
average_change = 0
anterior= 0
total_change = 0.00
greatest_increase_list = []
with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    next(csvreader,None)
    for row in csvreader:
        months.append(row[0])
        total = float(row[1]) + total


        average_change = (float(row[1]) - anterior + average_change)

        greatest_increase_list.append(float(row[1]) - anterior)
        anterior= float(row[1])
        profit_losses.append(row[1])

        
    final_list= zip(months,greatest_increase_list)
    row_anterior = 0
    row_name= ""
    row_name2 = ""
    row_mayor= 0
    row_menor = 0
    for row2 in final_list:
        
        if float(row2[1])> row_mayor:
            row_mayor= float(row2[1])
            row_name = str(row2[0])
        
        
        if float(row2[1]) < row_menor:
            row_menor= float(row2[1])
            row_name2 = str(row2[0])
            
#Ejemplo de como hacerlo mas facil
#print(greatest_increase_list.index((max(greatest_increase_list))))
#print(months[greatest_increase_list.index((max(greatest_increase_list)))])
#total_change = (average_change - float(profit_losses[0]) ) / (len(profit_losses) -1)

#https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python
formatted_float = ("${:,.0f}".format(row_mayor))
formatted_float2 = ("${:,.0f}".format(row_menor))
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:   {len(months)}")
print(f"Total: {total}")
print(f"Average Change: ${round(total_change,2)}")
print(f"Greatest Increase: {row_name} ({formatted_float}) ${round(max(greatest_increase_list))}")
print(f"Greatest Decrease: {row_name2} ({formatted_float2}) ${round(min(greatest_increase_list))}")



A = ["Financial Analysis", "Total Months:","Total:","Average Change","Greatest Increase", "Greatest Decrease"]
B = ["",len(months),total,round(total_change,2),row_name,row_name2]
C = ["","","","",formatted_float,formatted_float2]
Final_print = zip(A,B,C)

outputfile="main.csv"
with open(outputfile,"w") as datafile:
    writer=csv.writer(datafile)
    writer.writerows(Final_print)
