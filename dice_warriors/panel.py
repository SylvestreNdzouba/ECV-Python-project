import tkinter as tk


"""def panneau_jeu():
    pygame.init()
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))

    fond = pygame.image.load("backgroundGame.jpg")

    fond = pygame.transform.scale(fond, (largeur, hauteur))

    en_jeu = True

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False

        fenetre.blit(fond, (0, 0))

        pygame.display.flip()

    pygame.quit()
"""

def panneau_jeu():
    fenetre = tk.Tk()
    fenetre.geometry("800x600")
    
    image_de_fond = tk.PhotoImage(file="background.png")
    
    largeur_image = image_de_fond.width()
    hauteur_image = image_de_fond.height()
    
    canvas = tk.Canvas(fenetre, width=largeur_image, height=hauteur_image)
    canvas.pack()
    
    canvas.create_image(0, 0, anchor=tk.NW, image=image_de_fond)
    
    image_character1 = tk.PhotoImage(file="mage.png")
    image_character2 = tk.PhotoImage(file="warrior.png")
    
    canvas.create_image(30, 150, anchor=tk.NW, image=image_character1) 
    canvas.create_image(450, 110, anchor=tk.NW, image=image_character2)
    
    fenetre.mainloop()




if __name__ == "__main__":
    panneau_jeu()
