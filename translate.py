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

# Translates an S-expression into Python.
# sexp - An S-expression
# fun_defs - A list of lambda (function) definitions
# Returns a string of Python code.
def translate(sexp):
    # If it's a symbol, convert it to a string.
    if isinstance(sexp, Symbol):
        return sexp.value()
    elif isinstance(sexp, list):
        # If it's a println, replace it with our custom print.
        if len(sexp) == 2 and sexp[0] == Symbol("println"):
            return "lprintln(%s)" % translate(sexp[1])
        # If it's a binop...
        elif len(sexp) == 3 and (sexp[0] == Symbol("+")\
                              or sexp[0] == Symbol("*")):
            return "(%s %s %s)" % (translate(sexp[1]),\
                                   sexp[0].value(),\
                                   translate(sexp[2]))
        # If it's an ifleq0, convert it to a ternary expression.
        elif len(sexp) == 4 and sexp[0] == Symbol("ifleq0"):
            return "(%s if %s <= 0 else %s)" % (translate(sexp[2]),\
                                                translate(sexp[1]),\
                                                translate(sexp[3]))
        # If it's a lambda, add it to the list of def'ns and return the name.
        elif len(sexp) == 3 and sexp[0] == Symbol("λ"):
            return "(lambda %s : (%s))" % \
                (sexp[1][0].value(), translate(sexp[2]))

        # If it's an application...
        elif len(sexp) == 2:
            return "(%s(%s))" % (translate(sexp[0]),\
                               translate(sexp[1]))
        # Otherwise raise an exception.
        else:
            raise Exception("%r is not a well-formed expression." % sexp) 
    # If it's a number, convert it to a string.
    elif isinstance(sexp, int) or isinstance(sexp, float):
        return str(sexp)
    # Otherwise raise an exception.
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
                     % translate(parse(lamc_src.read().strip())))

        for fun_def in fun_defs:
            py_out.write("%s\n" % fun_def)

        py_out.write(_footer)

if __name__ == "__main__":
    main()
