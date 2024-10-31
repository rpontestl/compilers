funcaoTeste1:
param1 dd 0
param2 dd 0
soma dd 0
name equ "programa teste"
call print
L1:
cmp soma<100, 0
je L2
cmp soma<=90||param1>20, 0
je L3
mov eax, [soma]
jmp L4
L3:
L4:
jmp L1
L2:
mov eax, [soma]
cmp soma<=90||param1>20, 0
je L5
mov eax, [soma]
jmp L6
L5:
L6:
mov eax, [soma<=90]
mov eax, [soma]
mov eax, [param1]
mov eax, [soma]
mov eax, [soma]
mov eax, [soma]
mov eax, [soma]
mov eax, [soma]
mov eax, [soma]
ret
