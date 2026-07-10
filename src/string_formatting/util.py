def print_formatted(number):
    width = len(bin(number)[2:])              #to remove the unwanted 0x form the binary so widht become 5
    for i in range(1, number + 1):
        d = str(i).rjust(width)               #rjust will adject the result to the width specified 
        o = oct(i)[2:].rjust(width)
        h = hex(i)[2:].upper().rjust(width)
        b = bin(i)[2:].rjust(width)
        print(f"{d} {o} {h} {b}")                 