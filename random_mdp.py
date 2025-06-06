'''import'''
import tkinter
from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter import messagebox
import random
import string

x = 1

def plus():
    global x
    x += 1
    update_length_display()

def moin():
    global x
    if x > 1:
        x -= 1
    update_length_display()

def update_length_display():
    plus_label.config(text=f"Longueur : {x}")

'''définir ouvrir page web'''
def open_github():
    webbrowser.open_new("https://darkgpt.io")

'''générer mdp'''
def generate():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    resultat = ''.join(random.choices(caracteres, k=x))
    password_entry.config(state='normal')
    password_entry.delete(0, END)
    password_entry.insert(0, resultat)
    password_entry.config(state='readonly')

'''copier mot de passe'''
def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers")

window = Tk()

'''personnalisation fenêtre'''
window.title("by STUP!D")
window.geometry("400x500")
window.minsize(500, 500)
window.maxsize(500, 500)
window.iconbitmap("src\\icone.ico")
window.config(background="#000000")

'''frames'''
frame = Frame(window, bg='#000000', bd=1, relief=SUNKEN)
framedeux = Frame(window, bg='#000000', bd=1, relief=SUNKEN)
frametrois = Frame(window, bg='#000000', bd=1, relief=SUNKEN)

'''titre'''
label_title = Label(frame, text="create password", font=("courrier", 20), bg='#000000', fg='white')
label_title.pack()

'''bouton github'''
darkgpt_button = Button(frame, text="github", font=("courrier", 20), bg='red', fg='black', command=open_github)
darkgpt_button.pack(padx=10, fill=X)

'''champ mot de passe (sélectionnable)'''
password_entry = Entry(framedeux, font=("courrier", 20), bg='#000000', fg='black', justify='center', relief=FLAT)
password_entry.pack(padx=10, pady=10, fill=X)
password_entry.config(state='readonly')

'''bouton copier'''
copy_button = Button(framedeux, text="Copier", font=("courrier", 15), bg='red', fg='black', command=copy_password)
copy_button.pack(padx=10, pady=5, fill=X)

'''bouton génération'''
generate_button = Button(frame, text="create password", font=("courrier", 20), bg='red', fg='black', command=generate)
generate_button.pack(padx=10, fill=X)

'''bouton +'''
plus_button = Button(frame, text="+", font=("courrier", 20), bg='red', fg='black', command=plus)
plus_button.pack(padx=10, fill=X)

'''bouton -'''
moin_button = Button(frame, text="-", font=("courrier", 20), bg='red', fg='black', command=moin)
moin_button.pack(padx=10, fill=X)

'''affichage compteur'''
plus_label = Label(frametrois, text=f"Longueur : {x}", font=("courrier", 20), bg='#000000', fg='white')
plus_label.pack()

'''ajouter frames'''
frame.pack(expand=YES)
framedeux.pack(expand=YES)
frametrois.pack(expand=YES)

'''lancer'''
window.mainloop()
