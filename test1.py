def print_rangoli(size):
    n=97+size
    a=""
    for i in range(n-1,96,-1):
        for j in range(n-1,i-1,-1):
            a=a+chr(j)
            if j>i:
                a=a+"-"
        for k in range(j+1,n):
            a=a+"-"+chr(k)
        print(a.center((size+(size-1)*3),"-"))
        a=""   
    for i in range(98,97+size):
        for j in range(n-1,i-1,-1):
            a=a+chr(j)
            if j>i:
                a=a+"-"
        for k in range(j+1,n):
            a=a+"-"+chr(k)
        print(a.center((size+(size-1)*3),"-"))
        a=""
#main control
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
