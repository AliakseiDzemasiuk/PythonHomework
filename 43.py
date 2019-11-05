def get_top_performers(file,number_of_top_students=5):
    with open(file) as filer:
        filer.readline()
        contents=[line[:-1].split(',') for line in filer]
    result=sorted(contents,key=lambda x: float(x[2]),reverse=True)[:number_of_top_students]
    return list(map(lambda x: x[0], result))


def age_sort(file):
    with open(file) as filer:
        columns=filer.readline()
        contents=[line[:-1].split(',') for line in filer]
    with open('sorted_students.csv','w') as filer:
        filer.write(columns)
        for item in sorted(contents,key=lambda x: int(x[1]),reverse=True):
            filer.write(','.join(column for column in item)+'\n')
    print('Sorted data is now stored in sorted_students.csv')



filename=input('Enter a file name: ')
print('Top performers are: '+str(get_top_performers(filename)))
age_sort(filename)






