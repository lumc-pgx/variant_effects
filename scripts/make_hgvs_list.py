import json

chr_id = snakemake.params.chr_id

with open(snakemake.input[0], 'r') as infile:
    alleles = json.load(infile)
    for allele in alleles:
        with open("{}/{}.txt".format(snakemake.params.prefix, allele["sequence_id"]), "w") as outfile:
            for v in allele["variants"]:
                print("{}:g.{}".format(chr_id, v), file=outfile)

