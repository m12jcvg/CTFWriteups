# Runme

### Solución #1 (Fácil)
```
strings runme.exe

BRjS
BRjE
BRjC
BRjC
BRjO
BRjN
BRj{
BRjR
BRju
BRjn
BRjn
BRj1
BRjn
BRj6
BRj_
BRjP
BRj4
BRj7
BRjh
BRj}

```



### Solución #2


En la funcion principal en IDA vemos

```

call    ds:GetCommandLineA
mov     [ebp+var_4], eax
push    eax
push    22h             ; uExitCode
call    sub_401034

```

De acuerdo a la ayuda de GetCommandLineA

```
The return value is a pointer to the command-line string for the current process.
```

Por lo que sabemos que a la funcion sub_401034 le pasa la linea de comandos del proceso.

Dentro de sub_401034, encontramos


```

arg_0= byte ptr  8
arg_4= dword ptr  0Ch

push    ebp
mov     ebp, esp
push    esi
movzx   ecx, [ebp+arg_0]
mov     edx, [ebp+arg_4]
movzx   edx, byte ptr [edx]
cmp     ecx, edx
jnz     loc_4018BB

mov     ecx, 1
mov     edx, [ebp+arg_4]
inc     edx
push    edx
push    43h
call    sub_401060
pop     esi
mov     esp, ebp
pop     ebp
retn

```

como podemos ver compara los 2 parametros recibidos y si NO son iguales se va a la condicion de salida que esta en loc_4018BB, de lo contrario incrementa en 1 edx, lo pasa de nuevo a la funcion junto con el siguiente valor contra lo que va a comparar y así sucesivamente hasta llegar al último caracer.

```
loc_4018BB:
	push    40h
	push    offset aFailed  ; "Failed"
	push    offset aTheEnvironment ; "The environment is not correct."
	push    0               ; hWnd
	call    ds:MessageBoxA
	call    ds:ExitProcess

```

Tip:

	En IDA puedes ubicar el cursor en el 43h y presionar "r" para que lo convierta en su valor ASCII, repetir con todas las funciones para sacar el flag si es que no te sabes el ASCII de memoria.
