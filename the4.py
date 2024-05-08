def is_there_list(T):
    for elm in T:
        if type(elm) == list:
            return True
    return False

def current_list_finder(T, pname): 
    if pname in T:
        return T
    else:
        for i,elm in enumerate(T):
            if type(elm) == list:
                if pname in elm:
                    return elm
                elif is_there_list(elm):
                    if current_list_finder(elm,pname) != None:
                        return current_list_finder(elm, pname)
                    else: 
                        current_list_finder(T[i+1:], pname)
def upper_list(T,pname):
    lst = current_list_finder(T, pname)
    if lst in T:
        return T
    else:
        for i,elm in enumerate(T):
            if type(elm) == list:
                if lst in elm:
                    return elm
                if current_list_finder(elm,lst) != None:
                    return current_list_finder(elm, lst)
                else: 
                    current_list_finder(T[i+1:], lst)

def parent(T,pname):
    lst = current_list_finder(T, pname)
    if lst == None:
        return []
    if lst.index(pname) != 0:
        return lst[0]
    else:
        upper = upper_list(T,pname)
        if upper == None:
            return []
        return upper[0]


def children(T, pname):
    lst = current_list_finder(T, pname)
    result = []
    if pname != lst[0]:
        return result
    for i,elm in enumerate(lst):
        if  i == 0:
            continue
        elif type(elm) == list:
            result.append(elm[0])
        else:
            result.append(elm)

    return result            

def women(pname):
    return pname[0].isupper()             



def brothers(T, pname):
    result = []
    if pname == T[0] or pname == []:
        return []
    sibs = siblings(T,pname)
    for sib in sibs:
        if women(sib):
            continue
        result.append(sib)
    return result




def sisters(T, pname):
    result = []
    if pname == T[0] or pname == []:
        return []
    sibs = siblings(T,pname)
    for sib in sibs:
        if women(sib):
            result.append(sib)
    return result



def siblings(T, pname):
    if pname == T[0] or pname == []:
        return []    
    result = []
    prnt = parent(T, pname)
    childs = children(T,prnt)
    for elm in childs:
        if elm != pname:
            result.append(elm)
    return result

def uncles(T, pname):
    if pname == T[0]:
        return []
    prnt = parent(T,pname)
    if prnt == T[0]:
        return []
    return brothers(T,prnt)

def aunts(T, pname):
    if pname == T[0]:
        return []
    prnt = parent(T,pname)
    if prnt == T[0]:
        return []
    return sisters(T,prnt)


def cousins(T, pname):
    if pname == T[0]:
        return []
    result = []
    ants = aunts(T,pname)
    uncls = uncles(T,pname)
    if ants != []:
        for a in ants:
            result += children(T,a)
    if uncls != []:
        for u in uncls:
            result +=children(T,u)
    return result
