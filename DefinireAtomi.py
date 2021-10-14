import re

def split_by_separator(element, separatori, atomi_lexicali):
    if len(element) == 0 or element is None:
        return
    elif element in separatori:
        print(element)
        atomi_lexicali.append(element)
    elif not any(sep in element for sep in separatori):
        print(element)
        atomi_lexicali.append(element)
    elif re.compile("[+-]?([0-9]*[.])?[0-9]+").fullmatch(element):
        print(element)
        atomi_lexicali.append(element)
    else:
        for i in range(len(element)):
            sep = element[i]
            if(i < len(element)-1 and element[i] + element[i+1] in separatori):
                sep = element[i] + element[i+1]
            if sep in separatori:
                split_by_separator(element[0:element.index(sep)], separatori, atomi_lexicali)
                print(sep)
                atomi_lexicali.append(sep)
                split_by_separator(element[element.index(sep)+len(sep):], separatori, atomi_lexicali)
                break


def formatare_lista_atomi_lexicali(atomi_lexicali):
    atomi_lexicali = list(dict.fromkeys(atomi_lexicali))
    cuv_rezervate = ['int', 'double', 'void', 'while', 'if', 'else', 'Console', 'WriteLine', 'ReadLine', 'Parse']
    atomi_lexicali = ['ID','CONST'] + atomi_lexicali
    dictionar_atomi = {}
    cod_unic = 0

    pattern_constanta = re.compile("[+-]?([0-9]*[.])?[0-9]+")
    pattern_identificator = re.compile("[a-z][a-zA-Z0-9]{0,7}")

    for atom in atomi_lexicali:
        if atom in cuv_rezervate or not pattern_constanta.fullmatch(atom) and not pattern_identificator.fullmatch(atom):
            dictionar_atomi[atom] = cod_unic
            cod_unic += 1

    return dictionar_atomi

def spliting():
    f = open("ariePerimetru.txt", "r")
    #f = open("cmmdc.txt", "r")
    #f = open("suma.txt", "r")
    lines = f.readlines()
    separatori=['.', ',', ';', '(', ')', '{', '}', '*', '=', '-', '+', '>', '<', '!=', '>=', '<=', '==']
    atomi_lexicali = []
    for line in lines:
        elements = line.split()
        print("The current line is defined by: ", elements)
        for element in elements:
            split_by_separator(element, separatori, atomi_lexicali)

    print("Lista de atomi lexicali sunt: ", formatare_lista_atomi_lexicali(atomi_lexicali))

spliting()