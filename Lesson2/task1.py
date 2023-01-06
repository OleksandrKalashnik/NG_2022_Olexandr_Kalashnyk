stroka = str(input("Введите строку:"))
stroka = stroka.lower()
kolihestvo = {}
for i in  stroka: 
    kolihestvo [i] = stroka.count(i)    
sort = sorted(kolihestvo, key=kolihestvo.get, reverse = True)
for key in sort:
    print(str(key), ": ", str(kolihestvo.get(key)))