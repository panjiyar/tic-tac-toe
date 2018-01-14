vals = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def printgrid(grid):
	temp_grid = grid[:]
	temp_grid.insert(0, [])
	temp_grid[0] =['Col 1', 'Col 2', 'Col 3']
	temp_grid[0] = '\t' + '\t\t'.join(temp_grid[0])
	for i in range(1,4):
		temp_grid[i] = '\t\t'.join(temp_grid[i])
		temp_grid[i] = 'Row {}\t'.format(i) + temp_grid[i]
	for i in temp_grid:
		print i


def getNum(isItRow):
	row = 0 
	while True:
		key_word = "row" if isItRow else "col"
		row = raw_input("Please provide a valid {} (1-3):".format(key_word.upper()))
		try:
			row = int(row)
		except Exception, e:
			continue
		if row > 3 or row <= 0:
			continue
		return row


def player(grid, x='True'):
	while True:
		row = getNum(True)
		col = getNum(False)
		if grid[row-1][col-1] == '.':
			grid[row-1][col-1] = 'x' if x else 'o'
			return
		else:
			continue


def comp(grid):
	if grid[1][1] == '.':
		grid[1][1] = 'o'
		return

	#check if o can complete a 3 liner and finish the game if possible
	newgrid = grid[0]+grid[1]+grid[2]
	for i in vals:
		if newgrid[i[0]] == 'o' and newgrid[i[1]] == 'o' and newgrid[i[2]] == '.':
			grid[i[2]/3][i[2]%3] = 'o'
			return
		if newgrid[i[1]] == 'o' and newgrid[i[2]] == 'o' and newgrid[i[0]] == '.':
			grid[i[0]/3][i[0]%3] = 'o'
			return
		if newgrid[i[2]] == 'o' and newgrid[i[0]] == 'o' and newgrid[i[1]] == '.':
			grid[i[1]/3][i[1]%3] = 'o'
			return

	for i in vals:
		if newgrid[i[0]] == 'x' and newgrid[i[1]] == 'x' and newgrid[i[2]] == '.':
			grid[i[2]/3][i[2]%3] = 'o'
			return
		if newgrid[i[1]] == 'x' and newgrid[i[2]] == 'x' and newgrid[i[0]] == '.':
			grid[i[0]/3][i[0]%3] = 'o'
			return
		if newgrid[i[2]] == 'x' and newgrid[i[0]] == 'x' and newgrid[i[1]] == '.':
			grid[i[1]/3][i[1]%3] = 'o'
			return
		

	#check if x is completing a 3 liner
	#if it is, block it

	#if it is not, make a move
	# TODO : Make a "genius" move
	for i in range(0,9):
		if newgrid[i] == '.':
			print i
			grid[i/3][i%3] = 'o'
			return


def rowCheck(newgrid, val):
	if (newgrid[val[0]] != '.') and (newgrid[val[0]] == newgrid[val[1]]) and (newgrid[val[0]] == newgrid[val[2]]):
		return True
	return False


def checkForWinner(grid):
	newgrid = grid[0]+grid[1]+grid[2]
	for i in vals:
		if rowCheck(newgrid, i):
			return newgrid[i[0]]
	return None


def TwoPlayerMain():
	grid = [['.','.','.'],['.','.','.'],['.','.','.']]
	sign = True
	count = 0
	while True:
		printgrid(grid)
		player(grid, sign)
		win = checkForWinner(grid)
		if win:
			printgrid(grid)
			print win + ' WINS'
			break
		sign = not sign
		count += 1
		if count == 9:
			printgrid(grid)
			print "This is a DRAW"
			break


def OnePlayerMain():
	grid = [['.','.','.'],['.','.','.'],['.','.','.']]
	count = 0
	while  True:
		printgrid(grid)
		player(grid)
		if checkForWinner(grid):
			printgrid(grid)
			print 'PLAYER WINS'
			break
		count += 1
		if count == 9:
			printgrid(grid)
			print "This is a DRAW"
			break
		printgrid(grid)
		print "Computer's move :"
		comp(grid)
		if checkForWinner(grid):
			printgrid(grid)
			print 'COMPUTER WINS'
			break
		count += 1


def main():
	print "Choose one option: "
	print "1. Player vs Computer"
	print "2. Player vs Player"
	option = raw_input('')
	if option == '1':
		OnePlayerMain()
	elif option == '2':
		TwoPlayerMain()


if __name__ == '__main__':
	main()