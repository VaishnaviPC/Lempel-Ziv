#VaishnaviPoondiChinnappaNarayanan
#Importing modules 
import sys
import struct


class Encoder:
    def encode(self, input_string, input_length):
        '''The Encoder class uses dictionary and follows the Pseudocode of Encoding to encode the input file.
           :param input_string: This defines the string thats given in the input text which gets encoded in this function
           :param input_length: This is bit length defining number of encoding bits
           :result: lists the ascii values of the processed string
        '''
        if int(input_length) > 16:
            raise ValueError("Input Bit Length should be less than 16")
        MAX_TABLE_SIZE = pow(2, int(input_length))
        max_ascii = 256
        table_dict = dict((chr(i), i) for i in range(256))
        output_str = ""
        result = []
        for c in input_string:
            temp_str = output_str + c
            # print(temp_str)
            if temp_str in table_dict:
                output_str = temp_str
            else:
                if output_str:
                    ascii_val = table_dict[output_str]
                    result.append(ascii_val)
                    # print(ascii_val, output_str)
                if len(table_dict) < MAX_TABLE_SIZE:
                    table_dict[temp_str] = max_ascii
                    max_ascii = max_ascii+1
                output_str = c
        result.append(table_dict[output_str])
        # print(table_dict[output_str], output_str)
        return result

    def output(self, result, filename):
        '''The output function creates file with lzw.extention with input name as filename. It goes through struct module where >h denotes the conversion of ascii code into shortint(2bytes/16 bits). 
           :param result: list of string ascii values output from the encode function
           :param filename: parameter for input file
        '''
        with open('{}.lzw'.format(filename.split('.')[0]), 'wb') as f:
            for i in range(len(result)):
                f.write(struct.pack(">h", int(result[i])))

    def main(self):
        '''Main method for class encoder calls encoder method and outputs encoded text in a file with lzw extention
        '''

        args = sys.argv[1:]
        filename, bitlength = args[0], args[1]
        input_file = open(filename, "r")
        input_values = input_file.readline()
        # print(input_values, args.bitlength)
        result = self.encode(input_values, bitlength)
        self.output(result, filename)


if __name__ == '__main__':
    encoder = Encoder()
    encoder.main()
