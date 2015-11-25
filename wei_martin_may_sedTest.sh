#!/bin/bash

sed -i -e 's/\r//g' $1 | echo Changed line endings
sed -i -e 's/include "\(.*\)"/include <\1>/g' $1 | echo Corrected headers
sed -i -e '/^$/N;/^\n$/D' $1 | echo Removed extra blank lines
sed -i -e 's/[\t ]\{1,10\}$//g' $1 | echo Removed trailing tabs and spaces
sed -i -e '/(/{N;N;s/(\(.*\)\n\{2,3\}\t\{1,5\});/( \1 );/g}' $1 | echo Removed extra new lines inside parenthesis
sed -i -e 's/\(.\)[ \t]\{0,10\}([ \t]\{0,10\}\([^)n].*\))[ \t]\{0,10\}\([;$]\{0,1\}\)/\1(\2)\3/g' -e 's/[ \t]\{1,10\})/)/g' $1 | echo Fixed spacing inside parenthesis
sed -i -e '12,$s/string\([^_".]\)/std::string\1/g' -e '12,$s/\t\([mlc][aion].*[pt]\)/\tstd::\1/g' -e '12,$s/shared_ptr/std::shared_ptr/g' -e 's/endl/std::endl/g' $1 | echo Appended std to standard types
sed -i -e 's/\([;,]\)\([^ ]\)/\1 \2/g' $1 | echo Added space between commas and characters
sed -i -e '12,$s/\([^ ]\)\([=]\{1,2\}\)\([^ ]\)/\1 \2 \3/' $1 | echo Added space before and after =
sed -i -e '12,$s/[ ]</</g' -e '12,$s/>>/> >/g' $1 | echo Fixed spaces around brackets
sed -i -e 's/\(.\)\([+-]\{2\}\)/\2\1/g' $1 | echo Postfix to prefix
sed -i -e 's/[ ]\{0,2\}\([<=<]\{2\}\)[ ]\{0,2\}/ \1 /g' $1 | echo Fixedspacing around comparator operators
sed -i -e 's/\([\t ]\)\([fi][of].*\)[(]/\1\2 (/g' $1 | echo Fixed space after for and if
sed -i -e '/}$/{N;s/}\n$/}/}' -e '/^$/{N;s/\n\(\t\{1,5\}\)}/\1}/}' $1 | echo Fixed spacing between { and }
sed -i -e '/);$/{N;N;s/);\n\n\([\t][^/]\)/);\n\1/}' $1