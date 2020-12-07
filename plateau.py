from agent import *

class plateau():
    def __init__(self):
        self.state_plateau = [0,0,0,0,0,0,0,0,0]
        self.game = 0

        self.init_game()
        self.update_plateau()
        self.launch_game()
        #self.agent_blanc.get_actions(self)

    def get_joueur_precedent(self):
        return self.joueur_precedent

    def get_state_plateau(self):
        return self.state_plateau

    def init_game(self):
        #creation des 2 joueurs.
        self.agent_noir = agent('*')
        self.agent_blanc = agent('o')

    def affichage_plateau(self):
        print("    "+str(self.state_plateau[2])+"    ")
        print("  "+str(self.state_plateau[1])+"   "+str(self.state_plateau[3])+"  ")
        print(str(self.state_plateau[0])+"   "+str(self.state_plateau[8])+"   "+str(self.state_plateau[4]))
        print("  "+str(self.state_plateau[7])+"   "+str(self.state_plateau[5])+"  ")
        print("    "+str(self.state_plateau[6])+"    ")

    def update_plateau(self):
        #met a jour le plateau en allant chercher tous les pions des agents et leur position.
        i = 0
        self.state_plateau=['.','.','.','.','.','.','.','.','.']
        while i < 4:
            self.state_plateau[self.agent_noir.tab_pions[i].position] = self.agent_noir.symbole_pion
            self.state_plateau[self.agent_blanc.tab_pions[i].position] = self.agent_blanc.symbole_pion
            i += 1

    def launch_game(self):
        self.game = 1
        turn = 'black'
        count_tour = 1
        while self.game == 1 :
            print("tour :", count_tour)
            self.affichage_plateau()
            self.agent_noir.play(self)
            self.update_plateau()

            self.affichage_plateau()
            self.agent_blanc.play(self)
            self.update_plateau()

            count_tour += 1
