import tabulate as tb
from tabulate import tabulate
from itertools import zip_longest 
import pyfiglet
    
def main():
    intro = pyfiglet.figlet_format("By : Kelompok 5 ")
    q=1
    while True:
        if q==1:
            print("-----------------------------------------------------------------------------") 
            print("Program Sederhana Untuk Konversi Bilangan Desimal - Biner - Oktal - Heksadesimal")    
            print(intro)
            print("-----------------------------------------------------------------------------")          
            number = int(input("Masukkan Bilangan Desimal yang akan dikonversi : "))
            print("-----------------------------------------------------------------------------")
            # proses
            header = ['Biner', 'Octal', 'Hexa']
            # Biner
            dataBiner = []
            n=0
            resultbiner=""
            binNumb = number
            bin=binNumb
            txt = str(bin).center(9, " ")
            dataBiner.append(txt)
            while binNumb > 1:
                if binNumb % 2 == 0:
                    n=0
                else:
                    n=1
                resultbiner += str(n)
                dataBiner.append("2------ {:<20}".format(n))
                bin=int(binNumb/2)
                txt2 = str(bin).center(9, " ")
                dataBiner.append(txt2)
                if bin == 1:
                    resultbiner += str(bin)
                binNumb = bin
            # End-Biner
            # Octal
            dataOctal = []
            oktal = 0
            octNumb = number
            resultoktal=""
            txt3 = str(octNumb).center(9, " ")
            dataOctal.append(txt3)
            while octNumb >= 8:
                sisa = octNumb%8
                if sisa == 0:
                    oktal = int(octNumb/8)
                else:
                    oktal = int((octNumb-sisa)/8)
                resultoktal += str(sisa)
                dataOctal.append("8------ {:<15}".format(sisa))
                txt4 = str(oktal).center(9, " ")
                dataOctal.append(txt4)
                if oktal <= 8:
                    resultoktal += str(oktal)
                octNumb = oktal
            # End-Octal
            # Hexa
            dataHexa = []
            digits = "0123456789ABCDEF"
            hexa = 0
            hexNumb = number
            resulthexa = ""
            if hexNumb < 16:
                dataHexa.append(" {} = {}".format(hexNumb, digits[hexNumb]))
                resulthexa += digits[hexNumb]
            else:
                txt5 = str(hexNumb).center(9, " ")
                dataHexa.append(txt5)
                while hexNumb >= 16:
                    sisa = hexNumb%16
                    if sisa == 0:
                        hexa = int(hexNumb/16)
                    else:
                        hexa = int((hexNumb-sisa)/16)
                    if sisa > 9:
                        resHexa = digits[sisa]
                        dataHexa.append("16------ {} = {}".format(sisa,resHexa))
                    else:
                        resHexa = sisa
                        dataHexa.append("16------ {}".format(resHexa))
                    resulthexa += str(resHexa)
                    
                    if 9 < hexa < 16 :
                        resulthexa += str(digits[hexa])
                        dataHexa.append(" {} = {}".format(hexa, digits[hexa]))
                    elif hexa < 10:
                        resulthexa += str(hexa)
                        txt6 = str(hexa).center(9, " ")
                        dataHexa.append("{} ".format(txt6))
                    else:
                        txt6 = str(hexa).center(9, " ")
                        dataHexa.append("{} ".format(txt6))
                    hexNumb = hexa
            # End-Hexa
            result = list(zip_longest(dataBiner, dataOctal, dataHexa))
            tb.PRESERVE_WHITESPACE = True
            print(tabulate(result, header, tablefmt="plain"))
            print("--------------------------------------------------------------------------")
            print("Biner = {:<20} Octal = {:<15} Hexa = {:<15}".format((resultbiner[::-1]),(resultoktal[::-1]),(resulthexa[::-1])))
            print("Apakah ingin mengulangi proses?")
            q=int(input("[ Tekan 1 untuk = Ya | Tekan 0 untuk = Exit] : "))
        else:
            break

if __name__ == '__main__' :
    main()
