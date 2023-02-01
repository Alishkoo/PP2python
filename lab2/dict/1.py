thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(len(thisdict))
x = thisdict.get("brand")
print(x)
y = thisdict.keys()
print(y)
print(thisdict.values())