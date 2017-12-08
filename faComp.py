file1 = 'E:/YEAST/vcf/w303.masurca.pilon.fa'
file2 = 'E:/YEAST/vcf/w303.masurca.edit.fa'
out = './compare.txt'

fasta1 = open(file1,'r')
fasta2 = open(file2, 'r')
outFile = open(out, 'w')


pos = 0

faLine1Len = -1
faLine2Len = -1
seq1_idx = 0
seq2_idx = 0
scaffold1 = ''
scaffold2 = ''

f1idx = -1
f2idx = -1

while(True):

    while(seq1_idx < faLine1Len and seq2_idx < faLine2Len):
        seq1 = faLine1[seq1_idx]
        seq2 = faLine2[seq2_idx]

        seq1_idx += 1
        seq2_idx += 1
        pos += 1
        if(seq1 != seq2):
            tmp = scaffold1 + '\t' + str(pos) + '\t' + seq1 + '\t' + seq2 + '\n'
            outFile.write(tmp)

    if(seq1_idx >= faLine1Len):
        while (True):
            if(f1idx != fasta1.tell()):
                f1idx = fasta1.tell()
            else:
                break
            faLine1 = fasta1.readline().strip()
            if(faLine1 != ''): break


        if(faLine1[0] == '>'):
            scaffold1 = faLine1
            print(scaffold1)
            pos = 0
            faLine1 = fasta1.readline().strip()

        faLine1Len = len(faLine1)
        seq1_idx = 0

    if(seq2_idx >= faLine2Len):
        while (True):
            if(f2idx != fasta2.tell()):
                f2idx = fasta2.tell()
            else:
                break
            faLine2 = fasta2.readline().strip()
            if(faLine2 != ''): break

        if(faLine2[0] == '>'):
            scaffold2 = faLine2
            faLine2 = fasta2.readline().strip()

        faLine2Len = len(faLine2)
        seq2_idx = 0


outFile.close()