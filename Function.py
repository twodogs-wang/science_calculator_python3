import Expression
import copy

"""
this file contains classes I defined called "Function", Which handles user define ,store functions
"""

class _Function:
    def __init__(self,_name,_exp,_v_list,v_dict):
        self._fname=copy.deepcopy(_name)
        self._expression=_exp
        self._vname_list=_v_list[:] #存储变量名
        self._v_dict=v_dict

    def __get_vsize__(self):
        return len(self._vname_list)

    def __set_value__(self,_var_values):
        #print('setting\n')
        for i in range(len(self._vname_list)):
            try:
                _temp=self._v_dict[self._vname_list[i]]
                _temp.__set_value__(_var_values[i])
            except:
                #print("chicken special")
                continue

        #print(_var_values)
    def __reset__(self):
        for key in self._v_dict.keys():
            self._v_dict[key].__reset__()

    def __calculate__(self,_v_values):
        self.__set_value__(_v_values)
        _ans=self._expression.__to_number__()
        self.__reset__()
        return _ans

    def __get_name__(self):
        return self._fname

    def __get_vdict__(self):
        return self._v_dict
