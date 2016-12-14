from jeu import *
from ia import *
import pygame
import time
import sys
import os
import math



class RiviereGraphique(object):
    """Classe simple d'affichage et d'interaction pour le labyrinthe."""
    
    pi6=math.pi/6
    sinPi6=0.5
    cosPi6=math.cos(pi6)
    cotanPi6=1/math.tan(pi6)

    def __init__(self, jeu, titre='La rivière de l''IUT''O', size=(1000, 800), couleur=(209,238,238),prefixeImage="./images"):
        pygame.init()
        self.jeu=jeu
        self.riviere=getRiviere(jeu)
        self.joueurs=getJoueursJ(jeu)
        self.possibles=getJoueursPossibles(self.joueurs)
        self.nomsPossibles=getListeNomsJoueur(self.possibles)
        self.classement=getClassement(jeu)       
        self.nbLig=getNbLigR(self.riviere)
        self.nbCol=getNbColR(self.riviere)
        self.paire=estPaireR(self.riviere)
        self.colArrivee=getColArrivee(self.riviere)
        self.colDepart=getColDepart(self.riviere)        
        self.couleur=couleur
        self.getImages()
        pygame.display.set_icon(self.icone)
        self.fenetre = pygame.display.set_mode(size,pygame.RESIZABLE|pygame.DOUBLEBUF)
        pygame.display.set_caption(titre)
        self.surface=pygame.display.get_surface()

        self.size=size
        self.miseAJourParametres()
        
    def polygone(self,Surface, color, n, radius, position):
        pi2 = 2 * math.pi
        pygame.draw.lines(Surface,color,True,
          [(math.cos(i / n * pi2) * radius + position[0], math.sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])

    def droite(self,Surface,color,n,coef,pos):
        b=pos[1]-coef*pos[0]
        pygame.draw.lines(Surface,color,True,
                          [(i*10,coef*i*10+b) for i in range(0,n)])
        
    def miseAJourParametres(self):
        self.size=self.surface.get_size()
        self.hauteurMax=self.size[1]
        self.largeurMax=2*self.size[0]//3
        self.rayon=int(min(self.hauteurMax//(self.nbLig+2)*1,self.largeurMax//(2*self.nbCol)))
        self.cote=self.rayon
        self.hauteur=int(2*self.rayon*self.cosPi6)
        self.surfEau=pygame.transform.smoothscale(self.images["eau"],(2*(self.rayon-1),self.hauteur-2))
        self.surfRocher=pygame.transform.smoothscale(self.images["rocher"],(2*(self.rayon-1),self.hauteur-2))
        self.surfFleche=pygame.transform.smoothscale(self.images["fleche"],(self.cote//2,self.cote//2))
        self.surfTronc=pygame.transform.smoothscale(self.images["tronc"],(self.cote,self.cote))
        self.surfFond=pygame.transform.smoothscale(self.images["fond"],((self.rayon+self.rayon//2)*(self.nbCol)+self.cote,self.hauteur*(self.nbLig)//2+self.hauteur))
        self.surfDepArr=pygame.transform.smoothscale(self.images["fondeau"],(self.cote,self.hauteur+self.rayon))
        self.tailleFont=32
        self.surfJoueur={}
        for j in self.imgJoueurs:
            self.surfJoueur[j]=pygame.transform.smoothscale(self.imgJoueurs[j],(int(self.cote*1.2),int(self.cote*1.3)))     
        
        self.dessinerGrille()
        
    def chargeImage(self,nomImage, prefixImage="./images"):
        if os.path.isfile(os.path.join(prefixImage,nomImage)):
            s=pygame.image.load(os.path.join(prefixImage,nomImage))
        else:
            print("pb avec le fichier",prefixImage,nomImage)
            s=None
        return s
        
    def getImages(self,prefixImage="./images"):
        self.images={}
        self.imgJoueurs={}
        self.images["rocher"]=self.chargeImage("hexaRocher.png",prefixImage)
        self.images["eau"]=self.chargeImage("hexaEau.png",prefixImage)
        self.images["fleche"]=self.chargeImage("fleche.png",prefixImage)
        self.images["tronc"]=self.chargeImage("buche.png",prefixImage)
        self.images["fond"]=self.chargeImage("rocher.jpg",prefixImage)
        self.images["fondeau"]=self.chargeImage("eau.jpg",prefixImage)
        for nomJ in self.nomsPossibles:
            self.imgJoueurs[getRepresentationJoueur(self.possibles,nomJ)]=self.chargeImage(nomJ+".png",prefixImage)
        self.icone=pygame.image.load(os.path.join(prefixImage,'logoIUTO.png'))        

    def flecheCourant(self,direction,surfFleche):
        if direction=="N":
            f=pygame.transform.rotate(surfFleche,-90)
        elif direction=="S":
            f=pygame.transform.rotate(surfFleche,90)
        elif direction=="NO":
            f=pygame.transform.rotate(surfFleche,-45)
        elif direction=="NE":
            f=pygame.transform.rotate(surfFleche,-135)
        elif direction=="SO":
            f=pygame.transform.rotate(surfFleche,45)
        elif direction=="SE":
            f=pygame.transform.rotate(surfFleche,135)
        else:
            f=None
        return f
                
    def dessinerGrille(self,msg='',mode=0):
        self.surface.fill((255,255,255))
        self.debutH=self.cote+self.rayon
        self.debutV=self.cote+self.rayon
        debutV=self.debutV
        debutH=self.debutH
        cDebut=0
        self.surface.blit(self.surfFond,(debutV//2-self.cote//4,debutH//2-self.hauteur//6))
        self.surface.blit(self.surfDepArr,(debutV-self.cote//2+(self.colDepart)*(self.rayon//2+self.cote),debutH//2-self.hauteur//6))
        self.surface.blit(self.surfDepArr,(debutV-self.cote//2+(self.colArrivee)*(self.rayon//2+self.cote),debutH-2*self.rayon-self.hauteur//6+self.nbLig*self.hauteur//2))
        if not self.paire:
            debutH+=self.cote/2+self.rayon
            cDebut=1
        for i in range(self.nbLig):
            for j in range(cDebut,self.nbCol,2):
                self.polygone(self.surface,(0,0,0),6,self.rayon,(debutH+(j//2)*(2*self.rayon+self.cote),debutV+i*(self.hauteur//2)))
                contenu=getContenuR(self.riviere,i,j)
                if contenu==ROCHER:
                    self.surface.blit(self.surfRocher,(debutH+(j//2)*(2*self.rayon+self.cote)-(self.rayon-1),debutV+i*(self.hauteur//2)-(self.hauteur//2-1)))
                else:
                    self.surface.blit(self.surfEau,(debutH+(j//2)*(2*self.rayon+self.cote)-(self.rayon-1),debutV+i*(self.hauteur//2)-(self.hauteur//2-1)))
                courant=getCourantR(self.riviere,i,j)
                f=self.flecheCourant(courant,self.surfFleche)
                if f!=None:
                    self.surface.blit(f,(debutH+(j//2)*(2*self.rayon+self.cote)-(self.cote*1.5//2),debutV+i*(self.hauteur//2)-(self.cote//2)))
                if contenu==TRONC:
                    self.surface.blit(self.surfTronc,(debutH+(j//2)*(2*self.rayon+self.cote)-(self.cote*1.2//2),debutV+i*(self.hauteur//2)-(self.cote*1.2//2)))
                elif contenu not in (VIDE,ROCHER):
                    self.surface.blit(self.surfJoueur[contenu],(debutH+(j//2)*(2*self.rayon+self.cote)-(self.cote//2),debutV+i*(self.hauteur//2)-(self.cote*1.2//2)))
            if cDebut==0:   
                cDebut=1
                debutH+=self.cote/2+self.rayon
            else:
                cDebut=0
                debutH-=self.cote/2+self.rayon
        if mode==0:
            self.afficherMsgJeu(msg)
        elif mode==1:
            self.afficherMsgChoix(msg)

    def afficherMessage(self,ligne,message,images=[],couleur=(0,0,0)):
        font = pygame.font.Font(None, self.tailleFont)
        posy=self.hauteur*ligne
        posx=(self.rayon+self.rayon//2)*(self.nbCol)+self.cote*2
        listeTextes=message.split('@img@')

        for msg in listeTextes:
            if msg!='':
                texte=font.render(msg,1,couleur)
                textpos=texte.get_rect()
                textpos.y=posy
                textpos.x=posx
                self.surface.blit(texte,textpos)
                posx+=textpos.width#+(self.deltal//3)

            if images!=[]:
                surface=images.pop(0)
                debuty= posy-(self.rayon//3)
                self.surface.blit(surface,(posx,debuty))
                posx+=surface.get_width()#+(self.deltal//3)

    def afficherMsgJeu(self,msg):
        if getNbJoueursJ(self.jeu)!=0:
            self.afficherMessage(1,"C'est au tour du joueur @img@",[self.surfJoueur[getRepresentation(getJoueurCourantJ(self.jeu))]])
            self.afficherMessage(2,"Il lui reste "+str(getNbCoupsRestants(self.jeu))+" coups à effectuer")
        else:
            self.afficherMessage(1,"Voulez vous rejouer? (o/n)")                
       
        self.afficherMessage(3,msg)
        self.afficherMessage(5,"CLASSEMENT")
        for i in range(getNbJoueurs(self.classement)):
            self.afficherMessage(6+i,str(i+1)+'. @img@ '+getNom(getJoueurI(self.classement,i)),[self.surfJoueur[getRepresentation(getJoueurI(self.classement,i))]])

    def construireMsgChoix(self,mode=0):
        if mode==0:
            noms=self.nomsPossibles
            chaine='Q -> Quitter  '
        else:
            noms=[]
            chaine=''
            for i in range(getNbJoueurs(self.joueurs)):
                noms.append(getNom(getJoueurI(self.joueurs,i)))
        
        liste=[]
        for nom in noms:
            ch=getRepresentationJoueur(self.possibles,nom)
            chaine+=ch+' -> @img@  '
            liste.append(self.surfJoueur[ch])
        return chaine,liste
    
    def afficherMsgChoix(self,msg=''):
        self.afficherMessage(1,"Choix des joueurs entrant dans la course")
        self.afficherMessage(2,"Tapez l'initial du joueur de votre choix (minuscule => automatique)")
        texte,liste=self.construireMsgChoix(0)
        self.afficherMessage(3,texte,liste)
        self.afficherMessage(4,"Liste des joueurs choisis")
        texte,liste=self.construireMsgChoix(1)
        self.afficherMessage(5,texte,liste)
        self.afficherMessage(6,msg)
        
    """ l'idée pour calculer la case en fonction de la position de la souris est
        de calculer le nombre de diagonales et le nombre de lignes horizontales
        traversées par rapport le haut gauche de la carte. le coefficient 
        directeur des lignes obliques est cotanPi6.
        Pour le calcul, il faut faire attention à la ligne où on est pour
        trouver le nombre de diagonales traversées. Chaque ligne horizontale
        est composer de "motifs" de 3 segments de longueur. Un segement se
        trouve sur une ligne, un autre sur la ligne du dessus. Le troisième est
        à cheval sur les 2 lignes, il faut déterminer la ligne grâce à la ligne
        oblique dans l'autre sens.
        Enfin, le calcul est différent suivant que la grille est paire ou impaire
        y=ax+b b=y-ax
    """
    def getCase(self,pos):
        # calcule le nombre d'horizontales traversées
        if (pos[1]<self.debutV-self.hauteur//2): # cas du clic au dessus de la grille
            h=-1
        else:
            h=int((pos[1]+self.hauteur//2-self.debutV)/(self.hauteur//2))

        # On en déduit l'origine en y de notre repère oblique
        yOrig=self.debutV-self.hauteur//2
        # calcule de l'origine en x de notre repère oblique suivant la parité
        # de la grille
        if self.paire:
            #le sommet haut gauche du premier hexagone a pour abscisse:
            xOrig=self.debutH-self.sinPi6*self.rayon
            auxD=1
        else:
            # la droite qui prolonge le coté le + à gauche de la 1ere la ligne 
            # paire coupe la première ligne horizontale:
            xOrig=self.debutH
            auxD=0
    
        # calcule le nombre de diagonales traversées (la variable d)
        # grace à la la résolution de l'équation b=y-ax
        b=(pos[1]-yOrig)+self.cotanPi6*(pos[0]-xOrig)
        if b<0: # cas du clic au dessus de la 1ere diagonale
            d=-1
        else:
            d=int(b/self.hauteur)-h//2
            
        #calcul du segment
        num=d%3
        # calcul du numéro de colonne approximatif
        col=d*2//3
        
        if self.paire and h%2==0 or not self.paire and h%2==1:
            if num==0:
                lig=h
            elif num==2:
                lig=h-1
            else: # num==1
                b1=pos[1]-self.cotanPi6*pos[0]
                b2=(h/2*self.hauteur+self.debutV)-self.cotanPi6*(d*self.rayon+self.debutH)
                if b1<b2:
                    lig=h-1
                    col+=1
                else:
                    lig=h
        else:
            if not self.paire: # il y a des petits décalage entre les grilles paires et impaires
                num=(num+1)%3  # ces variables servent à rectifier le tir
                auxCol=1
            else:
                auxCol=0
            if num==1:
                lig=h-1
            elif num==2:
                lig=h
                col+=auxCol
            else: #num==0
                b1=pos[1]-self.cotanPi6*pos[0]
                b2=(h/2*self.hauteur+self.debutV-self.hauteur/2)-self.cotanPi6*((d-auxD)*self.rayon+self.debutH)
                col+=auxCol
                if b1<b2:
                    lig=h-1
                else:
                    lig=h
                    col-=1
        return (lig,col)
    
                
    def demarrer(self):
        self.phase=1
        #self.possibles=getListeNomsJoueur(self.joueurs)        
        pygame.time.set_timer(pygame.USEREVENT+1,100)
        self.mode=1 #mode vaut 1 si on selectionne les joueurs et 0 sinon
        self.dessinerGrille('',1)
        
        while(True):
            ev=pygame.event.wait()
            if ev.type ==pygame.QUIT:
                break
            if self.mode==0 and ev.type==pygame.USEREVENT+1:
                if getNbJoueursJ(self.jeu)!=0:
                    joueurCourant=getJoueurCourantJ(self.jeu)
                    msg=''
                    if not attenteDirection :
                        nbc=getNbCoupsRestants(self.jeu)
                        if nbc==0:
                            attenteDirection,msg=finirDeplacement(self.jeu)
                        else:
                            msg=jouerDirection(self.jeu,direction)
                            attenteDirection=getNbCoupsRestants(self.jeu)!=0
                    else:
                        if not estHumain(joueurCourant):
                            direction=choixDirection(jeu)
                            msg='le joueur '+getNom(joueurCourant)+ ' a choisi '+direction
                            attenteDirection=False                  
                    self.dessinerGrille(msg)
                    pygame.display.flip()
            if ev.type==pygame.VIDEORESIZE:
                fenetre=pygame.display.set_mode(ev.size,pygame.RESIZABLE|pygame.DOUBLEBUF)
                self.surface=pygame.display.get_surface()
                self.miseAJourParametres()
                self.dessinerGrille()
                pygame.display.flip()
            if self.mode==0 and ev.type==pygame.MOUSEBUTTONDOWN:
                if getNbJoueursJ(jeu)!=0 and attenteDirection:
                    pos=self.getCase(ev.pos)
                    direction=calculerDirection(self.jeu,pos)
                    attenteDirection=False
            if ev.type==pygame.KEYDOWN:
                if self.mode==0:
                    if chr(ev.key) in 'qQ':
                        break;
                    elif chr(ev.key) in 'oO':
                        if getNbJoueursJ(jeu)==0:
                            self.nomsPossibles=getListeNomsJoueur(self.possibles)
                            viderJoueurs(self.classement)
                            self.mode=1
                            self.dessinerGrille('',1)
                            pygame.display.flip()
                    elif chr(ev.key) in 'nN':
                        if getNbJoueursJ(jeu)==0:
                            break
                elif self.mode==1:
                    if ev.key not in [pygame.K_NUMLOCK,pygame.K_CAPSLOCK,pygame.K_SCROLLOCK,pygame.K_RSHIFT,pygame.K_LSHIFT,pygame.K_RCTRL,pygame.K_LCTRL,pygame.K_RALT,pygame.K_LALT,pygame.K_RMETA,pygame.K_LMETA,pygame.K_LSUPER,pygame.K_RSUPER,pygame.K_MODE]:            
                        shift=pygame.key.get_mods() & pygame.KMOD_SHIFT
                        caps=pygame.key.get_mods() & pygame.KMOD_CAPS
                        humain=(shift and not caps) or (not shift and caps) 
                        rep=chr(ev.key).upper()
                        nom2=getNomJoueur(self.possibles,rep)
                        if nom2 != None:
                            if nom2 in self.nomsPossibles:
                                self.nomsPossibles.remove(nom2)
                                ajouterJoueur(self.joueurs,nom2,humain)
                                self.dessinerGrille('',1)
                            else:
                                self.dessinerGrille(rep+' est déjà sélectionné',1)
                            pygame.display.flip()
                        elif rep=='Q':
                            self.nomsPossibles=getListeNomsJoueur(self.possibles)                        
                            self.mode=0 #mode vaut 1 si on selectionne les joueurs et 0 sinon
                            initJeu(self.jeu)
                            self.dessinerGrille()
                            attenteDirection=True
                        else:
                            self.dessinerGrille(rep+" n'est pas un joueur",1)
                            pygame.display.flip()
                    else:
                        self.dessinerGrille('',1)
                        
            pygame.display.flip()
        pygame.quit()    
            
jeu=Jeu("./","joueurs.txt","riviere1.txt")
rg=RiviereGraphique(jeu)
rg.demarrer()