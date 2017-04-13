import sys

def main():
    return lprintln(lam0(2))

def lprintln(string):
    print(string)
    return 0

def lam0(x):
    return (x + 1)

if __name__ == "__main__":
    sys.exit(main())
