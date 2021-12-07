def printLine(number):
    for n in range(1,number+1):
        print(('  {}  ').format(n),end='')
    print()

def printList(number):
    for number in range(number + 1):
        printLine(number)

number = int(input('Insira um numero : '))
printList(number)     