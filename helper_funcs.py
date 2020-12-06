"""
this file contains helper functions that is used through the entire program
"""

def __Check_equal_signs(_str:str)->bool:
    #check the number of equal signs
    num=_str.count('=')
    if not num==1:
        print("等号数量不对\n")
        return False
    return True

def __Split_define_command(_str:str):
    #split command at equal sign into two parts
    _temp=_str.split('=')
    assert len(_temp)==2
    return _Spaces_rearrange(_temp[0]),_Spaces_rearrange(_temp[1])

def __Check_parenthesis(_str:str)->bool:
    #check if number of parenthesis is symmetry.
    buffer=[]
    for i in _str:
        if i=='(':
            buffer.append(i)
        elif i==')':
            buffer.pop()
        else:
            continue
    if len(buffer)==0:
        return True
    else:
        print("括号数量不对\n")
        return False

def _Spaces_rearrange(_str:str)->str:
    #this function removes redunt spaces

    _str=_str.strip(' ')

    if not _str:
        return ''
    _ans=''
    _ans+=_str[0]

    for i in range(1,len(_str)):
        if not _str[i]==' ':
            _ans+=_str[i]
        elif _str[i]==' ' and _str[i-1] ==' ':
            continue
        else:
            _ans+=' '

    return _ans



def __Get_next_term(_it)->str:
    #get next term (str)
    _ans=''
    flag=True
    while True:
        try:
            _temp=next(_it)
            if _temp=='(':
                if flag:  # in case the command has only "("
                    #flag=False
                    continue
                else:
                    break
            elif _temp==' ' or _temp==')':
                break
            else:
                flag=False
                _ans+=_temp
        except StopIteration:
            break
    return _ans

def __Remove_first_item(_str:str)->str:
    #as it says, remove the first term of a command string
    _str=_Spaces_rearrange(_str)
    _str=_str.split(' ')
    _ans=''

    for i in range(1,len(_str)):
        _ans+=_str[i]+' '
    #print(_ans)
    #print(_Spaces_rearrange(_ans))
    return _Spaces_rearrange(_ans)

def __adjusted_isalpha(_str:str)->bool:
    #check if the input includes anything other than digit or alpha
    for i in _str:
        if i==' ':
            continue
        elif i.isalpha():
            continue
        else:
            return False
    return True

def __Get_next_item(_it):#################
    #get next term of a string based on the input iterator
    flag=True
    _ans=''
    while True:
        try:
            _temp=next(_it)
            if _temp==' ':
                if flag:
                    flag=False
                    continue
                else:
                     break
            elif _temp=="(":
                if _ans:
                    break
                else:
                    return "("
            elif _temp==")":
                if _ans:
                    break
                else:
                    return ")"
            else:
                flag=False
                _ans+=_temp

        except StopIteration:
            break
    return _ans

