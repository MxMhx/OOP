n = 10

for row in range(n,0,-1):
    print(str(' ')*int(row),end='')
    print(str('#')*int(n-(row-1)))