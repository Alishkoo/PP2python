import re

text = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"

result = re.split("/", text) #сплитает и засовывает в массив 
result1 = re.match("DC" , text) # ищет именно в начале 
result2 = re.search("DC", text) # ищет по всему но выводит первый найденный
result3 = re.findall("DC" , text) # засовывает все найденное в массив 
result4 = re.sub("AC", "MR" , text) # заменяет АС на MR 
result5 = re.fullmatch("AC/DCAC/DCAC", text) # совпадает ли полностью?




print(result)
print(result1)
print(result2[0])
print(result3)
print(result4)
print(result5)

