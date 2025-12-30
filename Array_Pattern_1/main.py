grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]

# To see the matrix
for  i in grid:
    print(i)
print()

top , bottom = 0 , len(grid) - 1
left , right = 0 , len(grid[0]) - 1


while top<=bottom and left <= right:
    
    for i in range(left,right+1):
        print(grid[top][i],end=" -> ")
    top+= 1
    
    for j in range(top,bottom+1):
        print(grid[j][right],end=" -> ")
    right-=1
    
    if top <= bottom:
        for k in range(right,left-1,-1):
            print(grid[bottom][k],end=" -> ")
        bottom-=1
        
    if left <= right:
        for l in range(bottom,top-1,-1):
            print(grid[l][left],end=" -> ")
        left += 1
        
print('end')