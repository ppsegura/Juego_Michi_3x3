from random import randrange

def display_board(board):
    #Dibujo el tablero actual
    print("+-------"*3,"+",sep="")
    for fila in board:        
        print("|       "*3,"|",sep="")
        print("|   ",end="")
        for valor in fila:
            print(valor, "  |",end="   ")
        print()
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")


def enter_move(board):
    #Ingresamos nuestro movimiento con un número válido
    while True:
        movimiento = int(input("Ingresa tu movimiento: "))-1 #La lista son posiciones del 0 al 8, por ende se resta 1, ya que ingresamos números del 1 al 9
        fila, columna = movimiento // 3, movimiento % 3 #Con este algoritmo obtenemos la fila y columna del número ingresado entre el 1 al 9
        #Si el número ingresado es correcto, agregamos O al valor del 1 al 9
        if 3 > fila >= 0 and 3 > columna >= 0 and board[fila][columna] != "X" and board[fila][columna] != "O":
            board[fila][columna]="O"
            break
        else:
            print("Ingresa un número válido")
            continue

def make_list_of_free_fields(board):
    #Creamos una lista formada por tuplas [(x,x),(y,y),...] con las posiciones vacías
    libres=[]
    for fila in range(3):
        for columna in range(3):
            if board[fila][columna] != "X" and board[fila][columna] != "O":
                libres.append((fila,columna)) #Agregamos la fila y columna vacía a la nueva lista
    return libres #retornamos la lista con las posiciones del 1 al 9 que no tienen X o O      


def victory_for(board, sign):
    if sign == "X":
        jugador = "maquina"
    elif sign == "O":
        jugador = "persona"
    else:
        return None
    
    cruce1 = cruce2 = True

    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return jugador
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return jugador
        if board[i][i] != sign: # Si un elemento en la diagonal principal no es igual a 'X' o 'O', se establece como 'False'
            cruce1 = False
        if board[2-i][2-i] != sign: # Si un elemento en la diagonal secundaria no es igual a 'X' o 'O', se establece como 'False'
            cruce2 = False
    if cruce2 or cruce1:
        return jugador
    
    return None

def draw_move(board):
    #almaceno la lista vacía en una variable
    free = make_list_of_free_fields(board)
    contador = len(free)
    #creo un contador de la cantidad de elemtnso vacíos
    if contador > 0:
        this = randrange(contador) # Almaceno en this un número entero random
        fila, columna = free[this] # Accedo mediante el indice this a una tupla de free[(x,x),(y,y),...)] y la almaceno en fila y columna
        board[fila][columna] = "X"

def main():
    # 3 * j * i + 1 = es igual al valor que tendra cada celda, i son las columnas, j las filas, primero se ejecuta j
    board = [[3 * j + i + 1 for i in range(3)]for j in range(3)]
    board[1][1]="X"
    while True:
        display_board(board)
        enter_move(board)

        if victory_for(board,"O"):
            display_board(board)
            print("Has ganado!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("Has empatado!")
            break
        
        draw_move(board)
        if victory_for(board,"X"):
            display_board(board)
            print("Has perdido!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("Has empatado!")
            break

if __name__ == "__main__":
    main()