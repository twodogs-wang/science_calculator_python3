import helper_funcs
import Expression
from Function import _Function
import copy
"""
this file parses the define command, recoginizes what sub-expressions it includes and store it as a function
"""



def __opera(_temp,_it,_Fun_dic,_left_var_list,_v_dict:dict):

    """
    deal with calculations which have two parameters, like plus and minus
    :param _temp: operation sign like '+' or '-'
    :param _it: iterator
    :param _Fun_dic: a dict which stores pre-defined functions
    :param _left_var_list: varible list
    :param _v_dict: variable dictionary which stores the assigned values of each variable for future calculation
    :return: an instance of class "Expression"
    """
    L = __Parse(_it, _Fun_dic, _left_var_list,_v_dict)
    R = __Parse(_it, _Fun_dic, _left_var_list,_v_dict)
    return {'+':Expression._plus_expression,
            '-':Expression._minus_expression,
            '*':Expression._product_expression,
            '/':Expression._divid_expression,
            'pow':Expression._power_expression}[_temp](L,R)

def __special_opeara(_temp,_it,_Fun_dic,_left_var_list,_v_dict:dict):
    """
    same as above, except these operations accepts only one parameter, like sin or cos

    :param _temp:
    :param _it:
    :param _Fun_dic:
    :param _left_var_list:
    :param _v_dict:
    :return:
    """
    L = __Parse(_it, _Fun_dic, _left_var_list,_v_dict)
    _temp_iter = copy.deepcopy(_it)
    _temp_term = __Parse(_temp_iter,_Fun_dic,_left_var_list,_v_dict)
    return {'sin':Expression._sin_expression,
            'cos':Expression._cos_expression,
            'log':Expression._log_expression}[_temp](L)

def __call_function(_it,_fname,_Fun_dic:dict,_left_var_list,_v_dict:dict):
    """
    this function handel cases if a pre-defined function been called

    :param _it:
    :param _fname:
    :param _Fun_dic:
    :param _left_var_list:
    :param _v_dict:
    :return:
    """
    _v_exp_list=[]
    _temp=''
    while True:
        _temp = __Parse(_it,_Fun_dic,_left_var_list,_v_dict)
        #print('*'+_temp+'*')
        if not _temp:
            break

        else:
            _v_exp_list.append(_temp)
            #print(_v_exp_list[0].__to_string__())
    return Expression._call_Fcuntion(_Fun_dic[_fname],_v_exp_list)


def __Parse(_it,_Fun_dic:dict,_left_var_list:list,_v_dict:dict):

    """
    most difficult part, it parse the command to check its math structure
    :param _it:
    :param _Fun_dic:
    :param _left_var_list:
    :param _v_dict:
    :return:
    """

    _operation = ['+', '-', '*', '/', 'pow', 'sin', 'cos', 'log']
    _temp=helper_funcs.__Get_next_item(_it)
    if not _temp or _temp==')':
        return None
    if _temp=='(':
        return __Parse(_it,_Fun_dic,_left_var_list,_v_dict)  #recursion is used here

    elif _temp.isdigit():
        return Expression._num_expression(_temp)

    elif _temp.isalpha() and _temp not in _operation:
        if _temp in _Fun_dic.keys():
            return __call_function(_it,_temp,_Fun_dic,_left_var_list,_v_dict)
        elif _temp in _left_var_list:  #变量
            _temp_var_exp=Expression._var_expression(_temp)
            _v_dict.update({_temp:_temp_var_exp})
            return _temp_var_exp
        else:
            print(_temp+' is not predefined function\n')
            return None

    else:  #opera
        if _temp in ['+','-','*','/','pow']:
            return __opera(_temp,_it,_Fun_dic,_left_var_list,_v_dict)
        else:
            return __special_opeara(_temp,_it,_Fun_dic,_left_var_list,_v_dict)


def __Parse_define_helper(_fname:str,_expression:str,_Fun_dic:dict,_left_var_list:list)->bool:
    #helper function of the above function, these two functions act like a tail-recursion
    _expression=helper_funcs._Spaces_rearrange(_expression)
    if not _expression:
        print('right side expression is empty\n')
        return False


    _v_dict = {}
    _it=iter(_expression)
    try:
        _new_exp=__Parse(_it,_Fun_dic,_left_var_list,_v_dict)
        _temp=helper_funcs.__Get_next_item(_it)
        if not _temp or _temp==')':
            print("your input is: "+_new_exp.__to_string__())
        else:
            print('your input includes extra contents\n')
            return False
    except:
        print('your command includes some weired things\n')
        return False

    _new_func=_Function(_fname,_new_exp,_left_var_list,_v_dict)
    _Fun_dic.update({_fname:_new_func})
    print('Function '+_fname+' has been defined\n')
    return True