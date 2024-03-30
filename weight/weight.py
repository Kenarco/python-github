weight = int(input("Enter weight: "))
unit = input("l(b) ot k(g): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


