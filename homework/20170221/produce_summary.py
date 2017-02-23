# parameter: day counter, the db file name
# function: if it is Day1, and there are delivery data in db file
#           Prints Day1 and all delivery information
def melonDeliveryByDays(day, file):
    the_file = open(file)
    print()
    print ("Day %d"%day)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print ("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
    the_file.close()

melonDeliveryByDays(1, "um-deliveries-20140519.txt")
melonDeliveryByDays(2, "um-deliveries-20140520.txt")
melonDeliveryByDays(3, "um-deliveries-20140521.txt")

"""
# it is possible to iterate through the file name
# by using the datetime with the filename + number + extension concatination
# the above three lines also can be changed into a separate funciton
# for this exercise, there are only three lines, so the method
# is not used to save some coding lines

# below is the code for looping the date
for i in xrange(10):
   with open('file_{0}.dat'.format(i),'w') as f:
       f.write(str(func(i)))

# below is the code for calculating number of days
import datetime as dt
print((dt.date(2014,1,1) -dt.date(2011,3,3)).days)
"""