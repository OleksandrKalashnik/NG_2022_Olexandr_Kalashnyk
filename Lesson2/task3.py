chislo = int(input("Введите число: "))
userTreeSize = chislo
Nomerchislo = 0
def Writer (treeSize, strNumber):
    treeSize -= strNumber
    while treeSize > 0:
        print(treeSize, end=" ")
        if treeSize == 1:
            strNumber += 1
            print("\n", end="")
            return strNumber
        treeSize -= 1
while Nomerchislo != userTreeSize:
   Nomerchislo = Writer(chislo, Nomerchislo)