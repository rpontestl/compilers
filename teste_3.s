funcaoTeste1:
param1 dd 0
param2 dd 0
soma dd 0
name equ "programa teste"
mov eax, offset "programa teste"
call print
mov eax, offset "teste"
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
cmp soma<=90||param1>20, 0
je L5
mov eax, [soma]
jmp L6
L5:
L6:
push eax
mov ebx, eax
pop eax
cmp eax, 0
jne L7
cmp ebx, 0
jne L7
mov eax, 0
jmp L8
L7:
mov eax, 1
L8:
mov eax, [soma]
mov eax, [soma]
ret
main:
param3 dd 0
a dd 0
mov eax, [a]
mov eax, 1
mov eax, 1
ret
