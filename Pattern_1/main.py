n = int(input("Enter the number of stars:"))
count = 0

skipped_stars = []


def make_stars(n):
    count = 0
    for i in range(n):
        print('*',end="")
        count += 1
        for j in range(n-2):
            if count in skipped_stars:
                print(' ',end="")
            else: 
                print('*',end="")
            
        print('*')
    

for i in range (2,n+1):
    if i == n:
        continue
    else:
        skipped_stars.append(i)
    
make_stars(n)


    