#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        

with open("day 024/mail merge/Input/Names/invited_names.txt") as names:
    for name in names:
        person = name.strip()
        # Read in the file
        with open('day 024/mail merge/Input/Letters/starting_letter.txt', 'r') as starting_letter:
            filedata = starting_letter.read()

        # Replace the target string
        filedata = filedata.replace('[name]', person)
        

        # Write the file out again
        with open(f'day 024/mail merge/Output/ReadyToSend/letter_for_{person}.txt', 'w') as file:
            file.write(filedata)
        
        
