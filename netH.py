#!/usr/bin/python3
import subprocess

def greet():
    print('****************************************************************************')
    print('******************** Welcome to net-H-toolz version 1.1 ********************')
    print('********************             coded by               ********************')
    print('********************            shadowak47              ********************')
    print('****************************************************************************')


def ping():
    print('Pinging host......')

def menu():
    print('--------------------------------------------------------------------------')
    print('--------------------              MENU                --------------------')
    print('--------------------------------------------------------------------------')
    print('--------------------        1) Ping                   --------------------')
    print('--------------------        2) IP Trace               --------------------')
    print('--------------------        3) Nmap Scan              --------------------')
    print('--------------------        4) Netstat                --------------------')
    print('--------------------        5) Local user check       --------------------')
    print('--------------------        6) Check Routing Table    --------------------')
    print('--------------------------------------------------------------------------')



greet()
menu()
targetIp = input('Enter IP address/Web Address of target: \n\n')

cont = 'y'

while cont == 'y':
    menu()
    selection = input('Select action (1-6): ')

    if selection == '1':

        print('You have selected to Ping the target')
        ping()
        #subprocess.run(['ls', '-l'])
        subprocess.run(['ping', targetIp, '-c5'])
        print('Ping complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break

    elif selection == '2':

        print('You have selected to Trace the target')
        subprocess.run(['traceroute', targetIp])
        print('Trace complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break

    elif selection == '3':

        print('You have selected to perform a port scan on target')
        print('This may take some time.....')
        subprocess.run(['nmap', '-A', targetIp])
        print('Port scan complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break

    elif selection == '4':

        print('Checking for all ports(listening) on system')
        subprocess.run(['netstat', '-l'])
        print('Scan complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break

    elif selection == '5':

        print('Checking all users on system')
        subprocess.run(['w'])
        print('User check complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break

    elif selection == '6':
        print('Checking routing table')
        subprocess.run(['netstat', '-r'])
        print('Check complete!')
        cont = input('Continue Attack(y/n)? ')
        if cont != 'y':
            break








