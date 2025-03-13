def punto4():
    n = int(input("Ingrese un número de 4 cifras: "))
    if n >= 1000 and n <= 9999:
        n4 = n % 10
        n //= 10
        n3 = n % 10
        n //= 10
        n2 = n % 10
        n //= 10
        n1 = n

        if(n4 and n1 % n4 == 0):
            print(f"El primer digito ({n1}) es multiplo del cuarto digito ({n4})")
        else:
            print(f"El primer digito ({n1}) no es multiplo del cuarto digito ({n4})")

        print("La suma del segundo y tercer dígito es:", n2 + n3)

    else:
        print("El número ingresado no es de 4 cifras")

punto4()