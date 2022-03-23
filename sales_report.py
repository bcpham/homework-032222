"""Generate sales report showing total melons each salesperson sold."""

# 1)Read through sales_report.py and understand the code
# 2)Write comments explaining what each line of code is doing
# 3)Write comments explaining any improvements you can think of:

        #Improvements will be to remove the if/else statements and instead
        #implement a dictionary that will take in the full name as a key and
        #the cumulated sum of melons as the value

# 4)If you have time, feel free to implement your suggested improvements
        #Ok

# salespeople = []                    #Defines a blank list called salespeople
# melons_sold = []                    #Defines a blank list called melons_sold

melons_dict = {}

f = open('sales-report.txt')        #Opens a text file

for line in f:                      #Iterates thru each line in f
    line = line.rstrip()            #Removes white space on the right side
    entries = line.split('|')       #Uses the | key as a delimiter and same line is renamed entries
    salesperson = entries[0]        #The first element is named salesperson
    melons = int(entries[2])        #The third element is the qty. of melons as an integer

    if salesperson not in melons_dict:
        melons_dict[salesperson] = melons

    else:
        melons_dict[salesperson] += melons

    # if salesperson in salespeople:                  #Conditional statement for salesperson in salespeople list
    #     position = salespeople.index(salesperson)   #From the salespeople list, return the index of where element salesperson is
    #     melons_sold[position] += melons             #To the position of the melons_sold list, add melon qty.
    #     #print(position)
    # else:
    #     salespeople.append(salesperson)             #add salesperson to the end of salespeople list
    #     melons_sold.append(melons)                  #add melons to the end of melons_sold list


#for i in range(len(salespeople)):   #Iterates thru the range of salespeople list (0,..., length-1)
    #print(f'{salespeople[i]} sold {melons_sold[i]} melons') #Prints out a statement for the report

for key in melons_dict:
    print(f'{key} sold {melons_dict[key]}')