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
    #print(arrayset)
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
    print("Количество слов в файле: ", end="")
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
# def controlfilter():
#     array3 = set(schet2())
#     print(array3)
#     print("------------------------------")
#     array4 = []
#     for i in array3:
#         if("ай" not in i):
#             if("ый" not in i):
#                 if("ой" not in i):
#                     if("ая" not in i):
#                         if("ны" not in i):
#                             if("бы" not in i):
#                                 array4.append(i)
#     print(array4)
#     print("----------------------")
#     array5 = []
#     for i in array3:
#         if(i not in array4):
#             array5.append(i)
#     print("Разница: ", end="")
#     print(array5)
#     print("---------------------------")
# controlfilter()
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
        peremenpodschet = podschet(i, array8)
        array7.append(str(peremenpodschet) + " " + i)
        #sum = sum + podschet(i, array8)
    #print(array7)
    array10 = []
    for i5 in array7:
        array10.append(i5)
    for i in range(len(array10)):
        for i9 in array10:
            i11 = i9.split()
            if(i9 != array10[len(array10) - 1]):
                i12 = array10[array10.index(i9) + 1].split()
                if(int(i11[0]) >= int(i12[0])):
                    val1 = array10[array10.index(i9) + 1]
                    array10[array10.index(i9) + 1] = array10[array10.index(i9)]
                    array10[array10.index(i9)] = val1
            elif(i9 == array10[len(array10) - 1]):
                j8 = array10[0].split() 
                if(int(i11[0]) <= int(j8[0])):
                    val3 = array10[array10.index(i9)]
                    array10[array10.index(i9)] = array10[0]
                    array10[0] = val3
    for i in array10:
        print(array10[len(array10) - 1 - array10.index(i)]) #ВМЕСТЕ С ПРИЛАГАТЕЛЬНЫМИ
    #print(sum)
    # ДЕЛАЕМ ПРОВЕРКУ НА ПРИЛАГАТЕЛЬНЫЕ:
    arrayitog = []
    for i14 in array10:
        if("ый" not in i14):
                if("ой" not in i14):
                    if("ая" not in i14):
                        arrayitog.append(i14)
    print("Слева: количсетво повторений, справо: название продукта")
    for i15 in arrayitog:
        print(arrayitog[len(arrayitog) - 1 - arrayitog.index(i15)])
sverka()


