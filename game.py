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
    def __init__(self, name, armor, weapon, secondary_weapon):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon







def main():
    # npc = Npc('bandit captain', 'studded leather', 'two-handed axe', None)
    # pickle.dump(npc, open(os.path.join('data','npcs',npc.name + '.p'),'wb'))
    battle = Battle('Caravan', ['Lethomyr Darkin'], ['bandit', 'bandit', 'bandit', 'bandit captain'])
    battle.load_npcs()
    # print(battle.friendly_npc_object_set, battle.enemy_npc_object_set)
    # for npc in battle.friendly_npc_object_set:
    #     print(npc.name, npc.armor, npc.weapon, npc.secondary_weapon)
    # for npc in battle.enemy_npc_object_set:
    #     print(npc.name, npc.armor, npc.weapon, npc.secondary_weapon)
    

if __name__ == "__main__":
    main()