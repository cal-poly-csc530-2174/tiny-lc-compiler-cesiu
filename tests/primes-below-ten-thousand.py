import sys

sys.setrecursionlimit(100000)

def main():
    return ((lambda dividesP : (((lambda prime_loop : (((lambda isPrimeP : (((lambda loop : (((loop(loop))(10000))))((lambda loop : ((lambda n : (((2 if (2 + (-1 * n)) <= 0 else ((((lambda x : (((loop(loop))((n + -1)))))(lprintln(n))) if (1 + (-1 * ((isPrimeP(isPrimeP))(n)))) <= 0 else ((loop(loop))((n + -1)))) if (((isPrimeP(isPrimeP))(n)) + (-1 * 1)) <= 0 else ((loop(loop))((n + -1))))) if (n + (-1 * 2)) <= 0 else ((((lambda x : (((loop(loop))((n + -1)))))(lprintln(n))) if (1 + (-1 * ((isPrimeP(isPrimeP))(n)))) <= 0 else ((loop(loop))((n + -1)))) if (((isPrimeP(isPrimeP))(n)) + (-1 * 1)) <= 0 else ((loop(loop))((n + -1)))))))))))))((lambda isPrimeP : ((lambda n : ((((prime_loop(prime_loop))(n))((n + -1)))))))))))((lambda prime_loop : ((lambda n : ((lambda divisor : (((1 if (1 + (-1 * n)) <= 0 else ((1 if (1 + (-1 * divisor)) <= 0 else ((0 if (1 + (-1 * (((dividesP(dividesP))(divisor))(n)))) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1)))) if ((((dividesP(dividesP))(divisor))(n)) + (-1 * 1)) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1))))) if (divisor + (-1 * 1)) <= 0 else ((0 if (1 + (-1 * (((dividesP(dividesP))(divisor))(n)))) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1)))) if ((((dividesP(dividesP))(divisor))(n)) + (-1 * 1)) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1)))))) if (n + (-1 * 1)) <= 0 else ((1 if (1 + (-1 * divisor)) <= 0 else ((0 if (1 + (-1 * (((dividesP(dividesP))(divisor))(n)))) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1)))) if ((((dividesP(dividesP))(divisor))(n)) + (-1 * 1)) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1))))) if (divisor + (-1 * 1)) <= 0 else ((0 if (1 + (-1 * (((dividesP(dividesP))(divisor))(n)))) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1)))) if ((((dividesP(dividesP))(divisor))(n)) + (-1 * 1)) <= 0 else (((prime_loop(prime_loop))(n))((divisor + -1))))))))))))))))((lambda dividesP : ((lambda divisor : ((lambda n : (((lambda loop : (((loop(loop))(1))))((lambda loop : ((lambda m : (((1 if (n + (-1 * (divisor * m))) <= 0 else (0 if ((n + (-1 * (divisor * m))) + (-1 * 1)) <= 0 else ((loop(loop))((m + 1))))) if ((divisor * m) + (-1 * n)) <= 0 else (0 if ((n + (-1 * (divisor * m))) + (-1 * 1)) <= 0 else ((loop(loop))((m + 1)))))))))))))))))))

def lprintln(string):
    print(string)
    return 0

if __name__ == "__main__":
    sys.exit(main())
