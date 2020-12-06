from Function import _Function
import Expression
import helper_funcs
import math

"""
this file contains the test part, which could assign values to pre-defined functions and calculate.
"""

def __opera(_it:iter,_Func_dic:dict,_opera:str): #handle baisc calculations
    L=__test_helper(_it,_Func_dic)
    R=__test_helper(_it,_Func_dic)
    if not L or not R:
        print('your command includes some weired things\n')
        return None
    return {'+':lambda x,y:x+y,
            '-':lambda x,y:x-y,
            '*':lambda x,y:x*y,
             '/':lambda x,y:x/y,
            'pow':lambda x,y:x**y}[_opera](L,R)

def __single_opera(_it:iter,_Func_dic:dict,_opera:str): #handle basic calculations
    L = __test_helper(_it, _Func_dic)
    if not L:
        print('your command includes some weired things\n')
        return None
    return {'sin':lambda:math.sin(L),
            'cos':lambda :math.cos(L),
            'log':lambda :math.log(L)
            }[_opera]()

def __call_func(_it:iter,_Func_dic:dict,_fname):  #call a pre-defined function
    _temp_func=_Func_dic[_fname]
    #_var_dict=_temp_func.__get_vdict__()
    v_list=[]
    for i in range(_temp_func.__get_vsize__()):
        _temp=__test_helper(_it,_Func_dic)
        if not _temp:
            print('wrong numbers of numbers\n')
            return None
        v_list.append(_temp)
    #print(v_list)
    return _temp_func.__calculate__(v_list)

def __test_helper(_it:iter,_Func_dic:dict)->float:  #a helper functions, also acts like a tail-recursion with the above
    _operation = ['+', '-', '*', '/', 'pow']
    _single_operation=['sin', 'cos', 'log']
    _temp = helper_funcs.__Get_next_item(_it)
    if not _temp:
        return None

    if _temp=='(':
        return __test_helper(_it,_Func_dic)

    elif _temp.isdigit():
        return float(_temp)

    elif _temp in _operation:
        return __opera(_it,_Func_dic,_temp)

    elif _temp in _single_operation:
        return __single_opera(_it,_Func_dic,_temp)

    elif _temp.isalpha():
        if _temp in _Func_dic.keys():
            return __call_func(_it,_Func_dic,_temp)
        else:
            print(_temp+' is not pre_defined!!!!!\n')
            return None


def __test(_command:str,_Func_dic:dict)->bool:
    """
    the entrance function of "testing" feature, this function is called in the main file.

    :param _command:
    :param _Func_dic:
    :return: displays the calculated answer and rerturn True, or False if command is not valid.
    """
    _command=helper_funcs._Spaces_rearrange(_command)
    if not _command:
        print('your command is invalid\n')
        return False
    else:
        _it=iter(_command)
        _ans=__test_helper(_it,_Func_dic)
        #print(_ans)
        _temp=helper_funcs.__Get_next_item(_it)
        if not _ans and not _ans==0:
            return False
        elif _temp and not _temp==')':
            print('your command includes extra contents: \n')
            return False
        print('answer'+ ' = ' + str(_ans)+'\n')
    return True