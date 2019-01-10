empty_board={11:" ",12:' ',13:' ',21:' ',22:' ',23:' ',31:' ',32:' ',33:' '}


def print_borad():
	print(empty_board.get(11,'')+'|'+empty_board.get(12,'')+'|'+empty_board.get(13,''))
	print('-+-+-')
	print(empty_board.get(21,'')+'|'+empty_board.get(22,'')+'|'+empty_board.get(23,''))
	print('-+-+-')
	print(empty_board.get(31,'')+'|'+empty_board.get(32,'')+'|'+empty_board.get(33,''))
	print('-+-+-')

def winning(status):
		if (theBoard.get(11,'') != ' ' and (theBoard.get(11,'') == theBoard.get(12,'') and theBoard.get(11,'') == theBoard.get(13,'')) or 
		(theBoard.get(21,'') != ' ' and theBoard.get(21,'') == theBoard.get(22,'') and theBoard.get(21,'') == theBoard.get(23,'')) or 
		(theBoard.get(31,'') != ' ' and theBoard.get(31,'') == theBoard.get(32,'') and theBoard.get(31,'') == theBoard.get(33,'')) or 
		(theBoard.get(11,'') != ' ' and theBoard.get(11,'') == theBoard.get(21,'') and theBoard.get(11,'') == theBoard.get(31,'')) or 
		(theBoard.get(12,'') != ' ' and theBoard.get(12,'') == theBoard.get(22,'') and theBoard.get(12,'') == theBoard.get(32,'')) or 
		(theBoard.get(13,'') != ' ' and  theBoard.get(13,'') == theBoard.get(23,'') and theBoard.get(13,'') == theBoard.get(33,''))) :
			print (str(turn)+ " WON THE GAME ")
			return 1
		
		
turn = 'X'
move=''

for i in range(9):
	print_board()		
	
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	empty_board[move] = turn
	
	won=0
	won=winning(won)
	if won==1:
		#won=0
		break
		
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
