
#Given a 32-bit signed integer, reverse digits of an integer.
def reverse(x: int):

    init = x
    if init<0:
        init=abs(init)


        lst1 = [int(d) for d in str(init)]

        lst2 = ['-']

        for el in range(len(lst1)-1,-1,-1):
            lst2.append(lst1[el])

        if lst2[-1] ==0:
            del lst2[-1]

        try:
            rev = int("".join(list(map(str,lst2)))) 
            if rev > (2**31-1) or rev < (-2**31):
                rev = 0
        except:
            rev = 0

    else: 
        lst1 = [int(d) for d in str(init)]

        lst2 = []

        for el in range(len(lst1)-1,-1,-1):
            lst2.append(lst1[el])

        if lst2[-1] ==0:
            del lst2[-1]
        try: 
            rev = int("".join(list(map(str,lst2))))
            if rev > (2**31-1) or rev < (-2**31):
                rev = 0
        except:
            rev = 0
    return rev

