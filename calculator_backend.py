def addition(a, b):
    """
    Additionne deux nombres et retourne leur somme.

    Paramètres :
        a (int ou float) : premier nombre.
        b (int ou float) : deuxième nombre.

    Retour :
        int ou float : la somme de a et b.
    """
    return a + b


def soustraction(a, b):
    """
    Soustrait le second nombre du premier et retourne la différence.

    Paramètres :
        a (int ou float) : premier nombre.
        b (int ou float) : deuxième nombre.

    Retour :
        int ou float : la différence de a et b.
    """
    return a - b


def multiplication(a, b):
    """
    Multiplie deux nombres et retourne leur produit.

    Paramètres :
        a (int ou float) : premier nombre.
        b (int ou float) : deuxième nombre.

    Retour :
        int ou float : le produit de a et b.
    """
    return a * b


def division(a, b):
    """
    Divise le premier nombre par le second et retourne le quotient.

    Paramètres :
        a (int ou float) : premier nombre.
        b (int ou float) : deuxième nombre (ne doit pas être zéro).

    Retour :
        float : le quotient de a par b.

    Exceptions :
        ZeroDivisionError : si b est égal à zéro.
    """
    if b == 0:
        raise ZeroDivisionError("Division par zéro impossible !")
    return a / b


# Variables globales pour l'interface calculatrice
expression = ""
display = "0"


def ajouter_chiffre(chiffre):
    """
    Ajoute un chiffre à l'expression courante.
    """
    global expression, display
    if expression == "0":
        expression = chiffre
    else:
        expression = expression + chiffre
    display = expression


def ajouter_operateur(op):
    """
    Ajoute un opérateur mathématique (+, -, *, /) à l'expression.
    """
    global expression, display
    if expression == "":
        return
    if expression[-1] in "+-*/":
        expression = expression[:-1] + op
    else:
        expression = expression + op
    display = expression


def ajouter_point():
    """
    Ajoute un point décimal (.) à l'expression.
    """
    global expression, display
    if "." not in expression:
        if expression == "":
            expression = "0."
        else:
            expression = expression + "."
    display = expression


def effacer():
    """
    Réinitialise la calculatrice en vidant l'expression et en affichant "0".
    """
    global expression, display
    expression = ""
    display = "0"


def calculer():
    """
    Évalue l'expression mathématique et affiche le résultat.
    """
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
