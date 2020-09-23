#VaishnaviPoondiChinnappaNarayanan
#Importing modules 
import os
import sys
import struct

class Decoder:
    def decode(self, input_string, input_length):
        '''The Decoder class uses dictionary in opposite fashion, where ASCII Value is the KEY and ASCII Character is the VALUE. It follows the Pseudocode of Decoding to decode the encoded text. 
           :param input_string: byte string read lzw file
           :input_length: This is bit length defining number of encoding bits
        '''
        enc_list = [int.from_bytes(input_string[i:i+2], 'big') for i in range(0, len(input_string), 2)]
        '''Every two bytes are converted to big endian
        '''

        if int(input_length) > 16:
            raise ValueError("Input Bit Length should be less than 16")
        MAX_TABLE_SIZE = pow(2, int(input_length))
        max_ascii = 256
        table_dict = dict((i, chr(i)) for i in range(256))
        result = ""
        dec_string = chr(enc_list.pop(0))
        result = result + dec_string
        # print(dec_string)
        for code in enc_list:
            if code in table_dict:
                new_dec_string = table_dict[code]
            elif code >= max_ascii:
                new_dec_string = dec_string + dec_string[0]
            result = result + new_dec_string
            # print(new_dec_string)
            if len(table_dict) < MAX_TABLE_SIZE:
                table_dict[max_ascii] = dec_string + new_dec_string[0]
                max_ascii = max_ascii + 1
            dec_string = new_dec_string
        # print(result)
        return result
         
    '''The output function opens and writes the decoded output in the decoded text file. 
    :param result: decoded string
    :param filename: input file name
    '''
    def output(self, result, filename):
        with open('{}_decoded.txt'.format(filename.split('.')[0]), 'w') as f:
            f.write(result)

    def main(self):
        '''Main method for class decoder calls decoder method and outputs decoded text in a text file(inputfilename_decoded.txt)
        '''
        args = sys.argv[1:]
        filename, bitlength = args[0], args[1]

        encoded_file = open(filename, "rb")
        encoded_values = encoded_file.readline()
        # print(input_values, args.bitlength)
        result = self.decode(encoded_values, bitlength)
        self.output(result, filename)


if __name__ == '__main__':
    decoder = Decoder()
    decoder.main()
