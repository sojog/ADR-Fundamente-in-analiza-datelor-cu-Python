
def are_acces_v1(varsta, gen):
    if 18 < varsta < 70:
        return True
    elif varsta > 16 and gen == "f":
        return True
    else:
        return False

def are_acces_v2(varsta, gen):
    if (18 < varsta < 70)  or (varsta > 16 and gen == "f"):
        return True
    else:
        return False

    
V = 16
g = "m"

print("Are acces:", are_acces_v1(V, g))
print("Are acces:", are_acces_v2(V, g))

