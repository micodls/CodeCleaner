import re

fileToClean = open("main.cpp")
text = fileToClean.read()

#remove new lines before close parentheses.
text = re.sub(r'(?<!["])\(\s*(\S*)\s*\)(?!["])', r'(\1)', text)
text = re.sub(r'(?<!["])(\S*)\s*(\(.*\))[\t ]+(.*)(?!["])', r'\1\2\3', text)

#trim trailing tabs and spaces.
text = re.sub(r'(?<!["])[ \t]+\n(?!["])', r'\n', text, flags=re.M)

#remove excess new lines between two close braces.
text = re.sub(r'(?<!["])}\n+(\t*)(?=[}])(?!["])', r'}\n\1', text)

#remove excess new line.
text = re.sub(r'(?<!["])\n\n+(?!["])', r'\n\n', text)
text = re.sub(r'(?<!["]);\n+(\s*)}(?!["])', r';\n\1}', text)

#insert a space between commas and characters.
text = re.sub(r'(?<!["]),([\S])(?!["])', r', \1', text)

#prepend std to standard types. Make sure that the standard type name is NOT a variable name and NOT a string.
text = re.sub(r'(?<!["])(string[ ><,]|map[ <]|list[ <]|shared_ptr[ <]|cout |endl[ ;])(?!["])', r'std::\1', text)

#no spaces before open angle brackets and 1 space after close angle brackets.
text = re.sub(r'(?<!["])\s<([^\s<])(?!["])', r'<\1', text)
text = re.sub(r'(?<!["])>([\S])(?!["])', r'> \1', text)


#fix headers (format should be: #include <header here>).
text = re.sub(r'#include[ ]*[<"](.*)[>"]', r'#include <\1>', text)

#convert postfix to prefix.
text = re.sub(r'(?<!["])([\w]*)(\+\+|\-\-)(?!["])', r'\2\1', text)

#remove tabs and spaces after open parentheses and before close parentheses.
text = re.sub(r'\([\s\t]*(.*)[\s\t]*\)', r'(\1)', text)
text = re.sub(r'[\s\t]{1,}\((.*)\)[\s\t]{1,}', r'(\1)', text)

#insert a space between for/if and open parenthesis.
text = re.sub(r'for\(', r'for (', text)
text = re.sub(r'if\(', r'if (', text)

#convert windows line endings to unix line endings.
text = re.sub('\r\n', '\n', text)

#insert spaces before and after mathematical operators. Operators should NOT be inside a string.
text = re.sub(r'(?<!["])((?<!["]){1,}((?<![+\-=<>])[+\-=]{1}(?![+\-+]))(?=["]){1})', r' \2 ', text)

# insert spaces before and after comparator operators. Operators should NOT be inside a string.
text = re.sub(r'(?<!["])(\S*)([=<>]=)(\S*)(?!["])', r'\1 \2 \3', text)

fileToClean.close()

fileToWrite = open('newMain.cpp', 'w')
fileToWrite.write(text)

fileToWrite.close()

print(text)