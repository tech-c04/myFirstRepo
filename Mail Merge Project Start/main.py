#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file2:
    invite = file2.read()
    for name in names:
        final_letter = invite.replace("[name]", name)
        letter_file = open(f"letter_for_{name}.txt","w")
        letter_file.writelines(final_letter)

        