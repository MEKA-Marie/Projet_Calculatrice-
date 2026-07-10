import customtkinter as ctk
import calculator_backend as backend


def cliquer(valeur):
    if valeur == "CE":
        backend.effacer()
    elif valeur == "=":
        backend.calculer()
    elif valeur == ".":
        backend.ajouter_point()
    elif valeur in "+-*/":
        backend.ajouter_operateur(valeur)
    elif valeur.isdigit():
        backend.ajouter_chiffre(valeur)

    display_var.set(backend.display)


def demarrer_interface():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    fenetre = ctk.CTk()
    fenetre.title("Calculatrice")
    fenetre.geometry("380x600")
    fenetre.resizable(False, False)

    global display_var
    display_var = ctk.StringVar(value="0")

    ecran = ctk.CTkEntry(
        fenetre,
        textvariable=display_var,
        width=340,
        font=("Courier", 40, "bold"),
        justify="right",
    )
    ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 20))

    boutons = [
        ("CE", 1, 0),
        ("7", 2, 0),
        ("8", 2, 1),
        ("9", 2, 2),
        ("/", 1, 3),
        ("4", 3, 0),
        ("5", 3, 1),
        ("6", 3, 2),
        ("*", 2, 3),
        ("1", 4, 0),
        ("2", 4, 1),
        ("3", 4, 2),
        ("-", 3, 3),
        ("0", 5, 0),
        (".", 5, 1),
        ("=", 5, 2),
        ("+", 4, 3),
    ]

    for texte, ligne, colonne in boutons:
        bouton = ctk.CTkButton(
            fenetre,
            text=texte,
            width=75,
            height=75,
            font=("Arial", 24, "bold"),
            command=lambda valeur=texte: cliquer(valeur),
        )
        bouton.grid(row=ligne, column=colonne, padx=8, pady=8)

    fenetre.mainloop()
