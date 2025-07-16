from Enemy import *
from Zombie import *
from Ogre import *
from Weapon import *
from Hero import *

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()
#     e2.talk()

#     while e1.health_points > 0 and e2.health_points > 0:

#         print('--------')
#         e1.special_attack()
#         e2.special_attack()
#         print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
#         print(f'{e2.get_type_of_enemy()}: {e1.health_points} HP left')
#         e2.attack()
#         e1.health_points -= e2.attack_damage
#         e1.attack()
#         e2.health_points  -= e1.attack_damage

#         if e1.health_points > 0:
#             print(f'{e1.get_type_of_enemy()} wins!')
#         else:
#             print(f'{e2.get_type_of_enemy()} wins!')



zombie = Zombie(100, 10)
ogre = Ogre(200, 3)

# print(zombie.talk())
# print(ogre.talk())

# battle(zombie, ogre)

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:

        print('--------')
        enemy.special_attack()
        print(f'Hero {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {hero.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points  -= hero.attack_damage

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


hero = Hero(10, 1)
zombie =  Zombie(10, 1)
weapon = Weapon('Sword', 200)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, ogre)