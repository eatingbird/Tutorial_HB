"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""


salespeople = []
melons_sold = []
# Using dictionary as a data structure is recommended
# it will make the aggregation and the search faster
# sales_info = { "sale_person_name": {
#                                     "sales_dollars": dollar value,
#                                     "sales_quantity": quantity value}
#                                     } 

f = open("sales-report.txt")
# recommend using "sales_report_file" as variable for clear definition
# also recommend import sys - and using sys.argv to enable calling other files

# this for loop can be put into function for all the old reports to use
# That way, we can migrate the old data into the new data structure
for line in f:
    line = line.rstrip()
    entries = line.split("|") 
    # entries will contain values with three different characters
    # recommend using "tokens"
    salesperson = entries[0]
    # "sales_person" for python-like code consistancy
    melons = int(entries[2])
    # "sales_quantity" for the variable recommended for clearer statement

    # below section is recommended to be
    # sales_info[sales_person][sales_amount] = \
    #   sales_info.get(sales_person, 0) + salse_info[sales_person][sales_amount]

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# for person in sales_info: # it will loop through
for i in range(len(salespeople)):
    # change the output format according to the data structure
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
