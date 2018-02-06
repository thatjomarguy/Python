def elective():
    myDic = {'2CPR2B': 'C Language',
             '1UNX1B': 'Intro to UNIX',
             '3SH414': 'Shell Programming',
             '4PL400': 'Perl Programming'}

    sortedDic = iter(sorted(myDic.items())) #sorts the iterations (keys) in order

    for key,value in sortedDic:
        print (key,value)                   #prints the sorted key and value

    while True:
        enter = input('\nEnter code number of course (-1 to exit)\n')
        if enter == '-1':                   #exit case
            break

        if enter in myDic.keys():           #if key is present print. else none
            print("You will be taking",myDic.get(enter),"this semester.")

if __name__ == '__main__':
    elective()