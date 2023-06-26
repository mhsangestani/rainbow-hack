import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    # Defining two variables for our range
    x = 1000
    y = 9999
    
    # Creating an empty dictionary to store our hashes as keys and their respective passwords as values
    dict_hash = dict()
    
    # Looping through the range from x to y
    for i in range(x,y):
        # Converting each number to a string for hashing purposes
        i = str(i)
        number = i.strip()
        
        # Hashing each number using SHA-256 and storing it in our dictionary with the number as its value
        ha = hashlib.sha256(number.encode()).hexdigest()
        dict_hash[ha]=number

    # Opening a file for writing
    file_out = open(output_file_name,'w')
    
    # Opening the input file for reading
    with open(input_file_name) as f:
        reader = csv.reader(f)
        # Looping through each row in the CSV file
        for row in reader:
            name = row[0]
            # Retrieving the password from our dictionary based on the hashed value in the CSV file
            f = dict_hash.get(row[1])
            # Creating a string to write to our output file
            out = name+ ','+ f + '\n'
            # Writing the output string to our file
            file_out.write(out)
            
    # Closing the output file
    file_out.close()
