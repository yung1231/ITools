#coding:utf-8

import idc 
import idautils 
import idaapi
import json
import sys

idaapi.auto_wait()

print('--- Start IDAPython ---')


opcodes = list()
for function_ea, real_name in idautils.Names():
    print('real_name: ', real_name, '\tfunction_ea: ', function_ea)
    opcode = ""
    for ins in idautils.FuncItems(function_ea):
        print('ins: ', ins, hex(ins))
        if idaapi.is_code(idaapi.get_flags(ins)):
            cmd = idc.GetDisasm(ins)
            mnem = cmd.split(' ')[0]
            # print(mnem)
            opcode+=mnem+' '
    if len(opcode.rstrip()) and len(opcode.rstrip())>18:
        opcodes.append(opcode.rstrip())
    print('-'*50)     
    
with open(f"{idc.ARGV[2]}\{idc.ARGV[1]}_opcodes.json", "a") as f:
    json.dump({'opcodes': opcodes}, f)

print('--- End IDAPython ---')
idc.qexit(0)