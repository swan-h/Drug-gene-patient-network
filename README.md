Drug-gene-patient network

All the datasets are gathered from publicly available sources to construct the drug-gene-patient network. 




uniprotlinks.csv is downloaded from DrugBank, which shows all of DrugBank's drugs and their UniProt ID's targets. 

uniprot-all.tab is downloaded from UniProt to use for mapping UniProt ID's to corresponding gene symbols. 

HumanStringNet.txt is downloaded from https://github.com/phuongdao1/bewith

stringnetwork.csv is a csv file of the HumanStringNet.txt and include a tuple pairs of the interaction genes in a separate column. 

donor_therapy.BRCA-EU-r25.tsv is from ICGC, which shows the drug therapy received by BRCA donor patients. 

sorted_druglist1.csv is manually curated drug list of only known drug therapies of BRCA patients. 

mart_export.txt is downloaded from Ensembl to use for mapping Ensembl ID's (patients' mutations) to corresponding gene symbols.

ensembl.csv is a csv file of the mart_export.txt




Summer+project.ipynb includes all the codes and data I have used to create the drug-gene-patient network. 
		Created in jupyter notebook using python 3.6, Networkx package required. 
