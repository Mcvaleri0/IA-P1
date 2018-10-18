"""
 ----- Grupo 48 -----
    
Joao Martinho  Nº 86454
Miguel Valerio Nº 86483 """



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

def board_moves(board):
    """ Argumento: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: movimentos
            movimentos -> Lista com todos os movimentos possiveis do tabuleiro. """
    
    for l in range(len(board)):
        for c in range(len(board[l])):
            pos = make_pos(l,c)

""" ======================================================================= """
