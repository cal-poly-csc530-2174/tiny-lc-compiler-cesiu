# Lambda Calculus -> Python Translator
# CPE 530, Spring '17
# Andrew Tran and Christopher Siu

import sys

from sexpdata import loads as parse

# LC = num
#    | id
#    | (λ (id) LC)
#    | (LC LC)
#    | (+ LC LC)
#    | (* LC LC)
#    | (ifleq0 LC LC lC)
#    | (println LC)
# Do we want to hardcode +, -, ifleq0, and println, or make them lambdas?

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 translate.py <file>", file = sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r") as lamc_src,\
         open("ltp.out", "w") as py_out:
        py_out.write("%s\n" % str(parse(lamc_src.read().strip())))

if __name__ == "__main__":
    main()
