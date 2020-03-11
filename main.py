BinorDin = input("Hello. please press 1 to convert Denary to Binary, and press 2 to convert Binary to denary ")

BinorDin = int(BinorDin)

if BinorDin == 1:

    Number = input("Great. Please enter a whole number between 0-255 and I will convert it into binary. ")

    Number = int(Number)

    NumBi = bin(Number)[2:]

    NumHex = hex(Number)[2:]

    if Number < 16:
        print("denary: ", Number)
        print("binary: ", NumBi.zfill(4))
        print("Hexadecimal: ", NumHex)

    elif Number < 256:
        print("denary: ", Number)
        print("binary: ", NumBi.zfill(8))
        print("Hexadecimal: ", NumHex)

    else:
        print("Incorrect value. Please try again. Remember, it must be a number between 0-255 (inclusive) and cannot include any decimal places.")

elif BinorDin == 2:

    Number = input("Great. Please enter a positive binary number between 0000 and 1111 1111 and I will convert it into binary. ")
    
    Number = int(Number)

    Number = bin(Number)[2:]

    NumDe = int(Number, 2)

    NumCheck = int(Number)

    print(NumCheck)

    #NumHex = hex(Number)[2:]

    if NumCheck < 16:
        print("denary: ", NumDe)
        print("binary: ", Number.zfill(4))
        #print("Hexadecimal: ", NumHex)

    elif NumCheck < 255:
        print("denary: ", NumDe)
        print("binary: ", Number.zfill(8))
       # print("Hexadecimal: ", NumHex)

    else:
        print("Incorrect value. Please try again. Remember, it must be a number between 0-255 (inclusive) and cannot include any decimal places")

else:
    print("Please only press the number 1 or 2.")
