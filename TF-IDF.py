path = r'C:\Users\muham\PycharmProjects\stopwords\Preprocess Data\P-Acta Informatica.csv'
f = open(path, "r")
line = f.readline()
DF = {}

print(f)
while line:
    print (line)
    for i in line:
        tokens = i
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}

f.close()