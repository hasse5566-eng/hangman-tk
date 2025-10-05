#hangman projekt 

import random 
import tkinter as tk

#ord som kan väljas 
WORD_LIST = ["apple", "banana", "dog", "cat", "school", "python", "computer", "chair", "table", "flower"]

#antal fel
MAX_MISTAKES = 6 

def main(): 
    secret = random.choice(WORD_LIST)
    shown = ["_"] * len(secret)
    guessed = set()
    mistakes = 0

    #skapar fönster
    root = tk.Tk()
    root.title("Hang man (Tkinter)")
    root.geometry("360x300")

    #rubrik&instruktioner 
    tk.Label(root, text="Välkommen till Hangman!", font=("Arial", 14)).pack(pady=5)
    tk.Label(root, text="Gissa en bokstav i taget").pack(pady=2)

    #visar ordet & status 
    word_lbl = tk.Label(root, text=" ".join(shown), font=("Consolas", 20)); word_lbl.pack(pady=8)
    status_lbl = tk.Label(root, text=f"Fel: {mistakes}/{MAX_MISTAKES}"); status_lbl.pack()
    guessed_lbl = tk.Label(root, text="Gissade bokstäver: "); guessed_lbl.pack(pady=2)
    msg_lbl = tk.Label(root, fg="blue"); msg_lbl.pack(pady=4)

    #inmatningsruta för att skriva bokstav 
    frame  = tk.Frame(root); frame.pack(pady=6)
    entry = tk.Entry(frame, width=5, font=("Arial", 16)); entry.grid(row=0, column=0, padx=5)
    btn = tk.Button(frame, text="Gissa"); btn.grid(row=0, column=1)

    #uppdatering av texten i fönsteret 
    def update(): 
        word_lbl.config(text=" ".join(shown))
        status_lbl.config(text=f"Fel: {mistakes}/{MAX_MISTAKES}")
        guessed_lbl.config(text="Gissade bokstäver: " + " ".join(sorted(guessed)))
    
    #när spelet är över
    def end(win):
        nonlocal secret
        btn.config(state="disabled")
        entry.config(state="disabled")
        if win:
            msg_lbl.config(text=f"Du vann! Ordet var: {secret}", fg="green")
        else:
            msg_lbl.config(text=f"Du förlorade. Ordet var: {secret}", fg="red")

    #När man trycker på Gissa eller Enter
    def on_guess(_=None):
        nonlocal mistakes, guessed, shown, secret
        g = entry.get().strip().lower()
        entry.delete(0, tk.END)
        
        if len(g) != 1 or not g.isalpha():
            msg_lbl.config(text="Skriv EN bokstav.", fg="blue"); return
        
        if g in guessed:
            msg_lbl.config(text="Redan gissat den.", fg="blue"); return
    
        guessed.add(g)
    
        if g in secret:
            msg_lbl.config(text="Rätt!", fg="green")
            for i, ch in enumerate(secret):
                if ch == g:
                    shown[i] = g
            update()
            if "_" not in shown:
                end(True)
        else: 
            mistakes += 1
            msg_lbl.config(text="Fel!", fg="red")
            update()
            if mistakes >= MAX_MISTAKES:
                end(False)
 
    #kopplar knappen
    btn.config(command=on_guess)
    root.bind("<Return>", on_guess)
 
    #skärmen uppdateras vid start 
    update()
    entry.focus_set()
 
    root.mainloop()
 
#startar programmet
if __name__ == "__main__":
    main()
    
#Så här spelar man:
#1. Starta filen `hangman_tk.py`
#2. Gissa en bokstav i taget
#3. Du får max 6 fel
#4. Avslöja alla bokstäver för att vinna
    
    