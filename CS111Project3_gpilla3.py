tax_dict = { 
'Pan troglodytes': 'Hominoidea',       'Pongo abelii': 'Hominoidea', 
'Hominoidea': 'Simiiformes',           'Simiiformes': 'Haplorrhini', 
'Tarsius tarsier': 'Tarsiiformes',     'Haplorrhini': 'Primates',
'Tarsiiformes': 'Haplorrhini',         'Loris tardigradus': 'Lorisidae',
'Lorisidae': 'Strepsirrhini',          'Strepsirrhini': 'Primates',
'Allocebus trichotis': 'Lemuriformes', 'Lemuriformes': 'Strepsirrhini',
'Galago alleni': 'Lorisiformes',       'Lorisiformes': 'Strepsirrhini',
'Galago moholi': 'Lorisiformes'
} 

yeast_dict = {
'Saccharomyces cerevisiae 101S' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae 228 CU-2' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae A364A' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae AWRI1631' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae AWRI796' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BMN1-35' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY2961' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY4741' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY4741-AV16' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY4741-AV8' : 'Saccharomyces cerevisiae', 
'Saccharomyces cerevisiae BY4741-BV19' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY4741-E18' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae BY4743' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae CAT-1' : 'Saccharomyces cerevisiae',
'Saccharomyces cerevisiae' : 'Saccharomyces',
'Saccharomyces' : 'Saccharomycetaceae',
'Kluyveromyces' : 'Saccharomycetaceae',
'Kluyveromyces marxianus' : 'Kluyveromyces',
'Kluyveromyces marxianus CBS 712' : 'Kluyveromyces marxianus',
'Kluyveromyces marxianus DMKU3-1042' : 'Kluyveromyces marxianus',
'Kluyveromyces marxianus var. bulgaricus' : 'Kluyveromyces marxianus',
'Kluyveromyces marxianus var. marxianus' : 'Kluyveromyces marxianus',
'Saccharomycetaceae' : 'Saccharomycetales',
'Saccharomycetales' : 'Saccharomycetes',
'Alloascoideaceae' : 'Saccharomycetales',
'Debaryomycetaceae' : 'Saccharomycetales',
'Nematodospora' : 'Saccharomycetales',
'Nematodospora valgi' : 'Nematodospora',
'Scheffersomyces' : 'Saccharomycetales',
'Scheffersomyces amazonensis' : 'Scheffersomyces',
'Scheffersomyces coipomoensis' : 'Scheffersomyces',
'Scheffersomyces cryptocercus' : 'Scheffersomyces',
'Scheffersomyces illinoinensis' : 'Scheffersomyces',
'Scheffersomyces insectosa' : 'Scheffersomyces',
'Scheffersomyces lignosus' : 'Scheffersomyces',
'Scheffersomyces parashehatae' : 'Scheffersomyces',
'Scheffersomyces quercinus' : 'Scheffersomyces',
'Scheffersomyces segobiensis' : 'Scheffersomyces',
'Scheffersomyces shehatae' : 'Scheffersomyces',
'Scheffersomyces spartinae' : 'Scheffersomyces',
'Scheffersomyces stipitis' : 'Scheffersomyces',
'Scheffersomyces virginianus' : 'Scheffersomyces',
'Saccharomycetes' : 'Saccharomycotina',
'Saccharomycotina' : 'saccharomyceta',
'unclassified Saccharomycotina' : 'Saccharomycotina',
'saccharomyceta' : 'Ascomycota',
'Pezizomycotina' : 'saccharomyceta',
'Ascomycota' : 'Dikarya',
'Taphrinomycotina' : 'Ascomycota',
'unclassified Ascomycota' : 'Ascomycota',
'Dikarya' : 'Fungi',
'Entorrhizomycota' : 'Dikarya',
'Basidiomycota' : 'Dikarya',
'Blastocladiomycota' : 'Fungi',
'Chytridiomycota' : 'Fungi',
'Cryptomycota' : 'Fungi',
'Microsporidia' : 'Fungi',
'Mucoromycota' : 'Fungi',
'Zoopagomycota' : 'Fungi',
'Fungi' : 'Opisthokonta',
'Aphelidea' : 'Opisthokonta',
'Choanoflagellida' : 'Opisthokonta',
'Metazoa' : 'Opisthokonta',
'Nucleariidae and Fonticula group' : 'Opisthokonta',
'Opisthokonta' : 'Eukaryota',
'Alveolata' : 'Eukaryota',
'Amoebozoa' : 'Eukaryota',
'Apusozoa' : 'Eukaryota',
'Cryptophyta' : 'Eukaryota',
'Euglenozoa' : 'Eukaryota',
'Haptophyceae' : 'Eukaryota',
'Jakobida' : 'Eukaryota',
'Eumetazoa' : 'Metazoa',
'Rhodophyta' : 'Eukaryota',
'Viridiplantae' : 'Eukaryota',
'Bilateria' : 'Eumetazoa',
'Deuterostomia' :'Bilateria',
'Chordata' : 'Deuterostomia',
'Craniata' : 'Chordata',
'Vertebrata' : 'Craniata',
'Gnathostomata' : 'Vertebrata',
'Teleostomi' : 'Gnathostomata',
'Euteleostomi' : 'Teleostomi',
'Sarcopterygii' : 'Euteleostomi',
'Dipnotetrapodomorpha' : 'Sarcopterygii',
'Tetrapoda' : 'Dipnotetrapodomorpha',
'Amniota' : 'Tetrapoda',
'Mammalia' : 'Amniota',
'Theria' : 'Mammalia',
'Eutheria' : 'Theria',
'Boreoeutheria' : 'Eutheria',
'Euarchontoglires' :'Boreoeutheria',
'Primates' : 'Euarchontoglires',
'Haplorrhini' : 'Primates',
'Simiiformes' : 'Haplorrhini',
'Catarrhini' : 'Simiiformes',
'Hominoidea' : 'Catarrhini',
'Hominidae' : 'Hominoidea',
'Homininae' : 'Hominidae',
'Homo' : 'Homininae',
'Homo sapiens' : 'Homo'
}

def list_ancestors(taxon, dictionary):
    '''Returns a list of ancestors for the taxon that is entered in'''
    
    answer = []
    answer.append(taxon)
    for i in range(len(dictionary)):
        answer.append(dictionary[taxon])
        taxon = dictionary[taxon]
        if taxon not in dictionary:
            break
    return answer

def root(dictionary):
    '''Returns the unique ancestrial taxon at the base of the entered in dictionary'''
    
    keys = dictionary.keys()
    values = dictionary.values()
    for taxa in values:
        if taxa not in keys:
            return taxa
        
def kids(taxon,dictionary):
    '''Returns a list of the offsprings produced by the inputed taxon in the correlated dictionary'''
    
    answer = [] 
    for key, value in dictionary.items():
        if taxon == value:
            answer.append(key)
    return answer

def common_ancestor(taxa_names, dictionary):
    '''Returns the closest common ancestor of the entered in list which can be empty or with taxons'''
    
    list0 = []
    if not taxa_names: # An empty list is returned if an empty list is the input for taxa_names
        return []
    for taxa in taxa_names:
        list0.append(list_ancestors(taxa, dictionary))
    for taxas in list0[0]:
        count = 0
        for x in range(0,len(list0)):
            for taxon in list0[x]:
                if taxon == taxas:
                    count += 1
                    if count == len(list0):
                        return taxas
                else:
                    continue 

def c_ancestor(taxa_names, dictionary):
    '''Returns the closest common ancestor of the entered in list which can be empty, have normal taxon names or abbreviated taxons names'''
    
    New_taxa = []
    for taxa in taxa_names:
        if '.' in taxa and taxa[0].isupper:
            for name in dictionary:
                if name[0] == taxa[0] and taxa[3:] in name:
                    New_taxa.append(name)
                    break
        else:
            New_taxa.append(taxa)
    return common_ancestor(New_taxa, dictionary)