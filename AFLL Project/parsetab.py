
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA FLOAT INTEGER LBRACKET RBRACKET STRINGlist : LBRACKET values RBRACKETvalues : value\n              | value COMMA valuesvalue : INTEGER\n             | FLOAT\n             | STRING'
    
_lr_action_items = {'LBRACKET':([0,],[2,]),'$end':([1,8,],[0,-1,]),'INTEGER':([2,9,],[5,5,]),'FLOAT':([2,9,],[6,6,]),'STRING':([2,9,],[7,7,]),'RBRACKET':([3,4,5,6,7,10,],[8,-2,-4,-5,-6,-3,]),'COMMA':([4,5,6,7,],[9,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'list':([0,],[1,]),'values':([2,9,],[3,10,]),'value':([2,9,],[4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> list","S'",1,None,None,None),
  ('list -> LBRACKET values RBRACKET','list',3,'p_list','listdeclaration.py',46),
  ('values -> value','values',1,'p_values','listdeclaration.py',50),
  ('values -> value COMMA values','values',3,'p_values','listdeclaration.py',51),
  ('value -> INTEGER','value',1,'p_value','listdeclaration.py',59),
  ('value -> FLOAT','value',1,'p_value','listdeclaration.py',60),
  ('value -> STRING','value',1,'p_value','listdeclaration.py',61),
]
