def compile_program(filename, assembly_list):
    if filename[:2] == '.\\':
        filename = filename[2:]
        
    program_name = filename.split('.')[0]
    
    with open(program_name+'.s','w') as file:
        for line in assembly_list:
            file.write(line + '\n')
    print(f"Assembly code written to {program_name}.s")
    