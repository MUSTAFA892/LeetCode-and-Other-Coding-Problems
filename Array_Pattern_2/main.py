grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]

m, n = len(grid) , len(grid[0])

k = 4
for i in grid:
    print(i)
print()

count = 0

while k != 1:
    print("Matrix for size:",k)

    for r in range(m-k+1):
        for c in range(n-k+1):
            nums = []
        
            for i in range(r, r + k):
                for j in range(c,c+k):
                    nums.append(grid[i][j])
                    
                print(nums) 
                nums = []
            print() 
            
    k -= 1
        
            
print(count)
