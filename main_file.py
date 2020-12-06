"""
this file is the entrance of the entire program

"""

import helper_funcs
import Expression
from Function import _Function
from Define import __define
from test import __test

def __execute(_type:str,_command:str,_Func_dic:dict)->bool:

    """
    :param _type: command type, like "define" or "test"
    :param _command: the entire command like define function or test pre-defined functions
    :param _Func_dic: The dict which stores predefined functions
    :return: return the return value of function "__define" or function "__test" depends on command type
    """
    #print(_command)
    #try:
    return {'define' : __define,
            'test' :__test}[_type](_command, _Func_dic)
    #except:
        #print('invalid input.....')




_type_tuple = ('define','test','quit')
_Func_dic={}

while True:
    print('please type your command\n')
    _command=input()

    if not _command:
        print('invalid input\n')
        continue

    _command=helper_funcs._Spaces_rearrange(_command)      #delete un-needed white-spaces
    _command=_command.lower()
    _flag=helper_funcs.__Check_parenthesis(_command)       #check the format of commands

    if _command == 'quit' or _command=='quit()':
        break

    else:
        _it=iter(_command)            #create an iterator for further parsing processes
        _type=helper_funcs.__Get_next_term(_it)
        _command=helper_funcs.__Remove_first_item(_command)  #separate type ("define" or "test") and the command

        if not _type in _type_tuple:
            print('unknown command type\n')
            continue
        elif not _command:
            print('command is too short\n')
            continue

        if not __execute(_type,_command,_Func_dic):
            continue

