import os
import sys
from core.lexer import Lexer


def usage(error: str|None) -> str|None:
    [print(f'ERROR: {error}') if error != None else None]
    print('USAGE:\n\t* simplex <filename>     -     Run the file')

    
if __name__ == '__main__':
    os.system('cls')
    os.chdir(os.getcwd() + r'\core')
    match len(sys.argv):
        case 2:
            Lexer(sys.argv[1]).read_file()
        case _:
            usage('you have to provide an argument (filename)')
