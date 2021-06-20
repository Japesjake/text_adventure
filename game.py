import os, pickle, random

class Data():
    def __init__(self):
        self.install_npcs()
        self.install_armor()
        self.install_weapons()
        self.install_player('JP', 'plate', 'longsword', 'fist')
    def install_npc(self, object):
        pickle.dump(object, open(os.path.join('data','npcs', object.name + '.p'),'wb'))
    def install_armor_piece(self, object):
        pickle.dump(object, open(os.path.join('data','items', 'armor', object.name + '.p'),'wb'))   
    def install_weapon(self, object):
        pickle.dump(object, open(os.path.join('data','items', 'weapons', object.name + '.p'),'wb'))
    def install_battle(self, object):
        pickle.dump(object, open(os.path.join('data','battles', object.name + '.p'),'wb'))               
    def install_npcs(self):
        self.install_npc(Npc('Lethomyr Darkin', 'plate', 'longsword', 'fist'))
        self.install_npc(Npc('bandit captain', 'studded leather', 'two-handed axe', 'fist'))
        self.install_npc(Npc('bandit', 'leather', 'axe', 'round wooden shield'))
        # self.install_npc(Npc('name', 'armor', 'weapon', 'secweapon'))
    def install_player(self, name, armor, weapon, secondary_weapon):
        pickle.dump(Player(name, armor, weapon, secondary_weapon), open(os.path.join('data', 'player.p'),'wb'))
    def install_armor(self):
        self.install_armor_piece(Armor('leather', '2'))
        self.install_armor_piece(Armor('plate', 5))
        self.install_armor_piece(Armor('studded leather', '3'))
        # self.install_armor_piece(Armor('name', armor class))
    def install_weapons(self):
        self.install_weapon(Weapon('axe', 6, 'chopping'))        
        self.install_weapon(Weapon('fist', 2, 'raw'))        
        self.install_weapon(Weapon('longsword', 10, 'piercing'))        
        self.install_weapon(Weapon('round wooden shield', 0, 'shield'))        
        self.install_weapon(Weapon('two-handed axe', 12, 'chopping'))        
        # self.install_weapon(Weapon('name', damage, 'type'))
    def install_battles():
        install_battle(Battle('Caravan', ['Lethomyr Darkin'], ['bandit', 'bandit', 'bandit', 'bandit captain']))
    def load(self, name):
        for subdir, dirs, files in os.walk(r'.\data'):
            for filename in files:
                if name + '.p' == filename:
                    path = subdir + os.sep + filename
                    return pickle.load(open(path,'rb'))


class Caravan():
    def play():
        print('You are escorting a caravan when bandits attack.')
    def battle():
        battle = load

class Battle():
    def __init__(self, name, friendly_npc_string_list, enemy_npc_string_list):
        self.name = name
        self.friendly_npc_strings_list = friendly_npc_string_list
        self.enemy_npc_strings_list = enemy_npc_string_list
        self.npc_strings_list = friendly_npc_string_list + enemy_npc_string_list
        self.npc_objects = set()
    def load_objects(self):
        self.load_npcs()
        self.load_armor()
        self.load_weapons()
        self.load_secondary_weapons()
    def load_npcs(self):
        for npc_string in self.npc_strings_list:
            self.npc_objects.add(pickle.load(open(os.path.join('data','npcs', npc_string + '.p'),'rb')))
    def load_player(self):
        self.npc_objects.add(pickle.load(open(os.path.join('data','npcs', 'player.p'),'rb')))
    def load_armor(self):
        for npc in self.npc_objects:
            npc.armor = data.load(npc.armor)
    def load_weapons(self):
        for npc in self.npc_objects:
            npc.weapon = data.load(npc.weapon)
    def load_secondary_weapons(self):
        for npc in self.npc_objects:
            npc.secondary_weapon = data.load(npc.secondary_weapon)
    def start(self):
        self.npc_turn_order = list(self.npc_objects.copy())
        random.shuffle(self.npc_turn_order)
        for npc in self.npc_turn_order:
            pass
            
                    



            

class Player():
    def __init__(self, name, armor, weapon, secondary_weapon):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.health = 100

class Npc():
    def __init__(self, name, armor, weapon, secondary_weapon):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.health = 100

class Armor():
    def __init__(self, name, armor_class):
        self.name = name
        self.armor_class = armor_class  

class Weapon():
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.damage_type = type       

def main():
    global data
    data = Data()
    # data.install_npcs()
    battle = Battle('Caravan', ['Lethomyr Darkin'], ['bandit', 'bandit', 'bandit', 'bandit captain'])
    battle.load_objects()
    battle.start()
    for npc in battle.npc_objects:
        print(npc.name, npc.armor, npc.weapon, npc.secondary_weapon)
if __name__ == "__main__":
    main()