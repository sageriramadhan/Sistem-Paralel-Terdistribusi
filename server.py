from SimpleXMLRPCServer import SimpleXMLRPCServer
from sys import argv
ACCOUNT_FILE = "databrankas.txt"

def deposit(acnt, amt): 
    return change_val(acnt, amt)

def withdraw(acnt, amt):
    return change_val(acnt, -1*amt)

def inquire(acnt):
    accnts = get_accounts()
    try:
        amt = accnts[acnt]
        return amt
    except KeyError:
        return None

def transfer(acnt1, acnt2, amt):
    accnts = get_accounts()
    try:
        accnts[acnt1] -= amt
    except KeyError:
        return (False, False)
    try:
        accnts[acnt2] += amt
    except KeyError:
        return(True, False)
    write_accounts(accnts)
    return (True, True)

def change_val(acnt, amt):
    accnts = get_accounts()
    try:
        accnts[acnt] += amt
        write_accounts(accnts)
        return True
    except(KeyError):
        return False

def get_accounts():
    accnts = {}
    try:
        f = open(ACCOUNT_FILE, 'r')
        for line in f:
            vals = line.rstrip().partition(',')
            accnts[vals[0]] = int(vals[2])
        f.close()
    except IOError:
        print("Gagal membuka {}".format(ACCOUNT_FILE))
    return accnts
    
def write_accounts(accnts):
    try:
        f = open(ACCOUNT_FILE, 'w')
        for (key,val) in accnts.iteritems():
            f.write("{},{}\n".format(key,val))
        f.close()
    except IOError:
        print("Gagal memperbaharui {} :(".format(ACCOUNT_FILE))
        
def main():
    try:
        if len(argv) != 2:
            raise IndexError()
        port_num = int(argv[1])
    except IndexError:
        print("Gunakan Perintah> python server.py 'port'")
        exit()
        
    try:    
        server = SimpleXMLRPCServer(
            ("127.0.0.1", port_num),
            allow_none=True)
    except Exception as e:
        print e
        print("gagal menggunakan jaringan")
        exit()
        
    server.register_introspection_functions()
    server.register_function(deposit)
    server.register_function(withdraw)
    server.register_function(inquire)
    server.register_function(transfer)
    server.serve_forever()
    
main()
