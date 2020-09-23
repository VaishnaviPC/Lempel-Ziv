# Introduction:

The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm. LZW is an adaptive compression algorithm that does not assume prior knowledge of the input data distribution. This algorithm works well when the input data is sufficiently large and there is redundancy in the data. The algorithm is simple to implement and has the potential for very high throughput in hardware implementations.

# Application of LZW

1. GIF and TIFF files
2. Adobe Acrobat Softwaare

# Two steps followed in LZW Algorithm
1. Encoding
2. Decoding

# LZW Algorithm
### Input File --> encoded File --> decoded File
In First step encoding is done by encoder.py to get encoded file
In Second step, the encoded file is decoded to original text using decoder.py


#### Pseudocode of Encoding

~~~
MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
initialize TABLE[0 to 255] = code for individual characters
STRING = null
while there are still input symbols:
SYMBOL = get input symbol
if STRING + SYMBOL is in TABLE:
STRING = STRING + SYMBOL
else:
output the code for STRING
If TABLE.size < MAX_TABLE_SIZE: // if table is not full
add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
STRING = SYMBOL
output the code for STRING
~~~

#### Pseudocode of Decoding

~~~
MAX_TABLE_SIZE=2(bit_length)
initialize TABLE[0 to 255] = code for individual characters
CODE = read next code from encoder
STRING = TABLE[CODE]
output STRING
while there are still codes to receive:
CODE = read next code from encoder
if TABLE[CODE] is not defined: // needed because sometimes the
NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
else:
NEW_STRING = TABLE[CODE]
output NEW_STRING
if TABLE.size < MAX_TABLE_SIZE:
add STRING + NEW_STRING[0] to TABLE
STRING = NEW_STRING
~~~

# Program Description
Programming Language : Python version 3
It can be run in any python3 environment.

~~~
InputfileName - The file to be compresssed
Bitlength - The length to be used
~~~

##### Command to run python program
~~~
python filename.py InputfileName Bitlength
~~~

# Data Structure
HashMap data structure- a dictionary has been used to implement the algorithm. In Python, the Dictionary data types represent the implementation of hash tables. It contains the key value pairs where ASCII characters act as KEY and with ascii value acts as its VALUE for encoding and vice versa in the case of decoding function.

# Syntax:
dict = {key1:value1, key2:value2, ... }. In this case a for loop is used for 256 ascii range. 
Sample below 
table_dict = dict((chr(i), i) for i in range(256))

# encoder.py
~~~
The Encoder class uses dictionary and follows the Pseudocode of Encoding to encode the input file. Here, In dict hashmap ASCII Value is the VALUE and ASCII Character is the KEY.
~~~
# decoder.py
~~~
The Decoder class uses dictionary in opposite fashion, where ASCII Value is the KEY and ASCII Character is the VALUE. It follows the Pseudocode of Decoding to decode the encoded text.
~~~

# Note

1. For encoding, encoder.py file is used. It will generate encoded "lzw" file.
2. For decoding the encoded "lzw" file, decoder.py is used. It is used to generate the decoded text file. The content of it will be same as the initial input file.
3. The encoding file is created and the value is stored in 16-bit format.

#what fails?
The program works when the input is given in only one line and doesnt work when the input string is given in multiple lines 

# What does the encoder and decoder program do?
The encoder program generates the encoded file in a 16bit format. The decoder program converts the generated encoded file back to the original input file. It handles null files and we can observe that large file size after encoding is reduced to smaller size file.


# References:
1. https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch 
2. www.asciitable.com
3.Stack overflow 
