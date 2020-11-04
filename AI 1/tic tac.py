import random
board = [' ' for x in range(10)]


def printBoard(board):
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def chooseLetter():
	let = ''
	while not(let=='X' or let=='O'):
		print("Which letter do you wish to choose ?")
		let = input().upper()
	if(let == 'X'):
		return ['X','O']
	else:
		return ['O','X']


def firstTurn():
	if random.randint(0,1)==0:
		return 'computer'
	else:
		return 'player'


def isFreeSpace(board,move):
        if board[move]==' ':
                return True
        else:
                return False


def isBoardFull(board):
        """for i in range(1,10):
                if isFreeSpace(board,i):
                        return False
                return True"""
        
        if board.count(' ') > 1:
                return False
        else:
                return True


def isWinner(board,letter):
        return ((board[7]==letter and board[8]==letter and board[9]==letter)or(board[4]==letter and board[5]==letter and board[6]==letter)or(board[1]==letter and board[2]==letter and board[3]==letter)or(board[7]==letter and board[4]==letter and board[1]==letter)or(board[8]==letter and board[5]==letter and board[2]==letter)or(board[9]==letter and board[6]==letter and board[3]==letter)or(board[7]==letter and board[5]==letter and board[3]==letter)or(board[1]==letter and board[5]==letter and board[9]==letter))



def insert_letter(board,letter,move):
        board[move]=letter



def selectRandom(board,list_move):
        possibleMoves=[]
        for i in list_move:
                if isFreeSpace(board,i):
                        possibleMoves.append(i)

        if len(possibleMoves)!=0:
                return random.choice(possibleMoves)
        else:
                return None

def getBoardCopy(board):
        dupBoard=[]
        for i in board:
                dupBoard.append(i)

        return dupBoard


def computerMove(board,computer_letter):
        
        if computer_letter == 'X':
                player_letter = 'O'
        else:
                player_letter = 'X'

        for i in range (1,10):
                copy = getBoardCopy(board)
                if isFreeSpace(copy,i):
                        insert_letter(copy,player_letter,i)
                        if isWinner(copy,player_letter):
                                return i
                        
        for i in range (1,10):
                copy = getBoardCopy(board)
                if isFreeSpace(copy,i):
                        insert_letter(copy,computer_letter,i)
                        if isWinner(copy,computer_letter):
                                return i

        move = selectRandom(board,[1,3,7,9])
        if move!= None:
                return move

        if isFreeSpace(board,5):
                return 5

        return selectRandom(board,[2,4,6,8])





def playerMove(board,player_letter):
        run = True
        while run:
                move = input('Select a position to place ' + player_letter + ' (1-9):')
                move = int(move)
                if(move > 0 and move < 10):
                        if isFreeSpace(board,move):
                                run = False
                                insert_letter(board,player_letter,move)
                        else:
                                print('The space is occupied ')
                else:
                        print('Please type a position within the range ')

                        
def main():
        print('Welcome to Tictac Toe')
        player_letter,computer_letter=chooseLetter()
        first_turn = firstTurn()
        print('The ' + first_turn + ' goes first')
	
	
        while not isBoardFull(board):
                if first_turn == 'player':
                        if not(isWinner(board,computer_letter)):
                               playerMove(board,player_letter)
                               printBoard(board)
                               first_turn = 'computer'
                        else:
                                print('Computer won the game')
                                break
                else:
                        if not(isWinner(board,player_letter)):
                               move = computerMove(board,computer_letter)
                               insert_letter(board,computer_letter,move)
                               print('Computer placed ' + computer_letter + ' at positiuon ' + str(move))
                               printBoard(board)
                               first_turn = 'player'

                        else:
                                print('Player wins')
                                break
                if isBoardFull(board):
                       print('Tie game')

main()

while True:
        answer = input('Do u want to play again ? (Y/N)')
        if answer.lower()=='y' or answer.lower()=='yes':
                board = [' ' for x in range(10)]
                print('------------------------')
                main()
        else:
                break
                                        



