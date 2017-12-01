import json
import os
import subprocess
import sys
import locus_processing

# a simple lookup for get a correct assembly identifier
def assembly_version(version):
    return {
            "hg19": "GRCh37",
            "hg38": "GRCh38"
        }.get(version, version)

locus = locus_processing.load_locus_yaml(snakemake.input.locus)
chr_id = locus.chromosome.accession

environment = os.environ.copy()
environment["PERL5LIB"] = "" 

vep_command = [
    "vep", 
    "--cache",
    "--dir_cache", snakemake.config["STAGE_PARAMS"]["VARIANT_EFFECT"]["vep_cache_dir"],
    "--cache_version", str(snakemake.config["STAGE_PARAMS"]["VARIANT_EFFECT"]["vep_cache_version"]),
    "--assembly", assembly_version(locus.reference),
    "--format", "hgvs",
    "--refseq",
    "--force_overwrite",
    "--check_existing",
    "--everything",
    "--no_stats",
    "--transcript_filter", "stable_id match {}".format(locus.transcript),
    "--json",
    "-o", "STDOUT"
]

results = []

with open(snakemake.input.variants, 'r') as infile, open(snakemake.output[0], "w") as outfile:
    alleles = json.load(infile)
    for allele in alleles:
        
        if snakemake.config.get("STAGE_PARAMS", {}).get("VARIANT_EFFECT", {}).get("ignoreBoundary", False):
            variants = allele["variants"][1:-1]
        else:
            variants = allele["variants"]
        
        variant_string = "\n".join(["{}:g.{}".format(chr_id, v["g_notation"]) for v in variants])
        
        vep_process = subprocess.Popen(vep_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=environment)
        (out, err) = vep_process.communicate(variant_string.encode("utf-8"))
        
        if err is not None:
            raise RuntimeError(err)
            
        def result_lines(result):
            for line in result.decode("utf-8").split("\n"):
                line = line.strip()
                if len(line) > 0:
                    yield json.loads(line)
        
        result = {
            "sequence_id": allele["sequence_id"],
            "vep": [r for r in result_lines(out)]
        }
        
        results.append(result)

    print(json.dumps(results, indent=4, separators=(',', ': ')), file=outfile)
        
