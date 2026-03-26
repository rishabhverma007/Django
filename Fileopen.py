#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","r") as file:
#    data = file.read()
#    print(data)

#WRITE OPERATION
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","w") as file:
#    file.write("This is a new line of text.\n")
#    file.write("This is another line of text.\n")

#APPEND OPREATION
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","a") as file:
#    file.write("This line is appended to the file.\n")

#FILE HANDLING
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","w") as file:
#    file.write("Amit,20,Delhi")
#    file.write("\nNeha,22,Mumbai")
#    file.write("\nRahul,19,Bangalore")
#    file.write("\nPriya,21,Chennai")
#1
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","r") as file:
#    data = file.read()
#    print(data)
#2
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","r") as file:
#    lines = file.readlines()
#    print(lines)
#3
#with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","r") as file:
#    for i in lines:
#        print(i)

#4
with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","w") as file:
    file.write("\nRITESH,21,LUCKNOW")
    file.write("\nPRANJAL,21,LUCKNOW")
    file.write("\nRISHABH,21,Barabanki")

with open(r"C:\Users\risha\OneDrive\Desktop\DATA.txt","a") as file:
    file.write("\nPRIYANSHU,21,LUCKNOW")

