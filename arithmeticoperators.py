'''
given an exclp and taxrate providrd by the user,
calculate the VATamt then return the inclp


excl = 50
rate = 0.16
vat = 0
incl = 0

vat = excl * rate
incl = excl + vat

print(incl)
print(vat)


given incl and tax provided by user,
calculate vat and excl


def calculatevat():
    excl = 0
    rate = 0.16
    vat = 0
    incl = 60.0068

    vat = incl * rate
    excl = incl - vat

    print(excl)

calculatevat()


def calculateVAT():
    exclusivePrice = 51.73
    vatTax = 0.16 #16/100
    vatAmount = 0
    inclusivePrice = 0

    vatAmount = exclusivePrice * vatTax
    inclusivePrice = exclusivePrice + vatAmount

    return inclusivePrice

print(calculateVAT())

def calculateVAT(exclusivePrice, vatTax):
    vatAmount = 0
    inclusivePrice = 0

    vatAmount = exclusivePrice * vatTax
    inclusivePrice = exclusivePrice + vatAmount

    return inclusivePrice

print(calculateVAT(51, 0.16))
'''


def calculateVAT(exclusivePrice, vatTax):
    vatAmount = exclusivePrice * vatTax
    inclusivePrice = exclusivePrice + vatAmount

    return inclusivePrice

def userInputs():
    excl = float(input("Enter the excl amount"))
    vatTax = float(input("Enter VAT Tax"))
    incl = calculateVAT(excl, vatTax)

    print(incl)

userInputs()