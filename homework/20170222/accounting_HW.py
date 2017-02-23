
melon_cost = 1.00

def txt_to_db(file):
    """transforms text to db

    # <sample data structure used>
    # db =[{'name':'Joe','amount': 5, 'paid': 5.00},
    #      {'name':'Frank','amount': 6, 'paid': 6.00},
    #      {'name':'Sally','amount': 3, 'paid': 3.00},
    #      {'name':'Sean','amount': 9, 'paid': 9.50},
    #      {'name':'David','amount': 4, 'paid': 4.00},
    #      {'name':'Ashley','amount': 3, 'paid': 2.00}]
    """

    the_file = open(file)
    db = []
    for line in the_file:
        tokens = line.rstrip().split('|')
        lib_items = {'name':tokens[1],'amount': float(tokens[2]), 'paid': float(tokens[3])}
        db.append(lib_items)
    return db

db = txt_to_db('customer-orders.txt')

def check_pay_status(name, amount, paid, melon_cost):
    """ Check individual customer's status"""

    expected = amount * melon_cost
    if expected != paid:
        print name, "paid {:.2f}, expected {:.2f}".format(paid, expected)


def check_all_pay_status(db):
    """Check every item in db"""

    cnt = 0
    while cnt < len(db):
        check_pay_status(db[cnt]['name'],db[cnt]['amount'],db[cnt]['paid'],melon_cost)
        cnt += 1


check_all_pay_status(db)