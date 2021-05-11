input_dir = 'input/'
output_lex = 'lexical_output/'
output_synt = 'syntactic_output/'
output_dir = 'output/'
files_read = 0
files_written = 0

for filename in os.listdir(input_dir):
    if filename.startswith('entrada'):
        file_num = filename.split('.')[0][7:]

        with open(f'{input_dir}{filename}', 'r') as fin:
            file_string = fin.read()
            current_position = 0 #TODO Put these in correct python global variables patterns
            line = 1
            tokens = []
            errors = 0

            while(current_position < len(file_string)):
                next_token(file_string[current_position:])
        if errors == 0:
            print(f"File {filename} read without errors")
        else:
            print(f"Found {errors} errors in {filename}")
        files_read += 1

        with open(f'{output_dir}saida{file_num}.txt', 'w') as fout:
            for token in tokens:
                fout.write(token)
        files_written += 1

print(f"Read {files_read} files\
 \nWrote {files_written} files")
