funcaoTeste1:
param1 dd 0
param2 dd 0
soma dd 0
name equ "programa teste"
mov eax, offset "programa teste"
call print
mov eax, offset "teste"
L1:
cmp soma!=100, 0
je L2
cmp soma!=60, 0
je L3
mov eax, [soma]
jmp L4
L3:
L4:
jmp L1
L2:
cmp soma!=60, 0
je L5
mov eax, [soma]
jmp L6
L5:
L6:
mov eax, [soma]
mov eax, [soma]
ret
