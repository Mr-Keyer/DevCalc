import os


#Estetica
CIANO = "\033[96m"
VERDE = "\033[92m"
RESET = "\033[0m"
BOLD  = "\033[1m"

arte = f"""{CIANO}{BOLD}
██████╗ ███████╗██╗   ██╗ ██████╗ █████╗ ██╗      ██████╗
██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██║     ██╔════╝
██║  ██║█████╗  ██║   ██║██║     ███████║██║     ██║
██║  ██║██╔══╝  ╚██╗ ██╔╝██║     ██╔══██║██║     ██║
██████╔╝███████╗ ╚████╔╝ ╚██████╗██║  ██║███████╗╚██████╗
╚═════╝ ╚══════╝  ╚═══╝   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
{RESET}"""

#Funcionalidades
def com_prefixo(num):
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
        os.system('clear')
        print(arte)
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
