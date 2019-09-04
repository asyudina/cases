
def isPalindrome(x: int):

    if x<0:
        return False 
    elif x ==0:
        return True 
    else:
        lst1 = [int(d) for d in str(x)]
        lst2  = []
        if len(lst1) == 1:
            return x
        cur_pos = 0 
        for el in range(len(lst1)-1,-1,-1):
            if lst1[el] == lst1[el-el+cur_pos]:
                lst2.append(lst1[el])
                cur_pos +=1
            else:
                return False
    try:         
        poly = int("".join(list(map(str,lst2))))
    except:
        return False

    return poly

