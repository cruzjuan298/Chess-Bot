import os
import chess
import chess.engine
import chess.pgn
import pygame 
import random 
'''
incorperate a function that would switch from white to black based on a 50% chance. If the player decided not to play pre set openings

'''
piece_image_mapping = {
    'P': 'wpawn.png',
    'R': 'wrook.png',
    'N': 'wknight.png',
    'B': 'wbishop.png',
    'Q': 'wqueen.png',
    'K': 'wking.png',
    'p': 'bpawn.png',
    'r': 'brook.png',
    'n': 'bknight.png',
    'b': 'bbishop.png',
    'q': 'bqueen.png',
    'k': 'bking.png'
}

sPath = #path to engine
engine = chess.engine.SimpleEngine.popen_uci(sPath)

pgnFile = open(#path to files)

with pgnFile as gameFile:
    games = []
    while True:
        game = chess.pgn.read_game(gameFile)
        if game is None:
            break
        games.append(game)

selectedGame = random.choice(games)
gameMoves = []

for move_num, move in enumerate(selectedGame.mainline_moves()):
    if move_num % 2 == 1:
        gameMoves.append(move)

print(selectedGame)

engine.configure({
    "Skill Level" : 1,
    "UCI_Elo": 1320,
})

whiteOrBlack = random.randrange(0,1)

class Board:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size 
        self.squareSize = size // 8
        self.board = chess.Board()
        self.WhiteToMove = True
        self.openingMoves = 5
        self.moveCounter = 0
        self.xPlane = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.yPlane = [8, 7, 6, 5, 4, 3, 2, 1]
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), self.squareSize // 3)

    def loadPieces(self):
        piecesImages = {} 
        images = os.path.join(os.path.dirname(__file__), 'pieces')

        for symbol, image in piece_image_mapping.items(): 
            piecesImages[symbol] = pygame.transform.scale(pygame.image.load(os.path.join(images, image)), (self.squareSize, self.squareSize))
        return piecesImages

    def drawBoard(self):
        color1, color2 = (238, 238, 210) , (118, 150, 86)
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, color1, (i *   self.squareSize, j * self.squareSize ,self.squareSize, self.squareSize))
                else:
                    pygame.draw.rect(screen, color2, (i *   self.squareSize, j * self.squareSize,   self.squareSize,  self.squareSize))
                fontImg = self.font.render(f"{self.xPlane[i]}{self.yPlane[j]}", True, (0, 0, 0))
                self.screen.blit(fontImg, (i * self.squareSize, j * self.squareSize) )

    def drawPieces(self, piecesImages):
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                pieceSymbol = piece.symbol()
                self.screen.blit(piecesImages[pieceSymbol], (chess.square_file(square) * self.squareSize, (7 - chess.square_rank(square)) * self.squareSize))

    def draw(self):
        self.drawBoard()
        self.drawPieces(self.loadPieces())

    def update(self, toSquare:tuple, fromSquare:tuple):
        move = chess.Move(chess.square(fromSquare[0], 7 - fromSquare[1]),chess.square(toSquare[0], 7 - toSquare[1]))
        if move in self.board.legal_moves:
            self.board.push(move)
            self.draw()
            self.WhiteToMove = False

    def engineMove(self):
        if self.moveCounter < self.openingMoves:
            self.board.push(gameMoves[self.moveCounter])
            self.moveCounter += 1
            print(f"{self.moveCounter}: {gameMoves[self.moveCounter - 1]}")
            self.draw()
        else:
            result = engine.play(self.board, chess.engine.Limit(time=0.1, depth=5))
            self.board.push(result.move)
            print(f"{result.move}")
            self.draw()

pygame.init()
screenWidth, screenHeight = 640, 640
screen = pygame.display.set_mode((screenWidth, screenHeight))
board = Board(screen, screenHeight)

activePieceX, activePieceY = None, None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if board.WhiteToMove == True:
                    pieceX, pieceY = event.pos
                    activePieceX, activePieceY = pieceX // board.squareSize, pieceY // board.squareSize

        if event.type == pygame.MOUSEBUTTONUP:
            if board.WhiteToMove == True:
                if event.button == 1:
                    newX, newY = event.pos
                    board.update((newX // board.squareSize, newY // board.squareSize),(activePieceX, activePieceY))
                    activePieceX, activePieceY = None, None

        if board.WhiteToMove == False:
            board.engineMove()
            board.WhiteToMove = True 

        if board.board.is_game_over():
            engine.quit()

    board.draw()
    pygame.display.flip()