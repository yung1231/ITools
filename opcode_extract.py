#coding:utf-8

import idc 
import idautils 
import idaapi
import json
import sys

idaapi.auto_wait()

opcodes = list()
for function_ea, real_name in idautils.Names():
    opcode = ""
    for ins in idautils.FuncItems(function_ea):
        if idaapi.is_code(idaapi.get_flags(ins)):
            asm = idc.GetDisasm(ins)
            mnem = asm.split(' ')[0]
            if mnem[-1]==';':
                opcode+=mnem[:-1]+' '
            else:
                opcode+=mnem+' '
    if len(opcode.rstrip()) and len(opcode.rstrip())>18:
        opcodes.append(opcode.rstrip())    
    
with open(f"{idc.ARGV[2]}\{idc.ARGV[1]}.json", "a") as f:
    json.dump({'opcodes': opcodes}, f)

idc.qexit(0)