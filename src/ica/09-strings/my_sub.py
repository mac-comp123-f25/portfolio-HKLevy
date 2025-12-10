def name_subst(name,text):
    new_text=text.replace('ZZZ',name)
    return new_text

sallie = name_subst("Sallie","My friend, ZZZ, won an award")
print(sallie)

print(name_subst("Fred","Jamie and ZZZ flew over the trees."))
print(name_subst("John","testing this"))