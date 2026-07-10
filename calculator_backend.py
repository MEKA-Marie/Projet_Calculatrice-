expression = ""
display = "0"


def ajouter_chiffre(chiffre):
    global expression, display
    if expression == "0":
        expression = chiffre
    else:
        expression = expression + chiffre
    display = expression


def ajouter_operateur(op):
    global expression, display
    if expression == "":
        return
    if expression[-1] in "+-*/":
        expression = expression[:-1] + op
    else:
        expression = expression + op
    display = expression


def ajouter_point():
    global expression, display
    if "." not in expression:
        if expression == "":
            expression = "0."
        else:
            expression = expression + "."
    display = expression


def effacer():
    global expression, display
    expression = ""
    display = "0"


def calculer():
    global expression, display
    if expression == "":
        return

    try:
        resultat = eval(expression, {"__builtins__": {}}, {})
        if isinstance(resultat, float) and resultat.is_integer():
            resultat = int(resultat)
        expression = str(resultat)
        display = expression
    except Exception:
        expression = ""
        display = "Erreur"
