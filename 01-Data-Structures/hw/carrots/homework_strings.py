""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""


# read the file dna.fasta
with open('./files/dna.fasta', 'r+') as dna_fasta:
    dna_dict = {}
    for dna_str in dna_fasta:
        if dna_str.startswith('>'):
            dna_key = dna_str.strip()
            dna_dict[dna_key] = []
        else:
            dna_dict[dna_key].append(dna_str.strip())


# read the file rna_codon_table.txt
with open('./files/rna_codon_table.txt', 'r+') as rna_codon_table:
    rna_codon_table = rna_codon_table.read().split()


def translate_from_dna_to_rna(dna):
    translation = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna = {}

    for key in dna:
        rna[key] = []
        for string in dna[key]:
            rna[key].append(f"{''.join(translation[i] for i in string)}")
    
    return rna


file1 = translate_from_dna_to_rna(dna_dict)
with open('translate_from_dna_to_rna.json', 'tw', encoding='utf-8') as f:
    f.write('[')
    for key in file1:
        f.write(f'{{"{str(key)}": "{str(file1[key]).strip("[").strip("]")}}}",\n')
    size = f.tell()
    f.truncate(size - 2)
    f.write(']')


def count_nucleotides(dna):
    num_of_nucleotides = ''

    for key in dna:
        num_of_nucleotides += f"{key}\n"
        value = ''
        for string in dna[key]:
            value += string
        num_of_nucleotides += f"[A - {value.count('A')}, C - {value.count('C')}, " \
                              f"G - {value.count('G')}, T - {value.count('T')}]\n"

    return num_of_nucleotides


file2 = count_nucleotides(dna_dict)
with open('count_nucleotides.txt', 'tw', encoding='utf-8') as f:
    for line in file2.split('\n'):
        f.write(line + '\n')


def translate_rna_to_protein(rna):
    protein = {}
    codon = dict(zip(rna_codon_table[::2], rna_codon_table[1::2]))

    for key in rna:
        protein_key = key
        protein[protein_key] = []
        for string in rna[key]:
            string = [string[i:i + 3] for i in range(0, len(string), 3)]
            for i in string:
                if len(i) == 3:
                    protein[protein_key] += codon[i]
                    protein[protein_key] = ''.join(protein[key])

    return protein


file3 = translate_rna_to_protein(translate_from_dna_to_rna(dna_dict))
with open('translate_rna_to_protein.json', 'tw', encoding='utf-8') as f:
    f.write('[')
    for key in file3:
        f.write(f'{{"{str(key)}": "{str(file3[key])}}}",\n')
    size = f.tell()
    f.truncate(size - 2)
    f.write(']')
