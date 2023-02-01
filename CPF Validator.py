print("Digite um CPF para verificar se ele é válido ou não")
cpf= str(input()) 
to_array = list(cpf)

dig1 = int(to_array[0])
dig2 = int(to_array[1]) 
dig3 = int(to_array[2]) 
dig4 = int(to_array[3]) 
dig5 = int(to_array[4]) 
dig6 = int(to_array[5]) 
dig7 = int(to_array[6]) 
dig8 = int(to_array[7]) 
dig9 = int(to_array[8])

soma= (dig1*10) + (dig2*9) + (dig3*8) + (dig4*7) + (dig5*6) + (dig6*5) + (dig7*4) + (dig8*3) + (dig9*2)

dig10 = (soma*10) % 11

soma2= (dig1*11) + (dig2*10) + (dig3*9) + (dig4*8) + (dig5*7) + (dig6*6) + (dig7*5) + (dig8*4) + (dig9*3) + (dig10*2)

dig11 = (soma2*10) % 11

if dig10 == 10:
    dig10 = 0
    
if dig11 == 10:
    dig11 = 0

txt10 = str(dig10)
txt11 = str(dig11)

if to_array[9] != txt10:
    print("Esse CPF não é válido")
elif to_array[10] != txt11:
    print("Esse CPF não é válido")
else :
    print("Esse CPF é válido")