import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    x = 1000
    y = 9999
    dict_hash = dict()
    for i in range(x,y):
        i = str(i)
        number = i.strip()
        ha = hashlib.sha256(number.encode()).hexdigest()
        dict_hash[ha]=number

    file_out = open(output_file_name,'w')
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            f = dict_hash.get(row[1])
            out = name+ ','+ f + '\n'
            file_out.write(out)
    file_out.close()
