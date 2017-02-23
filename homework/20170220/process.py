log_file = open("um-server-01.txt")
''' variable "log_file" is assigned the value of the opened content 
 of the "um-server-01.txt"'''
 
def sales_reports(log_file): 
# defines function "sales_reports", and take one parameter of "log_file"
    for line in log_file:
    # iterate through the lines of log_file 
    # line is an iteration variable. each line is becomes a value
        line = line.rstrip()
        ''' rstrip method definition found online:
         Returns a copy of the string with trailing characters removed. 
         String specifying the set of characters to be removed. 
         If omitted or None, the chars argument defaults to removing whitespace. 
         The chars argument is not a prefix; rather, 
         all combinations of its values are stripped.
         >>> '   spacious   '.rstrip()
        '   spacious'
        >>> "AABAA".rstrip("A")
        'AAB'
        >>> "ABBA".rstrip("AB") # both AB and BA are stripped
        ''
        >>> "ABCABBA".rstrip("AB")
        'ABC'
        
         since there is no character inside the rstrip,
         it will eliminate white spaces at the end of each lines'''
        
        day = line[0:3]
        # day is defined as the first to third characters of the line (0-2 index)
        if day == "Mon":
        # if the day variable set above is Mon,
            print line
            # then print the line value 

sales_reports(log_file)
''' run the sales_report function with log_file variable
to get all the lines that start with Mon from the um-server-01.txt file'''
