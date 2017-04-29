import numpy as np


#input array
board = np.array([[0,1,1,1,0],[1,1,1,0,1],[1,1,0,1,0],[1,0,1,0,1],[1,1,1,1,0]])

A = board.transpose()

global max_coin_vals
#initialize max_coin_value array
max_coin_vals = np.array([[0]*5 for _ in range(5)])



def robot_coin_collect(A,max_coin_vals,i=0,j=0,c=0):
	
	max_coin_vals[i][j]=c				#update max_coin_val at that index
	
	#base case
	if i==len(A)-1 and j == len(A)-1:
		print "----------------------------\nMax value is:", max_coin_vals[i][j]
	
	if j < len(A)-1:	#keep within bounds of board
		if A[i][j+1] == 1 and (max_coin_vals[i][j]+1) > max_coin_vals[i][j+1]:	#if box on right has coin and would have new max, update
			robot_coin_collect(A,max_coin_vals,i,j+1,max_coin_vals[i][j]+1)
		elif A[i][j+1]==0 and max_coin_vals[i][j] > max_coin_vals[i][j+1]:	#else, move right and update value if new max
			robot_coin_collect(A,max_coin_vals,i,j+1,max_coin_vals[i][j])
	if i < len(A)-1:
		if A[i+1][j] == 1 and (max_coin_vals[i][j]+1) > max_coin_vals[i+1][j]:
			robot_coin_collect(A,max_coin_vals,i+1,j,max_coin_vals[i][j]+1)
		elif A[i+1][j]==0 and max_coin_vals[i][j] > max_coin_vals[i+1][j]:
			robot_coin_collect(A,max_coin_vals,i+1,j,max_coin_vals[i][j])


robot_coin_collect(A,max_coin_vals)	#run program


#print matrix
print "-----------Output-------------"
max_coin_vals = max_coin_vals.transpose()

for row in max_coin_vals:
	print row

