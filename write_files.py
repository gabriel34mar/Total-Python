my_list=['Hello','world','here','I','am']
file=open(r'C:\Users\gabri\Documents\UMx\Carreras\Udemy\Total Python\Day 6\test1.txt','w')
file.write('''Hello
           world
           here i am\n''')
for w in my_list:
    file.writelines(w+'\n')
file.close()

