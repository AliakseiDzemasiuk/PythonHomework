def execute(file, fileo):
    writo(retrieve(file),fileo)  

def retrieve(file):
    fil=open(file,'r')
    res=sorted([line[:-1] for line in fil])
    fil.close()
    return res

def writo(data,file):
    fil=open(file,'w')
    for string in data:
        fil.write(string+'\n')
    fil.close()
    return

execute('unsorted_names.txt','sorted_names.txt')
