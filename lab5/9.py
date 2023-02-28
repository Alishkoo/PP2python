import re

def insert_spaces(string):
    
    pattern = r'(?<!^)(?=[A-Z])'
  
    result = re.sub(pattern, ' ', string)
    return result


input_string = "HelloWorldThisIsAStringWithNoSpaces"
output_string = insert_spaces(input_string)
print(output_string)