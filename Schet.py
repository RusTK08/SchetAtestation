# str5 = "sdjhfkj kjdskf fjbsdi iueraskjh"
# print(str5.upper()) #SDJHFKJ KJDSKF FJBSDI IUERASKJH
# print(str5.capitalize()) #Sdjhfkj kjdskf fjbsdi iueraskjh ПЕРВУЮ БУКВУ ПЕРВОГО СЛОВА
# print(str5.title()) #Sdjhfkj Kjdskf Fjbsdi Iueraskjh

def schet1():
    arrayset = set()
    data = open("input.txt", "r", encoding="utf-8")
    for line in data:
        for i in line.split():
            arrayset.add(i.title())
    data.close()
    print(arrayset)
    return arrayset
schet1()

#ВНИМАНИЕ НЕ СЧИТАЮ ПРИЛАГАТЕЛЬНЫЕ КАК ФРУКТЫ-ОВОЩИ!!!

def schet2():
    array = []
    data1 = open("input.txt", "r", encoding="utf-8")
    for line in data1:
        for i in line.split():
            array.append(i.title())
    data1.close()
    return array
def schet3():
    print("Длина: ", end="")
    print(len(schet2()))
schet3()
def schet4():
    max = 0
    inel = 0
    array2 = schet2()
    for i in array2:
        if(len(i) > max):
            max = len(i)
            inel = array2.index(i)
        #print(max, inel)
    print("Первое по величине слово: ", end="")
    print(array2[inel])
    print("Второе по величине слово: ", end="")
    print(array2[387])
schet4()
def controlfilter():
    array3 = set(schet2())
    print(array3)
    print("------------------------------")
    array4 = []
    for i in array3:
        if("ай" not in i):
            if("ый" not in i):
                if("ой" not in i):
                    if("ая" not in i):
                        if("ны" not in i):
                            if("бы" not in i):
                                array4.append(i)
    print(array4)
    print("----------------------")
    array5 = []
    for i in array3:
        if(i not in array4):
            array5.append(i)
    print("Разница: ", end="")
    print(array5)
    print("---------------------------")
controlfilter()
def podschet(arg1, arg2):
    count = 0
    for i in arg2:
        if(i == arg1):
            count += 1
    return count
def sverka():
    array6 = schet1()
    array8 = schet2()
    array8.sort()
    #print(array8)
    array7 = []
    #sum = 0
    for i in array6:
        array7.append(podschet(i, array8))
        array7.append(i)
        #sum = sum + podschet(i, array8)
    print(array7)
    #print(sum)
sverka()


