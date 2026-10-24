# 03. ek function banao jo list ke numbers ka average return kare:

def calc_average(lst):
    return sum(lst) / len(lst) if lst else 0
print(calc_average([5, 10, 20, 25, 30]))