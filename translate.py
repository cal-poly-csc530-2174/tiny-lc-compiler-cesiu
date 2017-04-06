# Lambda Calculus -> Python Translator
# CPE 530, Spring '17
# Andrew Tran and Christopher Siu

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
    pass

if __name__ == "__main__":
    main()
