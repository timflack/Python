"""
Script showing examples of using regular expressions in python using re module

Regular expressions allow us to search and match patterns of text
"""
import re

# create a multiline text string to perform regular expressions on
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

02920-555-555
01745.649.861

Dr. Flack
Dr Wenzel
Mrs Thorburn
Miss Flack
Mr. T

cat 
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# Patterns to search for can be made using the compile method
pattern = re.compile(r'abc')

# can then search for matches and return an iterable using finditer
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# can see from above code, 1 match which spans index 1 to 4
print(text_to_search[1:4])

# if you're going to match special character they need to be escaped with a \
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'google\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

"""
Special character matches
.       - Any character except new line
\d      - Digit (0-9)
\D      - Not a digit (0-9)
\w      - Word character (a-z, A-Z, 0-9, _)
\W      - Not a word character
\s      - Whitespace (space, tab, newline)
\S      - Not a Whitespace

These are anchors and access invisible positions before and after characters
\b      - Word boundary
\B      - Not a word boundary
^       - Beginning of a string
$       - End of a string

[]      - character set (match more than one character in one position)
()      - Match a group
|       - Or operator within group
Quantifiers
*       - 0 or more
+       - 1 or more
?       - 0 or one
{3}     - Exact number
{3,4}   - Range of numbers {min, max}
"""

pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Will only match if the string is at the start of the sentence
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# Will only match if the string is at the end of the sentence
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# Regex to match phone numbers in 5-3-3 pattern
# Will only match if the string is at the start of the sentence
pattern = re.compile(r'\d\d\d\d\d[-.]\d\d\d[-.]\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Matches everthing not in the character set
pattern = re.compile(r'[^a-zA-z]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Match all 3-letter words ending in 'at' except for bat
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Can us quantifiers to match more than one character at once
pattern = re.compile(r'\d{4}[-.]\d{3}[-.]\d{3}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Pattern to match all name prefixes and the corresponding name
pattern = re.compile(r'[DM](r|rs|iss)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

urls = """
https://www.google.com
http://coreyms.com
https://www.nasa.gov
https://youtube.com
"""

# pattern to match URls
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

# can access groups
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))

# can sub the groups
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

"""
Other methods other than finditer
.findall    - matches all and creates list of strings
.match      - returns first match if its at start
.search     - search entire string and return first match
"""

# Using flags
pattern = re.compile(r'start', re.IGNORECASE)
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# Look up more flags
