import yaml

include: "helper.snake"

PARAMS = VEPHelper(config, "Variant Effects")

onsuccess: PARAMS.onsuccess()
onerror: PARAMS.onerror()


with open(config["GENE"], "r") as infile:
    gene = yaml.safe_load(infile)

    
# main workflow
localrules:
    all, link_source, combine

rule all:
    input:
        PARAMS.outputs


include: "rules/link_sources.snake"
include: "rules/list_hgvs.snake"
include: "rules/run_vep.snake"
include: "rules/filter_vep.snake"


rule combine:
    input:
        dynamic("variant_effect/filtered_vep/{barcode}/{allele}.txt")
    output:
        "variant_effect/combined/{barcode}.txt"
    shell:
        "cat {input} > {output}"
