"""
 ----- Grupo 48 -----
    
Joao Martinho  N 86454
Miguel Valerio N 86483 """



from search import *



""" ============================= Tipo content ============================= """

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

""" ======================================================================== """



""" =============================== Tipo pos =============================== """

def make_pos(l, c):
    """ Argumento: l, c
            l -> Inteiro.
            c -> Inteiro.
        Retorno: (l, c)
            (l, c) -> Posicao no tabuleiro.
                l  -> Numero da linha.
                c  -> Numero da coluna. """
    return (l,c)


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
        return make_pos(pos_l(pos)+1, pos_c(pos))
    elif side == 3:
        return make_pos(pos_l(pos), pos_c(pos)-1)


def pos_get_opposite_side(pos, side):
    """ Argumentos: pos, side
            pos  -> Posicao no tabuleiro.
            side -> Direcao oposta da posicao vizinha.
                   (0=>cima; 1=>direita; 2=>baixo; 3=>esquerda).
        Retorno: pos_opposite_side
            pos_opposite_side -> Posicao vizinha da posicao dada segundo a
                                 direcao oposta da direcao dada. """
    if side == 0:
        return pos_get_side(pos, 2)
    elif side == 1:
        return pos_get_side(pos, 3)
    elif side == 2:
        return pos_get_side(pos, 0)
    elif side == 3:
        return pos_get_side(pos, 1)


def pos_dif(pos_initial, pos_final):
    """ Argumentos: pos_initial, pos_final
            pos_initial -> Posicao no tabuleiro.
            pos_final   -> Posicao no tabuleiro.
        Retorno: dif
            dif -> Posicao que representa a diferenca entre as posicoes dadas. """
    d_l = pos_l(pos_final) - pos_l(pos_initial)
    d_c = pos_c(pos_final) - pos_c(pos_initial)
    return make_pos(d_l, d_c)

""" ======================================================================== """



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


def move_get_direction(move):
    """ Argumento: move
            move -> Jogada no jogo Solitaire.
        Retorno: dir
            dir -> Direcao da jogada dada.
                   (0=>cima; 1=>direita; 2=>baixo; 3=>esquerda). """

    dif = pos_dif(move_initial(move), move_final(move))

    d_line = pos_l(dif)
    d_column = pos_c(dif)
    if d_line == 0:
        if d_column < 0:
            return 3
        else:
            return 1
    else:
        if d_line < 0:
            return 0
        else:
            return 2


def move_eat(move, pcom):
    """ Argumentos: move, pcom
            move -> Jogada no jogo Solitaire.
            pcom -> Posicao no tabuleiro.
        Retorno: True, False
            True  -> Se o move dado come a peca na posicao dada.
            False -> Caso contrario. """
    moveDir = move_get_direction(move)
    mid = pos_get_side(move_initial(move), moveDir)
    return pos_l(mid) == pos_l(pcom) and pos_c(mid) == pos_c(pcom)

""" ======================================================================== """



""" ============================== Tipo board ============================== """

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


def board_get_Ncolumns(board):
    """ Argumentos: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: Ncolumns
            Ncolumns -> Numero de colunas do tabuleiro. """
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
    if 0 <= l < board_get_NLines(board) and 0 <= c < board_get_Ncolumns(board):
        return True
    return False


def board_moves(board):
    """ Argumento: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: movs
            movs -> Lista com todos os movimentos possiveis do tabuleiro. """
    movs = []
    nLines = board_get_NLines(board)
    Ncolumns = board_get_Ncolumns(board)
    for l in range(nLines):
        for c in range(Ncolumns):
            pos = make_pos(l, c)

            if is_peg(board_get_content(board, pos)):
                movs += board_moves_pos(board, pos)
                """for i in range(4):   -> apenas para ver se a nova funcao funciona bem
                    pos_side = pos_get_side(pos, i)
                    pos_final = pos_get_side(pos_side, i)

                    if is_peg(board_get_content(board, pos_side)) and is_empty(board_get_content(board, pos_final)):
                        movs += [make_move(pos, pos_final)]"""
                        
    return movs


def board_moves_pos(board, pos):
    """ Argumentos: board, pos
            board -> Representa o tabuleiro de um jogo de Solitaire.
            pos   -> Posicao no tabuleiro que contenha uma peca.
        Retorno: movs
            movs -> Lista com os movimentos possiveis da peca dada no
                    tabuleiro dado. """
    movs = []
    for i in range(4):
        pos_side = pos_get_side(pos, i)
        pos_final = pos_get_side(pos_side, i)

        if is_peg(board_get_content(board, pos_side)) and is_empty(board_get_content(board, pos_final)):
            movs += [make_move(pos, pos_final)]

    return movs


def board_perform_move(board, move):
    """ Argumentos: board, move
            board -> Representa o tabuleiro de um jogo de Solitaire.
            move  -> Jogada no jogo Solitaire.
        Retorno: resultado
            result -> tabuleiro resultante de aplicar o move ao board."""
    first = move_initial(move)
    last = move_final(move)

    moveDir = move_get_direction(move)
    mid = pos_get_side(first, moveDir)

    result = []
    for line in board:
        result += [line.copy()]
    
    board_set_pos(result, first, c_empty())
    board_set_pos(result, last, c_peg())
    board_set_pos(result, mid, c_empty())

    return result


def board_get_npeg(board):
    """ Argumento: board
            board -> Representa o tabuleiro de um jogo de Solitaire.
        Retorno: nPeg
            nPeg -> Numero de pecas existentes no tabuleiro dado. """
    npegs = 0
    nLines = board_get_NLines(board)
    nColumns = board_get_Ncolumns(board)
    for l in range(nLines):
        for c in range(nColumns):
            pos = make_pos(l, c)
            cont = board_get_content(board, pos)
            if is_peg(cont):
                npegs += 1
    return npegs

""" ======================================================================== """



""" ============================ Tipo sol_state ============================ """

class sol_state:
    def __init__(self, board, npeg=None, moves=None, nMoves=None):
        self.board = board

        if npeg is None:
            self.npeg = board_get_npeg(self.board)
        else:
            self.npeg = npeg

        if moves is None:
            self.moves = board_moves(board)
            self.nMoves = len(self.moves)
        else:
            self.moves = moves
            self.nMoves = nMoves


    def __lt__(self, other):
        """ Argumentos: self, other
                self  -> Instancia do estado de um jogo de Solitaire.
                other -> Instancia do estado de um jogo de Solitaire.
            Retorno: True, False
                True  -> Se self < other.
                False -> Caso contrario. """
        return self.npeg > other.npeg   # FIXME -> se comecar a dar merda entoa falta comparar os moves

""" ======================================================================= """



""" ============================ Tipo solitaire ============================ """

class solitaire(Problem):
    def __init__(self, board):
        Problem.__init__(self, sol_state(board))

    def actions(self, state):
        """ Argumentos: self, state
                self  -> Representacao de um jogo de Solitaire.
                state -> Representacao do estado de um jogo de Solitaire.
            Retorno: moves
                moves -> Movimentos possiveis do jogo dado estando no estado
                         dado. """
        return state.moves

    def result(self, state, action):
        """ Argumentos: self, state, action
                self   -> Representacao de um jogo de Solitaire.
                state  -> Representacao do estado de um jogo de Solitaire.
                action -> Jogada no jogo Solitaire.
            Retorno: newState
                newState -> Estado resultante de executar a acao dada estando
                            no estado dado. """
        # ----------------------------- Pre-comida -----------------------------
        pos_ini = move_initial(action)

        dir = move_get_direction(action)
        if dir == 0:
            p1 = make_pos(pos_l(pos_ini)-1, pos_c(pos_ini)+1)
            p2 = make_pos(pos_l(pos_ini)-1, pos_c(pos_ini)-1)
        elif dir == 1:
            p1 = make_pos(pos_l(pos_ini)-1, pos_c(pos_ini)+1)
            p2 = make_pos(pos_l(pos_ini)+1, pos_c(pos_ini)+1)
        elif dir == 2:
            p1 = make_pos(pos_l(pos_ini)+1, pos_c(pos_ini)+1)
            p2 = make_pos(pos_l(pos_ini)+1, pos_c(pos_ini)-1)
        else:
            p1 = make_pos(pos_l(pos_ini)-1, pos_c(pos_ini)-1)
            p2 = make_pos(pos_l(pos_ini)+1, pos_c(pos_ini)-1)

        # posicao comida
        pcom = pos_get_side(pos_ini, dir)

        # moves que comem o que comi
        mv1 = make_move(p1, p2)
        mv2 = make_move(p2, p1)

        moves = []
        nMoves = 0
        for m in state.moves:
            if move_initial(m) != pos_ini and not move_eat(m, pos_ini) and move_initial(m) != pcom and m != mv1 and m != mv2:
                """ move_initial(m) == pos_ini -> moves que podia fazer.
                    move_eat(m, pos_ini) -> moves que me comiam.
                    move_initial(m) == pcom -> moves que a comida podia fazer.
                    mv1 and mv2 -> moves que podiam comer o que comi.
                  |------------------------------------------------------------|
                                                |
                                    esta-se a tirar estes moves. """
                moves += [m.copy()]
                nMoves += 1

        # Faz a acao dada
        newBoard = board_perform_move(state.board, action)

        # ----------------------------- Pos-comida -----------------------------
        pos_fin = move_final(action)

        # moves que posso fazer
        mvs = board_moves_pos(newBoard, pos_fin)
        moves += mvs
        nMoves += len(mvs)

        # moves que me podem comer
        for i in range(4):
            pos_side = pos_get_side(pos_fin, i)
            pos_side_final = pos_get_opposite_side(pos_fin, i)

            if is_peg(board_get_content(newBoard, pos_side)) and is_empty(board_get_content(newBoard, pos_side_final)):
                moves += [make_move(pos_side, pos_side_final)]
                nMoves += 1

        return sol_state(newBoard, state.npeg-1, moves, nMoves)

    def goal_test(self, state):
        """ Argumentos: self, state
                self  -> Representacao de um jogo de Solitaire.
                state -> Representacao do estado de um jogo de Solitaire.
            Retorno: True, False
                True  -> Se o estado dado for o estado objetivo do jogo dado.
                False -> Caso contratio. """
        return state.npeg == 1

    def h(self, node):  # FIXME -> precisa de melhoras
        """ Argumentos: self, node
                self -> Representacao de um jogo de Solitaire.
                node -> Representacao de um no das arvores de procura.
            Retorno: h(node)
                h(node) -> Valor atribuido pela funcao heuristica ao no dado. """
        return node.state.npeg

""" ======================================================================= """
