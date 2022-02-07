#get args
    args = get_args()
    rna = args.rna.upper()

    
    codon_to_aa = codon_dict
    k_mers = sublists(rna,3)

    sc = SparkContext.getOrCreate()
    rna_par = sc.parallelize(k_mers)
    trans = ''.join(rna_par.map(lambda codon: codon_to_aa.get(codon, '-')).collect())
    print(trans.partition('*')[0])