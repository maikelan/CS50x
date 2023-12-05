
def get_change():
    while True:
        x=float(input("Change: "))
        if x>0:
            break
        else :print ("请输入一个大于0的数字")
    return x

def calculate(change):
    x=change*100
    i=0
    i+=(x//25)
    a=x%25
    i+=(a//10)
    a=a%10
    i+=(x//5)
    a=a%5
    i+=a
    return i

def main():
    change=get_change()
    print("{calculate(change)}")
main()




