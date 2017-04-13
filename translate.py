# Lambda Calculus -> Python Translator
# CPE 530, Spring '17
# Andrew Tran and Christopher Siu

import sys

from sexpdata import Symbol, loads as parse

# LC = num
#    | id
#    | (λ (id) LC)
#    | (LC LC)
#    | (+ LC LC)
#    | (* LC LC)
#    | (ifleq0 LC LC lC)
#    | (println LC)
# Do we want to hardcode +, -, ifleq0, and println, or make them lambdas?

_print_wrapper = "def lprintln(string):\n"\
                 "    print(string)\n"\
                 "    return 0\n"

_header = "import sys\n"

_footer = "if __name__ == \"__main__\":\n"\
          "    sys.exit(main())\n"

def translate(sexp, fun_defs):
    if isinstance(sexp, Symbol):
        pass
    elif isinstance(sexp, list):
        if len(sexp) == 2 and sexp[0] == Symbol("println"):
            return "lprintln(%s)" % translate(sexp[1], fun_defs) 
        elif len(sexp) == 3 and (sexp[0] == Symbol("+")\
                              or sexp[0] == Symbol("*")):
            return "(%s %s %s)" % (translate(sexp[1], fun_defs),\
                                   sexp[0].value(),\
                                   translate(sexp[2], fun_defs))
        elif len(sexp) == 4 and sexp[0] == Symbol("ifleq0"):
            return "(%s if %s <= 0 else %s)" % (translate(sexp[2], fun_defs),\
                                                translate(sexp[1], fun_defs),\
                                                translate(sexp[3], fun_defs))
    elif isinstance(sexp, int) or isinstance(sexp, float):
        return str(sexp)
    else:
        raise Exception("%r is not a well-formed expression." % sexp) 

def main():
    global _print_wrapper
    global _header
    global _footer

    fun_defs = [_print_wrapper]

    if len(sys.argv) != 2:
        print("Usage: python3 translate.py <file>", file = sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r") as lamc_src,\
         open("%s.py" % ".".join(sys.argv[1].split(".")[:-1]), "w") as py_out:
        py_out.write("%s\n" % _header)

        py_out.write("def main():\n    return %s\n\n"\
                     % translate(parse(lamc_src.read().strip()), fun_defs))

        for fun_def in fun_defs:
            py_out.write("%s\n" % fun_def)

        py_out.write(_footer)

if __name__ == "__main__":
    main()
