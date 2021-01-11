##try:
##    num = int(input("Digite um numero de 0 a 100: "))
##    
##    if (len(str(num)) > 10):
##        raise ValueError("não pode ter mais que 10 digitos")
##    if (num > 100 or num < 0):
##        raise TypeError("O numero tem que ser igual ou maior que -1 e menor ou igual a 100 ")
##except ValueError as e:
##    print("Erro")
##except TypeError as e:
##    print(str(e) + " Erro")


##try:
##    f= open("VuckVuck.txt","r+")
##except FileNotFoundError as e:
##    print("File not found")
##print("?")

##class circle:
##    def __init__(self, r):
##        if(type(r) is not int):
##            raise TypeError("Raio deve ser inteiro")
##        else:
##            self.r = r
##        
##try:
##    circle("TESTE")
##except TypeError as e:
##    print(e)
##    print("erro")
##print(oi)
