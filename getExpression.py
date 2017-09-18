def obtainGrid(m,n):
	answer = []
	for i in range(1,m+1):
		for j in range(1,n+1):
			answer.append([i,j])
	return answer

Y_12_12 = obtainGrid(12,12)

def obtainKGrid(k,m,n):
	answer = []
	for i in range(-k,m+k+1):
		for j in range(-k,n+k+1):
			answer.append([i,j])
	return answer	

def findInversePhi(k,m,n):
	answer = []
	p = 2*k*k+2*k+1
	for point in obtainKGrid(k,m,n):
		i = point[0]
		j = point[1]
		q = (k+1)*i+k*j
		if (q % p == 0):
			answer.append([i,j])
	return answer

def findClosestInversePhi(k,m,n):
	answer = []
	for point in findInversePhi(k,m,n):
		x = point[0]
		y = point[1]
		#print(x,y)
		if (x <= 0 and y <= 0):
			answer.append([0,0])
		elif (x <= 0 and 0 <= y and y < n):
			answer.append([0,y])
		elif (x <= 0 and y >= n):
			answer.append([0,n-1])
		elif (0 <= x and x < m and y >= n):
			answer.append([x,n-1])
		elif (x >= m and y >= n):
			answer.append([m-1,n-1])
		elif (x >= m and 0 <= y and y < n):
			answer.append([m-1,y])
		elif (x >= m and y <= 0):
			answer.append([m-1,0])
		elif (0 <= x and x < m and y < 0):
			answer.append([x,0])
		else:
			answer.append([x,y])
	return answer


#This is an example from the paper
k = 3 
m = 6
n = 6

print(findInversePhi(3,6,6))
print(findClosestInversePhi(3,6,6))