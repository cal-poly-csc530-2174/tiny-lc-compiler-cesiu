import sys

def main():
    return lprintln((((lambda x : ((lambda y : ((y + x)))))(1))(2)))

def lprintln(string):
    print(string)
    return 0

if __name__ == "__main__":
    sys.exit(main())
