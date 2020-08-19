names = ("Roja", "Ram", "Sam", "Roja")
comps = ("Dell", "Apple", "MS", "Dell")

# zipped = list(zip(names,comps))
# zipped = set(zip(names,comps))
# zipped = dict(zip(names,comps))

zipped = zip(names, comps)

for (a, b) in zipped:
    print(a, b)
