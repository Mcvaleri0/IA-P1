"""
 ----- Grupo 48 -----
    
Joao Martinho  N 86454
Miguel Valerio N 86483 """



import math



""" ============================ Tipo content ============================ """

def c_peg():
    """ Retorna o simbolo representante de uma posicao ocupada. """
    return "O"


def c_empty():
    """ Retorna o simbolo representante de uma posicao vazia. """
    return "_"


def c_blocked():
    """ Retorna o simbolo representante de uma posicao bloqueada. """
    return "X"


def is_empty(e):
    """ Argumento: e
            e -> Conteudo de uma posicao.
        Retorno:
            True  -> Se e representar uma posicao vazia.
            False -> Caso contrario. """
    return e == c_empty()


def is_peg(e):
    """ Argumento: e
            e -> Conteudo de uma posicao.
        Retorno:
            True  -> Se e representar uma posicao ocupada.
            False -> Caso contrario. """
    return e == c_peg()


def is_blocked(e):
    """ Argumento: e
            e -> Conteudo de uma posicao.
        Retorno:
            True  -> Se e representar uma posicao bloqueada.
            False -> Caso contrario. """
    return e == c_blocked()

""" ======================================================================= """



""" ============================== Tipo pos ============================== """

def make_pos(l, c):
    """ Argumento: l, c
            l -> Inteiro.
            c -> Inteiro.
        Retorno: (l, c)
            (l, c) -> Posicao no tabuleiro.
                l  -> Numero da linha.
                c  -> Numero da coluna. """
    return (l, c)


def pos_l(pos):
    """ Argumento: pos
            pos -> Posicao no tabuleiro.
        Retorno: l
            l -> Numero da linha. """
    return pos[0]


def pos_c(pos):
    """ Argumentos: pos
            pos -> Posicao no tabuleiro.
        Retorno: c
            c -> Numero da coluna. """
    return pos[1]


def pos_get_side(pos, side):
    """ Argumentos: pos, side
            pos  -> Posicao no tabuleiro.
            side -> Direcao da posicao vizinha
                    (0=>cima; 1=>direita; 2=>baixo; 3=>esquerda).
        Retorno: pos_side
            pos_side -> Posicao vizinha da posicao dada segundo a direcao dada. """
    if side == 0:
        return make_pos(pos_l(pos)-1, pos_c(pos))
    elif side == 1:
        return make_pos(pos_l(pos), pos_c(pos)+1)
    elif side ==2:
        return make_pos(pos_l(pos)-1, pos_c(pos))
    elif side == 3:
        return make_pos(pos_l(pos), pos_c(pos)-1)
""" ======================================================================= """



""" ============================== Tipo move ============================== """

def make_move(i, f):
    """ Argumentos: i, f
            i -> Posicao.
            f -> Posicao.
        Retorno: [i, f]
            [i, f] -> Jogada no jogo Solitaire.
                i  -> Posicao inicial.
                f  -> Posicao final. """
    return [i, f]


def move_initial(move):
    """ Argumento: move
            move -> Jogada no jogo Solitaire.
        Retorno: p_initial
            p_initial -> Posicao incial. """
    return move[0]


def move_final(move):
    """ Argumento: move
            move -> Jogada no jogo Solitaire.
        Retorno: p_final
            p_final -> Posicao final. """
    return move[1]

""" ======================================================================= """



""" ============================= Tipo board ============================= """

def board_set_pos(board, posit, content):
    """ Argumentos: board, posit, content
            board   -> Representa o tabuleiro de um jogo de Solitaire.
            posit   -> Posicao.
            content -> Conteudo a colocar na posicao."""
    board[pos_l(posit)][pos_c(posit)] = content
    
    
def board_get_content(board, posit):
    """ Argumentos: board, posit
            board   -> Representa o tabuleiro de um jogo de Solitaire.
            posit   -> Posicao.
        Retorno: cont
            cont -> Conteudo da posicao no tabuleiro de jogo dados como argumentos. """
    if is_pos_valid(board, posit):
        return board[pos_l(posit)][pos_c(posit)]
    return c_blocked()  # pos invalida ==> content(pos) = c_blocked()


def board_get_NLines(board):
    """ Argumentos: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: nLines
            nLines -> Numero de linhas do tabuleiro. """
    return len(board)


def board_get_NCollumns(board):
    """ Argumentos: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: nCollumns
            nCollumns -> Numero de colunas do tabuleiro. """
    return len(board[0])


def is_pos_valid(board, pos):
    """ Argumentos: board, pos
            board -> Representa o tabuleiro de um jogo de Solitaire.
            pos   -> Posicao.
        Retorno: True ou False
            True  -> Se pos dentro dos limites do tabuleiro.
            False -> Caso Contrario. """
    l = pos_l(pos)
    c = pos_c(pos)
    if (l >= 0 and l < board_get_NLines(board) and
        c >= 0 and c < board_get_NCollumns(board)):
        return True
    return False


def board_moves(board):
    """ Argumento: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: movs
            movs -> Lista com todos os movimentos possiveis do tabuleiro. """
    movs = []
    for l in range(board_get_NLines(board)):
        for c in range(board_get_NCollumns(board)):
            pos  = make_pos(l, c)
            cont = board_get_content(board, pos)
            if is_peg(cont):
                for i in range(4):
                    pos_side  = pos_get_side(pos, i)
                    pos_final = pos_get_side(pos_side, i)
                    print("pos_side: " + str(pos_side))
                    print("pos_final: " + str(pos_final))
                    
                    if (is_peg(board_get_content(board, pos_side)) and
                        is_empty(board_get_content(board, pos_final))):
                        movs += [make_move(pos, pos_final)]
                        
    return movs


def board_perform_move(board, move):
    """ Argumentos: board, move
            board -> Representa o tabuleiro de um jogo de Solitaire.
            move  -> Jogada no jogo Solitaire.
        Retorno: resultado
            result -> tabuleiro resultante de aplicar o move ao board."""
    first = move_initial(move)
    last  = move_final(move)
    midL  = int(math.fabs(pos_l(first)-pos_l(last))//2)
    midC  = int(math.fabs(pos_c(first)-pos_c(last))//2)

    mid = make_pos(midL,midC)

    result = []
    for line in board:
        result += [line.copy()]
    
    board_set_pos(result, first, c_empty())
    board_set_pos(result,  last,   c_peg())
    board_set_pos(result,   mid, c_empty())

    return result

""" ======================================================================= """

