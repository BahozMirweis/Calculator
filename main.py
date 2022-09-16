from collections import defaultdict
from Calculator import BracketExpression

class CalculatorMainLoop:
    def main(self):
        while True:
            str = input("Enter some bracketed expression involving +, -, *, / (e.g. 3*((1+3)/2) ) and enter q to quit. It won't work if you enter it wrong as I haven't done checks to make sure formatting is correct yet: ")
            print('\n')
            if str == 'q':
                break

            print(f"The answer is: {BracketExpression(str).answer}\n")


CalculatorMainLoop().main()