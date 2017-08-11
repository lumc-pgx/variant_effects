include: "helper.snake"

PARAMS = VEPHelper(config, "Variant Effects")

onsuccess: PARAMS.onsuccess()
onerror: PARAMS.onerror()
    
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
include: "rules/combine_vep.snake"


