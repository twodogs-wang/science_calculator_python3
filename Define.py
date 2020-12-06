import helper_funcs
from Parse_define import __Parse_define_helper
import Function
"""
this file includes the code for "define" feature
"""

def __Check_right_exp(_right_exp):

    """
    :param _right_exp: the part after the equal sign of the command
    :return: True if the command does not include special unsupported symbols
    """
    for i in _right_exp:
        if i==' ':
            continue
        elif i in ['+','-','*','/','pow','log','sin','cos']:
            continue
        elif i == '(' or i==")":
            continue
        elif i.isalpha() or i.isdigit():
            continue
        else:
            print("your command contains invalid symbol\n")
            return False
    return True


def __Check_fname(_fname:str, _Func_dic:dict)->bool:

    """
    the define command should include a not pre-defined function name
    :param _fname: function name within the command
    :param _Func_dic: the dict which stores pre-defined function
    :return: True if the function name is not pre-defined
    """

    if not _fname:
        print("function name can not be empty\n")
        return False

    elif _fname in _Func_dic.keys():
        print(_fname+' has been defined\n')
        return False

    elif _fname in ['define','test','quit']:
        print('critical word ' + _fname+ ' can not be used as a function name\n')
        return False
    return True

def __get_var_list(_it:iter,_Fun_dic:dict):
    """
    a define command may includes variables in addition of a function name

    :param _it: iterator
    :param _Fun_dic: the dict that contains pre-defined functions
    :return:a list which contains variables
    """
    _ans=[]
    while True:
        _temp=helper_funcs.__Get_next_term(_it)
        if not _temp:
            break
        elif _temp in _Fun_dic.keys():
            print(_temp + ' is a pre-defined function\n' )
            return None
        elif _temp in _ans:
            print(_temp+' variable symbol can not be used twice\n')
            return None
        _ans.append(_temp)

    if not _ans:
        print('no variable found\n')
    return _ans



def __define(_command:str, _Func_dic:dict)->bool:
    #so far, the define comand, the string "define" has been removed
    #parse define command and store it
    """
    input:
            _command: command
            _Func_dic: a dictionary that stores all function objects
    """
    if not helper_funcs.__Check_equal_signs(_command):
        return False
    _command=helper_funcs._Spaces_rearrange(_command)

    _left_exp, _right_exp = helper_funcs.__Split_define_command(_command) #split by '=' sign

    if not _left_exp or not _right_exp:
        print("command is too short\n")
        return False

    elif not helper_funcs.__adjusted_isalpha(_left_exp):
        print('left side expression contains non-alpha symbols\n')
        return False

    _it=iter(_left_exp)
    _fname=helper_funcs.__Get_next_term(_it)
    if not __Check_fname(_fname,_Func_dic):
        return False

    _left_var_list=__get_var_list(_it,_Func_dic)
    if not _left_var_list:
        #print('variable can not be empty\n')
        return False

    if _fname in _left_var_list:
        print('Function name '+ _fname+ ' can not be used as variable again\n')
        return False
    #check if function name is used as a variable
    if not _right_exp:
        print('no define expression\n')
        return False
    elif not __Check_right_exp(_right_exp):
        return False
    if not __Parse_define_helper(_fname,_right_exp,_Func_dic,_left_var_list):
        return False
    else:

        return True

    return True