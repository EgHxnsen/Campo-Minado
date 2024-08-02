import random

MAX_COL = 8
MAX_LIN = 3

# Global Variables
campo = [['' for _ in range(MAX_COL)] for _ in range(MAX_LIN)]
bombs = [['' for _ in range(MAX_COL)] for _ in range(MAX_LIN)]
Result = 'Jogando'

def start_campo():
    global campo, bombs
    random.seed()
    for l in range(MAX_LIN):
        for c in range(MAX_COL):
            campo[l][c] = ' '
            bombs[l][c] = ' '
            v = random.randint(1, 3)
            if v > 2:
                bombs[l][c] = 'X'

def print_Border(ultimo):
    print('+', end='')
    for _ in range(MAX_COL):
        print('---+', end='')
    print()
    if not ultimo:
        print('|', end='')

def imprimir_campo():
    print("\033[H\033[J")
    for l in range(MAX_LIN):
        print_Border(False)
        for c in range(MAX_COL):
            print(f' {campo[l][c]} |', end='')
        print(l + 1)
    print_Border(True)

def valida_Resultado():
    for l in range(MAX_LIN):
        for c in range(MAX_COL):
            if campo[l][c] == ' ' and bombs[l][c] == 'X':
                return 'Jogando'
    return 'Ganhou'

def main() -> object:
    global Result
    start_campo()
    while Result == 'Jogando':
        imprimir_campo()
        print('Onde deseja jogar?')

        line = 0
        while line < 1 or line > MAX_LIN:
            line = int(input('Informe a linha: '))
            if line < 1 or line > MAX_LIN:
                print('Linha inválida!')

        columns = 0
        while columns < 1 or columns > MAX_COL:
            columns = int(input('Informe a coluna: '))
            if columns < 1 or columns > MAX_COL:
                print('Coluna inválida!')

        line -= 1  # ajusta para índice 0
        columns -= 1  # ajusta para índice 0

        if bombs[line][columns] == 'X':
            campo[line][columns] = 'B'
            Result = 'Perdeu, acertou uma mina!'
        else:
            campo[line][columns] = 'O'
            Result = valida_Resultado()

        imprimir_campo()
        print(Result)

if __name__ == '__main__':
    main()
