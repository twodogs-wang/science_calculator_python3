from Function import _Function
import copy
import math
"""
this file contains the class I defined called "Expression", all other expressions like plus, minus, sin and cos are all
its sub-classes

Also it includes a class called "call function", which handles pre-defined functions been called
"""

class Expression:
    def __init__(self):
        pass
    def __to_string__(self):
        pass
    def __to_number__(self):
        pass

class _num_expression(Expression):
    def __init__(self,_num):
        self.number=float(_num)
        self._str=_num
    def __to_string__(self):
        return self._str

    def __to_number__(self):
        return self.number

class _var_expression(Expression):
    def __init__(self,_v):
        self._vname=_v
        self._value=None
        self._flag=False

    def __to_string__(self):
        return self._vname

    def __set_value__(self, number):
        self._value=number
        #print('here')
        self._flag=True

    def __to_number__(self):
        if self._flag:
            #print(self.value)
            return self._value
        else:
            print('variable '+self._vname+' has not been assigned\n')
            return None

    def __reset__(self):
        self._value=None
        self._flag=False

class _plus_expression(Expression):

    def __init__(self,left,right):
        #self.opera=operator.copy()
        self.L=left
        self.R=right

    def __to_string__(self):
        _str="("+self.L.__to_string__()+" + "+self.R.__to_string__()+")"
        return _str

    def __to_number__(self):
        _num=self.L.__to_number__()+self.R.__to_number__()
        return _num


class _minus_expression(Expression):
    def __init__(self,left,right):
        #self.opera=operator.copy()
        self.L=left
        self.R=right

    def __to_string__(self):
        _str="("+self.L.__to_string__()+" - "+self.R.__to_string__()+")"
        return _str

    def __to_number__(self):
        _num=self.L.__to_number__() - self.R.__to_number__()
        return _num


class _divid_expression(Expression):
    def __init__(self,left,right):
        #self.opera=operator.copy()
        self.L=left
        self.R=right

    def __to_string__(self):
        _str='('+self.L.__to_string__()+" / "+self.R.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=self.L.__to_number__() / self.R.__to_number__()
        return _num

class _product_expression(Expression):
    def __init__(self,left,right):
        #self.opera=operator.copy()
        self.L=left
        self.R=right

    def __to_string__(self):
        _str='('+self.L.__to_string__()+" x "+self.R.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=self.L.__to_number__() * self.R.__to_number__()
        return _num

class _power_expression(Expression):
    def __init__(self,left,right):
        #self.opera=operator.copy()
        self.L=left
        self.R=right

    def __to_string__(self):
        _str='pow'+'('+self.L.__to_string__()+" , "+self.R.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=self.L.__to_number__() ** self.R.__to_number__()
        return _num

class _sin_expression(Expression):
    def __init__(self,left):
        #self.opera=operator.copy()
        self.L=left

    def __to_string__(self):
        _str='sin('+self.L.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=math.sin(self.L.__to_number__())
        return _num

class _cos_expression(Expression):
    def __init__(self,left):
        #self.opera=operator.copy()
        self.L=left

    def __to_string__(self):
        _str='cos('+self.L.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=math.cos(self.L.__to_number__())
        return _num

class _log_expression(Expression):
    def __init__(self,left):
        #self.opera=operator.copy()
        self.L=left

    def __to_string__(self):
        _str='log('+self.L.__to_string__()+')'
        return _str

    def __to_number__(self):
        _num=math.log(self.L.__to_number__())
        return _num

class _call_Fcuntion(Expression):
    def __init__(self,F,_var_exp_list):
        self._function=F
        self._fname=F.__get_name__()
        self._v_exp_list=_var_exp_list

    def __to_string__(self):
        _str=''
        for i in self._v_exp_list:
            _str+=i.__to_string__()+' '
        _str=self._fname+'('+_str[:-1]+')'
        return _str

    def __to_number__(self):
        _temp_list=[]
        for i in range(len(self._v_exp_list)):
            _temp_list.append(self._v_exp_list[i].__to_number__())
        return self._function.__calculate(_temp_list)
