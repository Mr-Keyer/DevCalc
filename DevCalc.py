print("=" * 50)
print("CALCUADORA DO PROGRAMADOR")
print("=" * 50)

def com_prefixo(num):
    print(f"Decimal: {num}")
    print(f"Binário: {bin(num)}")
    print(f"Octal: {oct(num)}")
    print(f"Hexadecimal: {hex(num)}")

def sem_prefixo(num):
    print(f"Binário: {num:b}")
    print(f"Octal: {num:o}")
    print(f"Hexadecimal: {num:x}")   # minúsculo
    print(f"Hexadecimal: {num:X}")   # maiúsculo


if __name__ == '__main__':

    while True:
        print("\n1 - Com prefixo.")
        print("2 - Sem prefixo.")
        print("3 - Sair.")


        op = input("Digite a sua preferencia:\n ")
        

        try:
            if op == "1":
                num = int(input("\nInsira o numero para ver:\nO binario.\nOctal.\nHexadecimal.\nDecimal.\nInserir o numero:\n "))
                com_prefixo(num)

            elif  op == "2":
                num = int(input("\nInsira o numero para ver:\nO binario.\nOctal.\nHexadecimal.\nDecimal.\nInserir o numero:\n "))
                sem_prefixo(num)

            elif op == "3":
                print("Saindo...")
                break 
            else:
                print("Escolha invalida.")

        except ValueError:
            print("Digite apenas numeros inteiros: ")
