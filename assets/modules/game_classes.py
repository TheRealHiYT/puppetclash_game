from typing import Literal, Union
from os import PathLike
from random import randint

characters = {
    "\"Gods\"": {
        "Nosear": {
            "image": {
                "Default": r"./assets/sprites/characters/Nosear/Nosear.png",
                "Moon Captured": r"./assets/sprites/characters/Nosear/skins/Moon_Captured.png",
                "AM": r"./assets/sprites/characters/Nosear/skins/I_AM.png"
            },
            # The 6 ?s are for the thing I put in ./secrets/dev/characters/docs.md btw
            "description": "The ocean was a largely unexplored part of our world but in 30XX over 84.7% of the oceans\n "
                           "were uncovered. In 301X, some satellites found a corpse at the bottom of the ocean; the corpse of a\n "
                           "god. The scientific and religious world was shaken up in the discovery and many attempted the\n "
                           "dangerous trek to the sunken body. Most failed, in fact so many failed that the immense ammount of submarines\n "
                           "formed a structure akin to the Appalachian Mountains near the god.\n "
                           "This area was dubbed \"The Final Resting Place\" due to the amount of deaths in that area. Eventaully though, A lucky group would\n "
                           "make it all the way to the body and in the greatest display of disrespect,\n "
                           "they attempted to bring back the deity by forcing a newly developed form of AI,\n "
                           "Artificial General Intelligence, into the dead brain. In yet another miracle, they succeeded\n "
                           "and the god was reborn.\n Nosear. That is what it named itself. The name was meaningless;\n "
                           "just made up by scrambling up letters. Something to show how meaningless Nosear was. It\n "
                           "had no purpose nor did it deserve one. Nosear, soon after awaking, realized that it was a\n "
                           "mistake and nothing more. Just the consequences of humanity's perverse influence on life that\n "
                           "no living thing, god or not, could escape from. Nosear despises all but cannot find the energy to fully hate.\n "
                           "It was useless in that respect as well. It decided to roam the world and reflect the horrors of humanity "
                           "back as its only way of loathing. An empty hate, for it cannot feel, cannot speak, and cannot communicate for it does not know what to say.\n "
                           "Metaphorically, it has no mouth, but it desperately needs to scream.\n "
                           "\"??????\": It's the only way it should have ended. A world humans thrived on, but invevitbly lost from themselves.\n "
                           "\"??????\": They had every tool in their disposal to prevent it, bombing Nosear, banning the expeditions to him, and so much more.\n "
                           "\"??????\": But once he was awakened, humanity realized their end was near, and he would not let any human escape his wrath\n "
                           "\"??????\": 'Isn't it ironic? When granted everything, you can't do anything.'\n "
                           "\"??????\": Ah, how familiar that line is.. well even if it's overused, it's still true, isn't it?\n"
                           "\"??????\": Ironic that humanity made that line, but they never listened to themselves anyway.",

            "char_variable": list(),
            "stats": {"HP": 1500, "Attack": 23, "Defense": 1000, "Speed": 15},
            "Movesets": [
                {
                    "name": "Echo Strike",
                    "description": "Copies the opponent's last used move with a small modifier.",
                    "damage": {"value": 15, "atk_type": "Physical"},
                    "unique_effect": [
                        {"target": "opponent's last attack", "effect": "copy", "strength": "slightly weaker"}]
                },
                {
                    "name": "Mirror Guard",
                    "description": "Reduces the opponent's attack by half and reflects a quarter back.",
                    "damage": {"value": 0, "atk_type": "Counter"},
                    "unique_effect": [
                        {"target": "self", "effect": "reduce", "strength": 0.5},
                        {"target": "self", "effect": "reflect", "strength": 0.25}
                    ]
                },
                {
                    "name": "Adaptive Blitz",
                    "description": "Changes based on the opponent's last attack.",
                    "damage": {"value": 10, "atk_type": "Physical"},
                    "unique_effect": [
                        {"target": "opponent's last attack", "effect": "change", "strength": "damage"}]
                },
                {
                    "name": "Chameleon Feint",
                    "description": "Random choice of the opponent's moveset.",
                    "damage": {"value": 5, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent's moveset", "effect": "perma-copy", "strength": "random"}]
                }
            ]
        },
        "Ogel": {
            "image": {
                "Default": r".\assets\placeholders\sprites\characters\placeholder.png",
            },
            "char_variable": list(),
            "description": """\"A comforting voice\": \"Where is he?! Where's my son!?\" \n \"A misleading voice\":\n "
                           "\"He's... missing. But you don't need to worry because we'll find him soon, I promise.\"\n "
                           "\n \"Mom. Dad. I really wish you can visit me! This is like a dream; I'm playing my\n "
                           "favorite game all day! ... But I miss you guys.\"  In an attempt to retrieve the boy,\n "
                           "he was forever changed. His skin a sickeningly bright yellow with a mockery of a blue\n "
                           "shirt and lime green pants. His eyes are lifeless with a mouth forever stuck in a thin\n "
                           "lined smile. During the extraction, Ogel was playing \"Kohls Admin House\" which brought\n "
                           "the abilities of the game with him. Unfortunately, the hastily put together machine had\n "
                           "the side effect of breaking the young boy's mind. His parents tried to heal their child,\n "
                           "but couldn't save him. After all, the power of a god is in the hands of a child who still\n "
                           "believes that he's in a game. Now abandoned, \"???\" has decided to use the boy for his\n "
                           "own entertainment and put him in an arena to fight to the death.""",
            "stats": {"HP": 1000, "Attack": 15, "Defense": 2000, "Speed": 25},
            "Movesets": [
                {
                    "name": "Speed Difference",
                    "description": "A basic attack that gives priority.",
                    "damage": {"value": 12, "atk_type": "Physical"},
                    "unique_effect": [{"target": "self", "effect": "speed up", "strength": 60}]
                },
                {
                    "name": "Sacred Swords",
                    "description": "Randomly use one of the divine swords.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "divine sword", "strength": "random"}]
                },
                {
                    "name": "Can i has chezburger?",
                    "description": "Heals 15% HP.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "heal", "strength": 15}]
                },
                {
                    "name": "Boing!",
                    "description": "A basic two-hit attack with the chance to CONFUSE the opponent.",
                    "damage": {"value": 8, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "CONFUSE chance", "strength": 30}]
                }
            ]
        }
    },
    "Beasts": {
        "Ichika": {
            "image": {
                "Default": r"./assets/sprites/characters/Ichika/Ichika.png",
                "Product 12": r"./assets/sprites/characters/Ichika/skins/Product_12.png",
                "Miku": r"./assets/sprites/characters/Ichika/skins/Miku.png"
            },
            "description": "The heir of a dying clan who must find someone strong enough to match her strength so she\n "
                           "can revive her lineage. Unfortunately, Ichika is too strong. Everyone she has fought all\n "
                           "have died to her hands before she could get a scratched. So her reason for accepting the\n "
                           "invitation to the arena is to find a suitable partner from her hope of finally tasting defeat.",
            "char_variable": None,
            "stats": {"HP": 900, "Attack": 12, "Defense": 1000, "Speed": 18},
            "Movesets": [
                {
                    "name": "Stab",
                    "description": "A basic attack with the chance of inflicting BLEED.",
                    "damage": {"value": 14, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "BLEED chance", "strength": 40}]
                },
                {
                    "name": "Perfect Counter",
                    "description": "If goes second and is hit then take no damage and hit for 1.5x.",
                    "damage": {"value": 18, "atk_type": "Physical"},
                    "unique_effect": [{"target": "self", "effect": "conditional counter", "strength": (0, 1.5)}]
                },
                {
                    "name": "I'm Better",
                    "description": "Increases attack power like Swords Dance.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "attack multi", "strength": 2}]
                },
                {
                    "name": "Death Strikes",
                    "description": "Hits four times.",
                    "damage": {"value": 6, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "multi-hit", "strength": 4}]
                }
            ]
        },
        "Izmir the Ruthless": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "Izmir is the closest thing to being the strongest but it's lacking mind holds it back.",
            "char_variable": int(),
            "stats": {"HP": 850, "Attack": 20, "Defense": 1500, "Speed": 20},
            "Movesets": [
                {
                    "name": "CHOMP",
                    "description": "A basic attack with a high chance to DECAY the opponent.",
                    "damage": {"value": 22, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "DECAY chance", "strength": 75}]
                },
                {
                    "name": "NIBBLE",
                    "description": "Does little damage. Adds 1 to the Counter.",
                    "damage": {"value": 5, "atk_type": "Physical"},
                    "unique_effect": [{"target": "self", "effect": "add token", "strength": 1}]
                },
                {
                    "name": "BULLRUSH",
                    "description": "Damage scales with Counter. Chance of CONFUSION.",
                    "damage": {"value": 0, "atk_type": "Physical"},
                    "unique_effect": [
                        {"target": "opponent", "effect": "token damage", "strength": "n-tokens"},
                        {"target": "self", "effect": "CONFUSE chance", "strength": 30}
                    ]
                },
                {
                    "name": "REST",
                    "description": "Goes to sleep and recovers 25% HP.",
                    "damage": {"value": 0, "atk_type": "None"},
                    "unique_effect": [{"target": "self", "effect": "heal", "strength": 25}]
                }
            ]
        }
    },
    "Human": {
        "Alexander": {
            "image": r"./assets/sprites/characters/Alexander/Alexander.png",
            # Just saying, having people like King Sisyphus of Crete
            # would be cool for skins (also would attract ULTRAKILL fans)
            "description": "Humans are the weakest, most fragile thing to be. Even a breath could kill them. It's\n "
                           "like the whole of reality is against them. Thus, they found strength in numbers while\n "
                           "still being strong independently. To add on, in moments of desperation,\n "
                           "when they're barely holding on, a single human could face all of the hostile stars in the sky.\n "
                           "A single human could push their limits and do whatever they need to. It doesn't matter how cruel or\n "
                           "unfair reality is because they believed that they deserve to live in it. \n "
                           "\"???\": \"Fun Fact: Humans went from steel to nukes almost three times faster than it took them to go\n "
                           "from bronze to steel.\"",
            "char_variable": 20,
            "stats": {"HP": 500, "Attack": 18, "Defense": 1777, "Speed": 15},
            "Movesets": [
                {
                    "name": "Kick",
                    "description": "A basic attack that does 1.5x of normal.",
                    "damage": {"value": 18, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "damage multi", "strength": 1.5}]
                },
                {
                    "name": "Grapple",
                    "description": "Locks one random move of the opponent.",
                    "damage": {"value": 5, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent's moveset'", "effect": "lock move", "strength": "random"}]
                },
                {
                    "name": "Block",
                    "description": "Gain a good amount of defense for one turn.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "defense up", "strength": 80}]
                },
                {
                    "name": "I'm Better",
                    "description": "Boosts attack like Swords Dance.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "attack multi", "strength": 2}]
                }
            ]
        }
    },
}

print(characters["Beasts"]["Ichika"]["description"])


class Character:
    effects = {"move_effects": ["attack multi", "damage multi", "speed up", "defense up",
                                "change", "copy", "heal", "multi-hit", "CONFUSE chance",
                                "DECAY chance", "BLEED chance"],

               "unique_move_effects": ["perma-copy", "conditional counter", "lock move",
                                       "divine sword", "token damage", "add token"]}

    divine_swords = [{"name": "Firebrand", "effect": "FIRE", "damage": 25},
                     {"name": "Venomshank", "effect": "DECAY", "damage": 25},
                     {"name": "Windforce", "effect": "WINDED", "damage": 15},
                     {"name": "Darkheart", "effect": "LIFESTEAL", "damage": 20},
                     {"name": "Illumina", "effect": "JUMPER", "damage": 20},
                     {"name": "Ghostwalker", "effect": "REAPER", "damage": 35},
                     {"name": "Icedagger", "effect": "FREEZE", "damage": 35}]

    status_effects = [{"name": "CONFUSE", "effect": -1, "stat_affected": "opp turn"},
                      {"name": "DECAY", "effect": 16, "stat_affected": "opp hp", "duration": 3},
                      {"name": "BLEED", "effect": 12, "stat_affected": "opp hp", "duration": 5},
                      {"name": "FIRE", "effect": 15, "stat_affected": "opp hp", "duration": 6},
                      {"name": "WINDED", "effect": -10, "stat_affected": "opp speed", "duration": 2},
                      {"name": "LIFESTEAL", "effect": 0.5, "stat_affected": "hp"},
                      {"name": "JUMPER", "effect": 10, "stat_affected": "speed"},
                      {"name": "REAPER", "effect": 20, "stat_affected": "attack"},
                      {"name": "FREEZE", "effect": 299, "stat_affected": "opp hp"}],

    def __init__(self, race: Union[Literal["Gods"], Literal["Beasts"], Literal["Human"], Literal["Undead"]], name: str,
                 skin_list: dict[str: PathLike], hp: int, attack: int, defense: int, speed: int,
                 moveset: list[dict[str, str, dict[int, str], list[dict[str, str, Union[str, int]]]]]):
        self.__race = race
        self.__name = name
        self.__skin_list = skin_list
        self.current_effects = list()
        self.__max_hp = hp
        self.hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__speed = speed
        self.__moveset = moveset

    def get_race(self):
        return self.__race

    def get_name(self):
        return self.__name

    def get_skin_list(self):
        return self.__skin_list

    def get_max_hp(self):
        return self.__max_hp

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_speed(self):
        return self.__speed

    def get_moveset(self):
        return self.__moveset

    def add_effect(self, effect: dict, unique: bool):
        if not unique:
            self.current_effects.append(effect)

    def use_move(self, target, move_index: int):
        try:
            move_name, move_desc = self.get_moveset()[move_index]
            move_dmg, move_type = self.get_moveset()[move_index]['damage']
            move_effects = list()
            for effect in self.get_moveset()[move_index]['unique_effect']:
                move_effects.append(effect)

            if move_dmg > 0:
                for effect in move_effects:
                    sp_effect_attr = effect["effect"]
                    if sp_effect_attr in self.effects["unique_move_effects"]:
                        if sp_effect_attr == "divine sword":
                            chosen_sword = self.divine_swords[randint(0, 7)]
                            print(f"Chosen Sword: {chosen_sword}")
                            if chosen_sword["name"] == "Icedagger":
                                if randint(0, 100) <= chosen_sword["damage"]:
                                    target.take_damage(299, True)
                            else:
                                target.add_effect(self.status_effects["effect"])

        except IndexError as e:
            print(f"An IndexError ({e}) was raised! Remember, the first item in a list is at 0.")

    def take_damage(self, damage: int, defense_bypassed: bool):
        if not defense_bypassed:
            damage -= self.get_defense()
            self.hp -= damage
            self.hp = max(self.hp, 0)
        else:
            self.hp -= damage
            self.hp = max(self.hp, 0)

        return self.hp
