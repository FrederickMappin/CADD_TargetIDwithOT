# Target Identification with OpenTarget CLI
Target identification is a critical first step in Computer-Aided Drug Design (CADD), where the goal is to determine the biological molecules—typically proteins—that play a key role in a disease process. By identifying and validating these targets, researchers can focus drug discovery efforts more effectively, increasing the chances of developing successful therapeutics.Open Targets is a collaborative platform that integrates data from genomics, transcriptomics, clinical studies, and other sources to help researchers systematically identify and prioritize potential drug targets. It provides a robust, data-driven framework to explore the association between targets and diseases, making it a valuable resource for early-stage drug discovery.


## Usage 
Investigate a Ensembl gene ID (ENSG00000134086) for gene or Experimental Factor Ontology(EFO_0000349) for diseases.

```python -m opentarget --help``` 
```
Usage: python -m opentarget <ID> <request_type>

Examples:
  python -m opentarget EFO_0005952 target_disease_evidence
  python -m opentarget EFO_0000349 associated_targets
  python -m opentarget ENSG00000134086 associated_diseases

Valid request types and their descriptions:
  associated_targets: Find targets associated with a specific disease or phenotype
  associated_diseases: Find diseases and phenotypes associated with a specific target
  target_disease_evidence: Explore evidence that supports a specific target-disease association
```

## Project Portion Section 
In this section, I demonstrate the practical application of the tool within a real-world project scenario.

### Objective 
 Utilize the OpenTargets CLI to perform target identification and disease association analysis using curated biological datasets. Our focus is on demonstrating how the OpenTargets platform can be employed programmatically to retrieve relevant information about genes and diseases, a critical step in streamlining early-stage drug discovery.
### Methodology


### Expected Outcome



