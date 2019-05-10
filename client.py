import xmlrpclib
import httplib
from sys import argv
import socket

def deposit(acnt, amt):
    if amt <= 0:
        print("Dana yang dideposit harus lebih besar dari 0")
    elif server.deposit(acnt, amt):
        print("berhasil deposit sebesar Rp{} ke ID_Nasabah {}!".format(amt, acnt))
    else:
        print("Tidak ditemukan ID_Nasabah, {}!".format(acnt))

def withdraw(acnt, amt):
    if amt <= 0:
        print("Dana yang diambil harus lebih besar dari 0")
    elif server.inquire(acnt) < amt:
        print("Saldo Anda Tidak Mencukupi")
    else:
        if server.withdraw(acnt, amt):
            print("Berhasil melakukan penarikan sebesar Rp{} ke ID_Nasabah {}!".format(amt,acnt))
        else:
            print("Tidak ditemukan ID_Nasabah, {}!".format(acnt))
    
def inquire(acnt):
    amt = server.inquire(acnt)
    if amt is not None:
        print("Saldo Nasabah {} sebesar Rp{}".format(acnt, amt))
    else:
        print("Tidak ada Nasabah, {}!".format(acnt))
        
def transfer(acnt1, acnt2, amt):
    if amt <= 0:
        print("Dana yang ditransfer harus lebih besar dari 0")
    else:
        ans = server.transfer(acnt1, acnt2, amt)
        if ans[0] is False:
            print("Tidak ditemukan ID_Nasabah, {}!".format(acnt1))
        elif ans[1] is False:
            print("Tidak ditemukan ID_Nasabah, {}!".format(acnt2))
        elif server.inquire(acnt1) < amt:
            print("Saldo {} Tidak Mencukupi".format(acnt1))
        else:
            print("Berhasil memindahkan dana sebesar Rp{} dari Nasabah {} kepada {}!"
                .format(amt, acnt1, acnt2))
        
def parsecmd(cmd):
    if len(cmd) == 2 and cmd[0] == 'CekSaldo':
        inquire(cmd[1])
    elif len(cmd) == 3 and cmd[0] == 'Deposit':
        deposit(cmd[1], int(cmd[2]))
    elif len(cmd) == 3 and cmd[0] == 'Penarikan':
        withdraw(cmd[1], int(cmd[2]))
    elif len(cmd) == 4 and cmd[0] == 'Transfer':
        transfer(cmd[1], cmd[2], int(cmd[3]))
    else:
        return False
    return True

class TimeoutTransport(xmlrpclib.Transport):
    timeout = 10.0
    def set_timeout(self, timeout):
        self.timeout = timeout
    def make_connection(self, host):
        h = httplib.HTTPConnection(host, timeout=self.timeout)
        return h      

class ServerConnection():
    def __init__(self, address_port):
        (self.address, self.port_num) = address_port.split(':')
        self.server = xmlrpclib.ServerProxy(
            'http://'+self.address+':'+self.port_num,
            transport=TimeoutTransport())
        
def main():
    global server
    try:
        server = ServerConnection(argv[1]).server
        if not parsecmd(argv[2:]):
            raise IndexError()
    except (IndexError, ValueError) as e:
        print("Gunakan Perintah > python client.py 'server':'port' cmd")
        print("     cmd adalah [CekSaldo | Penarikan | Deposit | Transfer]")
        print("")
        print("     Contoh:")
        print("       Deposit 'Nasabah' 'Dana Masuk'")
        print("       Penarikan 'Nasabah' 'Dana Keluar'")
        print("       CekSaldo 'Nasabah'")
        print("       Transfer 'Nasabah Pengirimin' 'Nasabah Penerima' 'Besar Dana'")
    except socket.error as e:
        print("Socket Error")
        print e
    except Exception as e:
        print e
        
if __name__ == '__main__':
    main()
