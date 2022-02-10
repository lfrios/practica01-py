from enum import Enum
import random


tipo_Ataque = Enum('Ataque','Ligero, Pesado, Especial')
tipo_Defensa = Enum('Defensa','Esquivar, Desviar, Bloquear')

tipo_Defensa.Esquivar.blocks = {tipo_Ataque.Ligero}
tipo_Defensa.Desviar.blocks = {tipo_Ataque.Ligero, tipo_Ataque.Pesado}
tipo_Defensa.Bloquear.blocks = {tipo_Ataque.Especial}

class Peleador:
    def __init__(self, name):
        self.name = name
        self.attack = None
        self.defense = None
        self.hitpoint = 100
    
    def damage(self):
        puntos_vida = random.randint(5,40)
        self.hitpoint -= puntos_vida
    
    def seleccion_ataque(self):
        eleccion_ataque = int(input('Selecciona el tipo de ataque a realizar 1-Ataque Ligero 2-Ataque Pesado 3- Ataque Especial:  '))
        self.attack = tipo_Ataque(eleccion_ataque)

    def seleccion_defensa(self):
        eleccion_defensa = int(input('Selecciona como defenderte 1-Esquivar 2-Desviar 3-Bloquear:  '))
        self.defense = tipo_Defensa(eleccion_defensa)

class Contrincante(Peleador):
    def __init__ (self, name):
        super().__init__(name)

    def seleccion_ataque(self):
        self.attack = random.choice(list(tipo_Ataque))

    def seleccion_defensa(self):
        self.defense = random.choice(list(tipo_Defensa))

class Game:
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"***   Round: {self.round}   ***")  

    def check_win(self, player, opponent):
        if player.hitpoint < 1 and opponent.hitpoint > 0:
            self.game_over = True
            print("Game Over")
        elif opponent.hitpoint < 1 and player.hitpoint > 0:
            self.game_over = True
            print("Victory")
        elif player.hitpoint < 1 and ai.hitpoint < 1:
            self.game_over = True
            print("*** Draw ***")
    def display_result(self, player, opponent):
            print(f"{player.name} uso un ataque {player.attack.name}, {opponent.name} realizo un {opponent.defense.name} ")
            print(f"{player.name} hizo danho a {opponent.name}\n")

    def take_turn(self, player, opponent):

        if player.attack not in opponent.defense.blocks:
            opponent.damage()
            current_game.display_result(player, opponent)
        else:
            print(f"{player.name} uso un ataque {player.attack.name}, {opponent.name} realizo un {opponent.defense.name} \n")
            print(f"{opponent.name} nego el ataque de {player.name} - No hubo danho")

current_game = Game()
human = Peleador("Varyan")
ai = Contrincante("Garrosh")

players = [human, ai]

while not current_game.game_over:
    for player in players:
        player.seleccion_ataque()
        player.seleccion_defensa()
    current_game.new_round()
    current_game.take_turn(human, ai)
    current_game.take_turn(ai, human)
    print(f"{human.name}'s health = {human.hitpoint}")
    print(f"{ai.name}'s health = {ai.hitpoint}")
    current_game.check_win(human, ai)