"""file= open("demo.txt", "w")
 # file.write("Demo line")
file.writelines(["Demo line 01 \n",
                 "Demo line 02 \n",
                 "Demo line 03 \n"])

file.close() """


#~~~+++~~~#


with open(r"H:\My Drive\PythonFCC\demo.txt", "w") as file:
 # file.write("Demo line")
    file.writelines(["Demo line 01 \n",
                 "Demo line 02 \n",
                 "Demo line 03 \n"])

