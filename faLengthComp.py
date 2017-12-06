DIR='C:/Users/G-ICT/norm/'
file1= 'sigma.masurca.pilon.fa.length'
file2= 'sigma.masurca.edit.fa.length'

file1 = DIR + file1
file2 = DIR + file2

len1 = open(file1)
len2 = open(file2)

len1 = len1.readlines()
len2 = len2.readlines()


same = 0

for i in range(len(len1)):
    same = 0
    for j in range(len(len2)):
        pilon =len1[i].split(' ')[0]

        edit = len2[j].split(' ')[0]
        if ( pilon == edit ):
            if(len1[i] == len2[j]):
                same = 1
            break

    if(same == 0):
        print(len1[i] , " : ", len2[j])


