  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
    y = '((Ali Akbar Gholami))'
z = y.center(67,'0')
print(z)