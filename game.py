from gui import *
import os, pickle

class Scene():
    def __init__(self, name):
        self.name = name

class Battle():
    def __init__(self, name, friendly_npc_string_list, enemy_npc_string_list):
        self.name = name
        self.friendly_npc_string_list = friendly_npc_string_list
        self.enemy_npc_string_list = enemy_npc_string_list
    def load_npcs(self):
        self.friendly_npc_object_set = set()
        self.enemy_npc_object_set = set()
        for friendly_npc_string in self.friendly_npc_string_list:
            self.friendly_npc_object_set.add(pickle.load(open(os.path.join('data','npcs', friendly_npc_string + '.p'),'rb')))
        for enemy_npc_string in self.enemy_npc_string_list:
            self.enemy_npc_object_set.add(pickle.load(open(os.path.join('data','npcs', enemy_npc_string + '.p'),'rb')))
            

class Player():
    pass

class Npc():
    def __init__(self, name, armor_string, weapon_string, secondary_weapon_string):
        self.name = name
        self.armor_string = armor_string
        self.weapon_string = weapon_string
        self.secondary_weapon_string = secondary_weapon_string
        self.armor = pickle.load(open(os.path.join('data','items','armor', self.armor_string + '.p'),'rb'))
        self.weapon = pickle.load(open(os.path.join('data','items','weapons', self.weapon_string + '.p'),'rb'))
        self.secondary_weapon = pickle.load(open(os.path.join('data','items','weapons', self.secondary_weapon_string + '.p'),'rb'))
        self.health = 100

class Armor():
    def __init__(self, name, worth, armor_class):
        self.name = name
        self.worth = worth
        self.armor_class = armor_class  

class Weapon():
    def __init__(self, name, worth, damage, type, accuracy):
        self.name = name
        self.worth = worth
        self.damage = damage
        self.damage_type = type       
        self.accuracy = accuracy

def main():
    battle = Battle('Caravan', ['Lethomyr Darkin'], ['bandit', 'bandit', 'bandit', 'bandit captain'])
    battle.load_npcs()    
    for npc in battle.friendly_npc_object_set:
        print(npc.name, npc.armor, npc.weapon, npc.secondary_weapon)
    for npc in battle.enemy_npc_object_set:
        print(npc.name, npc.armor, npc.weapon, npc.secondary_weapon)
    # npc = Npc('bandit', 'leather', 'axe', 'fist')
    # pickle.dump(npc, open(os.path.join('data','npcs',npc.name + '.p'),'wb'))
    # armor = Armor('plate', 500, 6)
    # pickle.dump(armor, open(os.path.join('data','items','armor',armor.name + '.p'),'wb'))     
    weapon = Weapon('round shield', 0, 2, 'raw', 95)
    pickle.dump(weapon, open(os.path.join('data','items','weapons',weapon.name + '.p'),'wb'))
if __name__ == "__main__":
    main()