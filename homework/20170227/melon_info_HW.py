"""
Prints out all the melons in our inventory
"""

from melons import melon_info

def print_melon_info(melon_name):
    """Print information for melon"""

    print melon_name.upper()
    melon = melon_info[melon_name]
    for character in melon:
        print "  " + character +": "+str(melon[character])


def generate_new_key(character_name):
    for melon in melon_info:
        melon_info[melon][character_name] = None



def add_character_to_melons(character_name):
    """Add value to a key in melon

    For future use of 'Define Local initiative'
    Run to enter values to a melon character key
    """

    print "Do you know any value for the character?"
    user_input = raw_input("(y/n): " ).lower()

    if user_input == 'y':
        for melon in melon_info:
            print "Please input value for %s"%melon
            character_value = raw_input(": ")
            melon_info[melon][character_name] = character_value
    elif user_input == 'n':
        generate_new_key(character_name)
    else:
        print "Please enter y/n."


generate_new_key("flesh color")
generate_new_key("rind color")
generate_new_key("average weight")
print_melon_info("Casaba")
