#!/bin/bash

import os, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
    print("""       [HELP]


    Functions:
        crackit (to crack an hash)
        hashit (to hash a string)

    Algorithm suppported:
        -sha1
        -sha224
        -sha384
        -sha512
        -md5

    Specify a list for crackit:
        -w

    Usage: ./hashcrack.py crackit -sha256 <hash> -w file.txt
    """)

def banner():
    print(f"""

    [FRANCE]
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    """)

def funchash(arg):
    j = 1
    for i in arg:
        match i:
            case "-sha1":
                import hashlib
                hash = hashlib.sha1(arg[j].encode())
                return hash.hexdigest()
            case "-sha224":
                import hashlib
                hash = hashlib.sha224(arg[j].encode())
                return hash.hexdigest()
            case "-sha256":
                import hashlib
                hash = hashlib.sha256(arg[j].encode())
                return hash.hexdigest()
            case "-sha384":
                import hashlib
                hash = hashlib.sha384(arg[j].encode())
                return hash.hexdigest()
            case "-sha512":
                import hashlib
                hash = hashlib.sha512(arg[j].encode())
                return hash.hexdigest()
            case "-md5":
                import hashlib
                hash = hashlib.md5(arg[j].encode())
                return hash.hexdigest()
        j = j + 1
    j=1

def hashcrack(arg):
    if "-w" in arg:
        j = 1
        L = 1
        algo = ""
        char = ""
        list = []
        found = 0
        for t in arg:
            if '-sha' in t or "md" in  t:
                algo = t
                char = arg[L]
            L = L + 1

        for i in arg:
            if i == "-w":
                with open(arg[j], 'r') as file:
                    for line in file:
                        line = line.replace("\n", "")
                        list = [algo, line]
                        hashed_line = funchash(list)
                        if hashed_line == char:
                            print(f"\n\n{bcolors.OKGREEN}Match found!{bcolors.ENDC}\n{char} : [{bcolors.OKGREEN}{line}{bcolors.ENDC}]")
                            found = 1
                    if found == 0:
                        print(f"\n\n{bcolors.FAIL}[FAILED!]{bcolors.ENDC}")
                #return arg[j]
            j = j + 1
        j=1

def main():
    banner()
    import hashlib
    print(hashlib.algorithms_available)
    arg = sys.argv
    if "crackit" in arg:
        hashcrack(arg)
    elif "hashit" in arg:
        print(funchash(arg))
    else:
        help()

if __name__=="__main__":
    main()
import os, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
    print("""       [HELP]


    Functions:
        crackit (to crack an hash)
        hashit (to hash a string)

    Algorithm suppported:
        -sha1
        -sha224
        -sha384
        -sha512
        -md5

    Specify a list for crackit:
        -w
    """)

def banner():
    print(f"""

    [FRANCE]
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    {bcolors.OKBLUE}##########{bcolors.ENDC}##########{bcolors.FAIL}##########{bcolors.ENDC}
    """)

def funchash(arg):
    j = 1
    for i in arg:
        match i:
            case "-sha1":
                import hashlib
                hash = hashlib.sha1(arg[j].encode())
                return hash.hexdigest()
            case "-sha224":
                import hashlib
                hash = hashlib.sha224(arg[j].encode())
                return hash.hexdigest()
            case "-sha256":
                import hashlib
                hash = hashlib.sha256(arg[j].encode())
                return hash.hexdigest()
            case "-sha384":
                import hashlib
                hash = hashlib.sha384(arg[j].encode())
                return hash.hexdigest()
            case "-sha512":
                import hashlib
                hash = hashlib.sha512(arg[j].encode())
                return hash.hexdigest()
            case "-md4":
                import hashlib
                hash = hashlib.new('md4', arg[j].encode('utf-8'))
                return hash.hexdigest()
            case "-md5":
                import hashlib
                hash = hashlib.md5(arg[j].encode())
                return hash.hexdigest()
        j = j + 1
    j=1

def hashcrack(arg):
    if "-w" in arg:
        j = 1
        L = 1
        algo = ""
        char = ""
        list = []
        found = 0
        for t in arg:
            if '-sha' in t or "md" in  t:
                algo = t
                char = arg[L]
            L = L + 1

        for i in arg:
            if i == "-w":
                with open(arg[j], 'r') as file:
                    for line in file:
                        line = line.replace("\n", "")
                        list = [algo, line]
                        hashed_line = funchash(list)
                        if hashed_line == char:
                            print(f"\n\n{bcolors.OKGREEN}Match found!{bcolors.ENDC}\n{char} : [{bcolors.OKGREEN}{line}{bcolors.ENDC}]")
                            found = 1
                    if found == 0:
                        print(f"\n\n{bcolors.FAIL}[FAILED!]{bcolors.ENDC}")
                #return arg[j]
            j = j + 1
        j=1

def main():
    banner()
    import hashlib
    print(hashlib.algorithms_available)
    arg = sys.argv
    if "crackit" in arg:
        hashcrack(arg)
    elif "hashit" in arg:
        print(funchash(arg))
    else:
        help()

if __name__=="__main__":
    main()
