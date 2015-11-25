import re

cppPathAndFileName = "main.cpp"



### reading the contents of the file to a variable(asciiFileContents)
with open(cppPathAndFileName , 'r') as fileContents:
    asciiFileContents = fileContents.read()

### finding and replacing the wrong syntax, and changes saved in the variable(newAsciiFileContents)

# fix headers (format should be: #include <header here>)
newAsciiFileContents = re.sub(r'#include "([a-zA-Z]+)"', r'#include <\1>', asciiFileContents)

# trim trailing tabs and spaces.
newAsciiFileContents = re.sub(r'(.)[ \t]*$', r'\1$', newAsciiFileContents)

# remove excess new line.
newAsciiFileContents = re.sub(r'\n{3,}', r'\n', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(;)\n(\t+)(\/\/.*)', r'\1\n\n\2\3', newAsciiFileContents)

# prepend std to standard types. Make sure that the standard type name is NOT a variable name and NOT a string.
newAsciiFileContents = re.sub(r'\b(string|cin|cout|list|shared_ptr)\b', r'std::\1', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(std::)+', r'std::', newAsciiFileContents)
newAsciiFileContents = re.sub(r'"(.*)std::(string|cin|cout)(.*)"', r'"\1\2\3"', newAsciiFileContents)
newAsciiFileContents = re.sub(r'/(.*)std::(string|cin|cout)(.*)', r'/\1\2\3', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(#include []"|<])std::(string|list)', r'\1\2', newAsciiFileContents)

# insert spaces between commas and characters that are inside <> [] ()
newAsciiFileContents = re.sub(r'(.),(.)', r'\1, \2', newAsciiFileContents)

# insert spaces before and after mathematical operators. Operators should NOT be inside a string.
newAsciiFileContents = re.sub(r'([^=|^\s|^\/])([=|\+|\-|\*|\/|%][^=].*)', r'\1 \2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(\s[=|\+q|\-|\*|\/|%])([^\s|^\/|^\+|^\-].*)', r'\1 \2', newAsciiFileContents)

# no spaces before open angle brackets and 1 space after close angle brackets.
# covert >> to > >.
newAsciiFileContents = re.sub(r'(\w|\d)\s(<)', r'\1\2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'#include<', r'#include <', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(cin|cout)(<<)', r'\1 \2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'([]\w|\d][^\s])(>)(>)', r'\1\2 \3', newAsciiFileContents)

# remove tabs and spaces after open parentheses and before close parentheses.
# remove new lines before close parentheses.
newAsciiFileContents = re.sub(r'(\()[\t|\s]+(.)', r'\1\2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(.)[\t|\s]+(\()', r'\1\2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(.)[\t|\s]+(\))', r'\1\2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(\))[\t|\s]+(.)', r'\1\2', newAsciiFileContents)

# convert postfix to prefix.
newAsciiFileContents = re.sub(r'(.)(\+\+|\-\-)', r'\2\1', newAsciiFileContents)
newAsciiFileContents = re.sub(r'\n{2,}\}', r'\n}', newAsciiFileContents)

# insert spaces before and after comparator operators. Operators should NOT be inside a string.
newAsciiFileContents = re.sub(r'(.)(==|<=|>=|\+\+|\-\-)', r'\1 \2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(<<.*)\s(==|<=|>=|\+\+|\-\-)', r'\1\2', newAsciiFileContents)
newAsciiFileContents = re.sub(r'(==|<=|>=)(.)', r'\1 \2', newAsciiFileContents)

# insert a space between for/if and open parenthesis.
newAsciiFileContents = re.sub(r'(for|if)(\()', r'\1 \2', newAsciiFileContents)

### save the changes made in the variable to the new file
with open('main-fixed.cpp', 'w') as output:
    output.write(newAsciiFileContents)