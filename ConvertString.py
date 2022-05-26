with open('insertSQL.txt') as file_object:
    for line in file_object:
        line = line.rstrip()
        line += ';'
        with open('result.txt', 'a') as f:
            f.write(line)
            f.write('\n')
        print(line)
    #contents = file_object.read();
#print(contents)
