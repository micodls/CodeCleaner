# Convert to Unix line endings
s/\r//g

# Convert header includes to format #include "" (will be converted to format #include <> later)
/^#include </s/>/"/
s/#include </#include "/

# Convert tabs to 4 spaces and remove blank lines
s/\t/    /g
/./!d;

# Prepend std to standard types
/^ *string\|^string/ s/string /std::string /
/^ *map\|^map/ s/map/std::map/
/^ *vector\|^vector/ s/vector/std::vector/
/^ *list\|^list/ s/list/std::list/
/^ *shared_ptr\|^shared_ptr/ s/shared_ptr/std::shared_ptr/

# Insert a space between commas and characters
s/\(map\|vector\|list\|shared_ptr\)\+ </\1</g
s/,\([^ ,]*\)/, \1/

# Prepend std to standard types which are inside <>
/[a-z]</,/>/ s/\([, <]\)\+\(string\|map\|vector\|list\|shared_ptr\)\+\([,> <]\)/\1std::\2\3/g

# Insert spaces before and after mathematical operators
s/[=]\B/ = /g

# Convert >> to > >
/^ *std::\|^std::/ s/>\|> */> /g

# Remove tabs and spaces after open parentheses and before close parentheses
#s/\(.[^ ]*\) *(/\1(/g
s/ *(/(/
s/( *\([^ ]*\)/(\1/g
s/\([^ ]*\) *)/\1)/g
#s/(\([^ ]*\)[\n]*);/(...\1...);/g
#s/\([ \t\n]*([^ \t\n]*)[ \t\n]*\)/\(\1\)/g

# Insert spaces before and after comparator operators. Operators should NOT be inside a string.
# Insert a space between for/if and open parenthesis.
s/\(for\|if\)\+(/\1 (/
/for (\| if (/ s/\([^ ;]*\);\([^ ;]*\)/\1; \2/g
/for (\| if (/ s/\([^ =<>]\)\([=%/*]\)/\1 \2/g
/for (\| if (/ s/\([=%/*]\)\([^ =<>]\)/\1 \2/g
/for (\| if (/ s/\([a-z0-9]\)\(<=\|>=\)/\1 \2/g

# Convert postfix to prefix
s/\([[:alnum:]]*\)++/++\1/

# Remove space before ';' at the end of line
s/ *;$/;/g

s/\( *[^ ]*\) */\1 /g
s/ $//g

# Convert header includes to format #include <>
/^#include "/s/"/</
/^#include </s/"/>/