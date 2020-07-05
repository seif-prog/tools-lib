# This program writen by python 2
#                  Author  : Seif


'''
import
'''
  
from Core import *
import sys


'''
Main
'''
#Home
def SN():
    os.system('clear')
    main_logo()
    print (' {1} -> fsociety')
    print (' {2} -> errorcybertool')
    print (' {3} -> Tool-X')
    print (' {4} -> Nmap')
    print (' {5} -> RED_HAWK')
    print (' {6} -> sherlock')
    print (' {7} -> txtool')
    print (' {8} -> ASU')
    print (' {9} -> Lazymux')
    print (' {10} -> just-for-fun')
    print (' {11} -> Hash-generator')
    print (' {12} -> FBBrute3')
    print (' {13} -> facebook brute')
    print (' {14} -> OSIF')
    print (' {15} -> SET')
    print ('\n {99} -> To Exit \n')
    choice = raw_input (SNprompet)
    if choice == '1':        fsociety()
    elif choice == '2':        errorcybertool()
    elif choice == '3':        toolx()
    elif choice == '4':        nmap()
    elif choice == '5':        red_hawk()
    elif choice == '6':        sherlock()
    elif choice == '7':        txtool()
    elif choice == '8':        ASU()
    elif choice == '9':        Lazymux()
    elif choice == '10':        just_for_fun()
    elif choice == '11':        Hash_generator()
    elif choice == '12':        fbBrute3()
    elif choice == '13':        fbbrute()
    elif choice == '14':        osif()
    elif choice == '15':        SET()
    elif choice == '99':        sys.exit()

SN()
