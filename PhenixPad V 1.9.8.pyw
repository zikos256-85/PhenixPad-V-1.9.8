import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#code Name : Colombo
#Build:203
class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisdeveloppeur = Menu(__thisMenuBar,tearoff=0)
    __thisUpdate = Menu(__thisMenuBar,tearoff=0)
    __thisRedirection = Menu(__thisHelpMenu,tearoff=False)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
                self.__root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
            pass 
                

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            print("Error please to restart")
           

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            print("Error please to restart")
            

        #set the window text
        self.__root.title("New file- PhenixPad : Version 1.9.8")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy",command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="information sur la version phenixpad",command=self.__showAbout)
        self.__thisHelpMenu.add_command(label="À propos du phenixpad",command=self.__showAbout3)
        self.__thisHelpMenu.add_command(label="SLOPPY SOFTWARE AGREEMENT TERMS",command=self.__showAbout4)
        self.__thisHelpMenu.add_command(label="Update Information",command=self.__showAbout5)
        self.__thisHelpMenu.add_cascade(label="Redirection",menu=self.__thisRedirection)
        self.__thisRedirection.add_command(label="Ghit Hub",command=self.__GhitHub)
        self.__thisRedirection.add_command(label="PhenixPad Help Update",command=self.__PhenixPadHelpUpdate)
        self.__thisHelpMenu.add_command(label="Report Bug",command=self.__showAbout6)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__thisdeveloppeur.add_command(label="New",command=self.__newFile)
        self.__thisdeveloppeur.add_command(label="Open",command=self.__openfiledev)
        self.__thisdeveloppeur.add_command(label="Save",command=self.__saveFile)
        self.__thisdeveloppeur.add_command(label="fonctionnalité de développement",command=self.__showAbout2)
        self.__thisMenuBar.add_cascade(label="développeur",menu=self.__thisdeveloppeur)
        


        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()


    def __showAbout(self):
        showinfo("Phenixpad","Created by: Phenix :Phenixpad Version 1.9.8")


    def __showAbout2(self):
        showinfo("fonctionnalité de développement","la fonctionnalité developpeur permet au développeur de continuer à travailler sur son projet de codage tout en utilisant notre bloc-notes. vous pouvez ouvrir votre code source créé à nouveau et même enregistrer la reprise de votre code ou projet dans le bloc-notes.") 

    def __showAbout3(self):
        showinfo("À propos du phenixpad","Facile à utiliser, nous avons conçu ce bloc-notes avec des fonctionnalités utiles. Il sera mis à jour chaque mois pour améliorer l'utilisation du phenixpad. N'oubliez pas de toujours le mettre à jour pour bénéficier des dernières améliorations. Tous droits réservés.\n Ce produit est fourni selon les termes du contrat de logiciel fourni par sloppy.\n Date de création du logiciel : 2020.\n Dernière version : 1.9.3 build:203\n crée par sloppy.")


    def __showAbout4(self):
          showinfo("SLOPPY SOFTWARE AGREEMENT TERMS","TERME DU CONTRAT LOGICIEL SLOPPY FOURNIT AUX PHENIX PAD:Le logiciel est protégez par le groupe sloppy ,c'est le groupe sloppy qui se charge du devellopment et de l amelioration de l aplication.\n sloppy ce chargera de faire dans l aplication:\n . Les mise a jour,J'usqua sa fin du support qui est programmée pour le 31 décembre 2021.\nAssurez l amelioration du produit.\nAssurez les correction de bug trouvée dans le produit.\nAssurez le service technique  d aide si un utlisateur recontre des probleme d utilisation de l aplication.\ncondition d instalation du logiciel :nous fournisson le logiciel gratuitement , il n ya pas de restricion d installation  par nombre d'ordinateur , vous pouvez deployez le logiciel sur tout votre parc informatique.")
    def __showAbout5(self):
          showinfo("Update information","Phenixpad est un produit qui sera mise a jour chaque mois\n , pour vous offrir la meilleur expérience  d'utilisation de se logiciel\n , ces mise a jour vont permettre a résoudre tous les bug trouvée dans le logiciel\n , ainsi que lui intégrée de nouvelle fonctionnalité\n , et facilitée son utilisation\n. C'est pour ça que nous voulons que vous ayez la dernier\n version pour que vous pouvez profitez de la meilleur expérience du produit\n . Pour que vous vous procurez les dernière version\n , veuillez vous rendre soit a notre page ghit Hub\n , pour la verison en Open Source\n , ou sur notre site OFFICIEL de téléchargement pour la version en .EXE\n . Dans ces deux site nous vous publieront  la description des mise a jour\n , pour que vous pouvez savoir ce que c'est mise a jour vont apporter de nouveaux\n . Tout les nouvelles mise a jour sont publier le DEUXIÈME VENDREDI DU MOIS\n .Pour pouvoir accéder a c'est deux site\n allez sur l'onglet Redirection vers:\nGhit Hub ou\nPhenixpad site")
    def __showAbout6(self):
        showinfo("Report Bug","Si vous avez trouvez un bug sur le logiciel merci de bien nous mettre au courant via ce mail : PhenixDeveloppement85@gmail.com\nC'est a grâce de votre fidélité quand n' améliore Phenixpad.")

   

          
    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("Text Documents","*.txt*"),("Text Documents","*.txt")])
        showinfo("Message Important","La nouvelle version de Phenix Pad va bientôt sortir, elle se nomme PhenixPad X et va offrir de nouvelle fonctionnalité pour une utilisation encore plus facile, c'est pour ça que nous vous invitons à la découvrir dès quel sort . Pour être informé des dernières informations suis-moi sur twitter où je mets tous les infos du suivi du projet PhenixPad X.")

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            

            #try to open the file 

            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Phenixpad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

    def __openfiledev(self):

        self.__file =  askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*")])

        
        if self.__file == "":
            #no file to open
            self.__file = None
        else:

            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Phenixpad")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())
        
    def __newFile(self):
        self.__root.title("Untitled - Phenixpad V 1.9.8")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
                

                
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Phenixpad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __GhitHub(self):
        webbrowser.open('https://github.com/zikos256-85/PhenixPad-Version-1.9.3')
    def __PhenixPadHelpUpdate(self):
        webbrowser.open('https://sites.google.com/view/phenixpad-update-help/accueil')
    def __twitter(self):
        webbrowser.open()
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()    