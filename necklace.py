same_necklace = "abcabcabc"
same_necklace2 = "abcabcabc"
def figureout():
    if same_necklace == same_necklace2:
        print("Same necklace")
    else:
        shiftedNecklace = same_necklace
        for x in same_necklace:
            if shiftedNecklace == same_necklace2:
                print("This is the same necklace")
            break
        else:
            shiftedNecklace = (shiftedNecklace[len(shiftedNecklace)-1:len(shiftedNecklace):]+(shiftedNecklace[0:len(shiftedNecklace)-1]))

print("I should've took CIS 255 and made a spinning wheel")

figureout()
def counter():
    counted = 0
    shiftedNecklace = same_necklace
    for x in same_necklace:
            shiftedNecklace = (shiftedNecklace[len(shiftedNecklace)-1:len(shiftedNecklace):]+(shiftedNecklace[0:len(shiftedNecklace)-1]))
    if same_necklace == shiftedNecklace:
                counted = counted + 1
    print(counted)
counter()