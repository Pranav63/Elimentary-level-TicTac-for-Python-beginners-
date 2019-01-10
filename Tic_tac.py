empty_board={11:" ",12:' ',13:' ',21:' ',22:' ',23:' ',31:' ',32:' ',33:' '}


def print_borad():
	print(empty_board.get(11,'')+'|'+empty_board.get(12,'')+'|'+empty_board.get(13,''))
	print('-+-+-')
	print(empty_board.get(21,'')+'|'+empty_board.get(22,'')+'|'+empty_board.get(23,''))
	print('-+-+-')
	print(empty_board.get(31,'')+'|'+empty_board.get(32,'')+'|'+empty_board.get(33,''))
	print('-+-+-')
	
