DIR='C:/Users/G-ICT/norm'
FileNAME='sigma.spades.edit.fa'
name = DIR+'/'+FileNAME
file = open(name)

length = 0

contig_Name = []
contig_Length = []
for line in file:
    if(line[0] == '>'):
        line = line.split('\n')[0]
        contig_Name.append(line)
        contig_Length.append(length)
        length = 0
    else:
        length += len(line)

contig_Length.append(length)

print(contig_Length)
print(len(contig_Name))

outName = name + '.length'
out =open(outName, 'w')

for i in range(len(contig_Name)):
    out.write(contig_Name[i] + ' : ' + str(contig_Length[i+1]) + '\n')

out.close()