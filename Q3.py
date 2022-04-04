

def match(module):
    match module:
        case "CSC1006":
            return "Mathematics 2"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return"Data Structures and Algorithms"
        case "CSC1009":
            return ("Object Oriented Programming");
        case "CSC1010":
            return "Computer Networks"
        case _:
            return "Unknown Module code"

print(match("CSC1009"))

for i in range(102,65,-1):
    print(i)
