change_list = []
no_input = int(input("Enter num of gantries: "))
for i in range(no_input): 
    while True: 
        expressway = input("Enter name of gantry:")
        if expressway.isalpha() and len(expressway) < 20:
            old = float(input("Enter old rate:")) 
            new = float(input("Enter new rate:")) 
            change = new - old 
            if change > 0:
                change_list.append(expressway)
                print("Change is", change)          
            break
        else:
            print("Gantry must only contain letters and less than 20 characters. ") 
print("Changes list:", change_list)