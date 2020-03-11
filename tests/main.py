#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:58:31 2020

@author: marc
"""


#On cherche à créer un programme tel qu'il remplira automatiquement les champs
#d'un document LaTeX type Lettre de Motivation

#On définit d'abord :
#- Le programme qui génèrera des parties grammaticalement correctes
#- Un générateur de skills suivant ce que la personne dispose et souhaite faire
#apparaître

#Cela passe par la création de différents niveaux de priorité et d'automatisation
#-- Automatisé
#- Algorithmiquement calculé via config
#+ Configuré
#++ À renseigner

global dict_extracts

main_config_name="main_config.txt"

def extract_txt(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    
    return content

def sort_data_from_extracted_txt(extracted_content):
    '''Deletes lines without data, commentaries within the file
    Creates a dictionary'''
    
    field_value_dict=dict()
    
    for i in extracted_content:
        #Each line in the extracted content helps
        
        if(i.startswith("//")==True or (not i)):
            pass
        else:
            [field,value]=i.split("=")
            field_value_dict[field]=value
    return field_value_dict

extracts=extract_txt(main_config_name)
dict_extracts=sort_data_from_extracted_txt(extracts)
print(dict_extracts)

def iterate_on_list():
    dict_iterated=dict()
    for i in dict_extracts.keys():
        try:
            [field,number]=i.split("_")
            
            if(dict_iterated.get(field)==None):
                dict_iterated[field]=dict()
            dict_iterated[field][number]=dict_extracts[i]
        except:
            pass

    return dict_iterated

pre_chosen_words=iterate_on_list()
print(pre_chosen_words)

def string_types_of_pre_chosen_words(category,words_dict):
    L=''
    for i in words_dict[category].keys():
        #Chaque liste de dictionnaire du dico
        [num,word]=[i,words_dict[category][i]]
        L=L+str(num)+'='+str(word)+'\n'
    return L
        
#print(types_of_pre_chosen_words("debutformule",pre_chosen_words))

def laboOuEntreprise(num):
    if(num==0):
        return ["Laboratoire","il"]
    elif(num==1):
        return ["Entreprise","elle"]
    elif(num==2):
        return ["Offre","elle"]
    else:
        raise "Vous n'avez pas défini à quoi vous répondiez !"
def chercheQuoi(num):
    if(num==0):
        return "mon premier emploi"
    elif(num==1):
        return "un CDI"
    elif(num==2):
        return "un CDD"
    elif(num==3):
        return "un emploi"
    elif(num==4):
        return "un stage"
    else:
        raise "Vous n'avez pas défini quel type de boulot !"

def generate():
    
    etat=int(input("Laboratoire (0), Entreprise (1), Offre (2) ? "))
    cherche=int(input("Premier Emploi (0), CDI (1), CDD (2), Emploi (3), Stage (4) ? "))
    
    #Ici sont utilisés les skills
    #Plusieurs domaines peuvent coexister
    print("Dans quel domaine votre emploi sera orienté ?"+'\n')
    quoi=int(input(string_types_of_pre_chosen_words("skill",pre_chosen_words)+'\n'))
    
    #Ici sont utilisés les skills
    #Plusieurs matières peuvent coexister
    etudes=str(input("Qu'avez vous étudié durant votre scolarité qui pourrait intéresser l'entrprise ? "))
    
    #Ici sont utilisés des sujets d'intérêt
    cadre=str(input("Dans le cadre de quoi ? "))
    
    #Ici sont utilisés des pré-formulations
    #Seule une attente exigée
    attente=str(input("Pourquoi ça correpond ? "))
    
    entree="Madame, Monsieur,"+'\n'
    
    #paragraphe_1
    presentation="J’ai réalisé mes études en deux écoles d'ingénieur : à l’ISBS et à l’ESIEE Paris. J’y ai étudié {0}.".format(etudes)
    recherche="Je cherche actuellement {0} en {1}, dans le cadre {2}. Je postule à votre {3} car {4} correspond {5}.".format(chercheQuoi(cherche),pre_chosen_words["skill"][str(quoi)],cadre,laboOuEntreprise(etat)[0],laboOuEntreprise(etat)[1],attente)
    paragraphe_1=presentation+'\n'+recherche
    
    #paragraphe_2
    #Le paragraphe 2 étant trop complexe à créer, il vaut mieux le rédiger soi-même.
    paragraphe_2=''
    
    argM=str(input("Redigez votre Argument maître en entier : "))
    
    att=str(input("Votre attitude est quoi ?"))
    
    #paragraphe_3
    #L'argument maitre serait à rédiger soi-même, c'est très facile à faire
    argument_maitre=''
    #Les arguments sont à générer. Les structures de phrases étant faciles à réaliser, c'est la partie la plus facile à faire.
    arguments=''
    attitude="Mon attitude {0} : je suis {1}. Dans mes activités, je suis {2}. J'ai une facilité {3}. Je m'adapte {4}.".format('','','','','')
    paragraphe_3=argument_maitre+arguments+attitude
    
    #sortie
    politesse=dict_extracts['politesse']
    remerciements=dict_extracts['remerciements']
    sortie=politesse+'\n'+remerciements+'\n\n'+dict_extracts['firstname']+' '+dict_extracts['lastname']
    
    texte=entree+paragraphe_1+'\n'+paragraphe_2+'\n'+paragraphe_3+'\n'+sortie
    return texte

print(generate())

