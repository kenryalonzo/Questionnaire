# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

"""
    titre = question[0]
    choix = question[1]
    bonne = question[2]
"""

def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input("Votre réponse entre (" + str(min) + " et " + str(max) +") : ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print(f"Error : vous devez entrer un compris entre {min} et {max}")
    except:
        print("Error : vous devez entrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min, max)


def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")

    for i in range(len(choix)):
        print(" ", i+1, "-", choix[i])
    print()
    reponse_correcte = False
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return reponse_correcte
    
"""
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponse = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"
"""

def lancer_qestionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print(f"\n==============Score : {score} / {len(questionnaire)} ==================\n")
    

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Avers", "Bruxelles", "Bruges", "Liege"), "Bruxelles")
    )

# poser_question(question1)
# poser_question(question2)

lancer_qestionnaire(questionnaire)

# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
# poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")