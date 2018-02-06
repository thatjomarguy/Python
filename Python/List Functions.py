def functionA(list): #Replace Susan and Chet with Ellie Beatrice and Charles
    print("==== Part A ==== Search X replace with Y")
    for v in list:
        i=list.index(v)             #enumerates list for index
        if v=='Susan':
            list.pop(i)             #pop removes the element at index
            list.insert(i,'Ellie')  #insert(index, element)
        if v=='Chet':
            list.pop(i)
            list.insert(i,"Charles")
            list.insert(i,"Beatrice")

    print(list,"\n")

def functionB(list): #remove bill from array
    print("==== Part B ==== Remove x")
    for v in list:
        i=list.index(v)
        if v=='Bill':
            list.pop(i)             #pop removes the element at index

    print(list,"\n")

def functionC(list): #add lewis and izzy to the end of the array
    print("==== Part C ==== Add to list")
    insert = ['Lewis','Izzy']
    list.extend(insert)             #extend adds to end of list

    print(list,"\n")

def functionD(list): #Remove nick (or remove the first index)
    print("==== Part D ==== Remove front")
    list.pop(0)

    print(list,"\n")

def functionE(list): #reverse the array
    print("==== Part E ==== Reverse")
    list = list[::-1]               #array[::-1] reverses list

    print(list,"\n")

def functionF(list): #add Archie to front (or add element to front)
    print("==== Part F ==== Add front")
    x = 'Archie'
    list = [x]+list                  #[str]+list adds to front

    print(list,"\n")

def functionG(list):
    print ("==== Part G ==== Sort")
    list.sort()                     #list.sort() sorts by ascii

    print(list,"\n")


#Initialize
if __name__ == '__main__':
    list = ['Nick','Susan','Chet','Dolly','Bill']
    print("List: ",list,"\n")

functionA(list)
functionB(list)
functionC(list)
functionD(list)
functionE(list)
functionF(list)
functionG(list)