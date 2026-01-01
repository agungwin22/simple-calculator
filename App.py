import os

class Calculator:
    def __init__(self):
        self.result = 0

    def tambah(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def kurang(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def kali(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def bagi(self, num1, num2):
        if angka2 == 0:
            print("ERROR: tidak bisa dengan 0!")
        self.result = num1 / num2
        return self.result

    def modulus(self, num1, num2):
        if angka2 == 0:
            print("ERROR: tidak bisa dengan 0!")
        self.result = num1 % num2
        return self.result

    def pangkat(self, num1,num2):
        self.result = num1 ** num2
        return self.result

class CalculatorMenu:
    def __init__(self):
        self.calc = Calculator()

    def menu(self):
        print(f"{'WELCOME TO':^40}")
        print(f"{'SIMPLE CALCULATOR':^40}")
        print(f"{'Simple Kalkulator by agungwin22':^40}")
        print("="*40)

    def screen(self):
        while True:
            os.system("cls") # untuk windows
            #os.system("clear") # untuk mc os dan linux

            self.menu()


            try:
                try:
                    num1 = float(input("Masukan angka: "))
                    operator = input("Operator (+,-,/,*,%,^): ")
                    num2 = float(input("Masukan angka: "))
                    print(" ") # hanya untuk bikin jarak tampilan
                except ValueError:
                    print("ERROR: Input tidak valid!")

                # logika perhitungan
                if operator == '+':
                    hasil = self.calc.tambah(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40,"\n")
                elif operator == '-':
                    hasil = self.calc.kurang(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40,"\n")
                elif operator == '*' or operator == 'x':
                    hasil = self.calc.kali(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40)
                elif operator == '/':
                    hasil = self.calc.bagi(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40)
                elif operator == '**' or operator == '^':
                    hasil = self.calc.pangkat(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40)
                elif operator == '%':
                    hasil = self.calc.modulus(num1, num2)
                    print("-"*40)
                    print(f"Hasil: {num1} {operator} {num2} = {hasil}")
                    print("-"*40,"\n")
                else:
                    print("ERROR: Input tidak Valid!")

                isdone = input("\nLanjutkan (y/n) ? ")

                if isdone == 'n':
                    print("\nTerima Kasih Telah menggunakan Aplikasi ini!")
                    break

            except Exception as e:
                print(f"Terjadi Error: {e}")


# program utama
if __name__ == "__main__":
    main = CalculatorMenu()
    main.screen()
