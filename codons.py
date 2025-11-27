def create_codon_dict(file_path):
    codons_dic = {}
    file = open(file_path)
    rows = file.readlines()
    file.close()
    for row in rows:
        row = row.strip()
        cells = row.split("\t")
        codons_dic.update({cells[0]:cells[2]})
    return codons_dic


