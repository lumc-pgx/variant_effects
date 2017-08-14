include: "helper.snake"

PARAMS = VEPHelper(config, "Variant Effects")

onsuccess: PARAMS.onsuccess()
onerror: PARAMS.onerror()
    
# main workflow
localrules:
    all, link_source

rule all:
    input:
        PARAMS.outputs


include: "rules/link_sources.snake"
include: "rules/do_vep.snake"
