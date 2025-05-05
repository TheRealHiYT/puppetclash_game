from typing import Literal, Union
from os import PathLike

characters = {
    "\"Gods\"": {
        "Nosear": {
            "image": {
                "Default": r"./assets/sprites/characters/Nosear/Nosear.png",
                "Moon Captured": r"./assets/sprites/characters/Nosear/skins/Moon_Captured.png",
                "AM": r"./assets/sprites/characters/Nosear/skins/I_AM.png"
            },
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
                           "back as its only way of loathing. An empty hate, for it cannot feel, and it cannot speak for it does not know what to say.\n "
                           "It has no mouth, but it must scream. \n"
                           "\"??????\": It's the only way it should have ended. A world humans thrived on, but lost because of their greed.\n "
                           "\"??????\": They had every tool in their disposal to prevent it, bombing Nosear, preventing the expeditions, and more.\n "
                           "\"??????\": Isn't it ironic? When granted everything, you can't do anything.\n "
                           "\"??????\": Ah, that line is a familiar one. Well even if it's overused, it's still true, isn't it?",
            # The 6 ?s are for the thing I put in READ.md btw
            "stats": {"HP": 1500, "Attack": 23, "Defense": 1000, "Speed": 15},
            "Movesets": [
                {
                    "name": "Echo Strike",
                    "description": "Copies the opponent's last used move with a small modifier.",
                    "damage": {"value": 15, "atk_type": "Physical"},
                    "unique_effect": [
                        {"target": "opponent's Last attack", "effect": "copy", "strength": "slightly weaker"}]
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
                        {"target": "opponent's last attack", "effect": "change", "strength": "base damage"}]
                },
                {
                    "name": "Chameleon Feint",
                    "description": "Random choice of the opponent's moveset.",
                    "damage": {"value": 5, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent's moveset", "effect": "copy", "strength": "random"}]
                }
            ]
        },
        "Ogel": {
            "image": {
                "Default": r".\assets\placeholders\sprites\characters\placeholder.png",
            },
            "description": """\"A comforting voice\": \"Where is he?! Where's my son!?\" \n \"A misleading voice\": "
                           "\"He's... missing. But you don't need to worry because we'll find him soon, I promise.\" "
                           "\n \"Mom. Dad. I really wish you can visit me! This is like a dream; I'm playing my "
                           "favorite game all day! ... But I miss you guys.\"  In an attempt to retrieve the boy, "
                           "he was forever changed. His skin a sickeningly bright yellow with a mockery of a blue "
                           "shirt and lime green pants. His eyes are lifeless with a mouth forever stuck in a thin "
                           "lined smile. During the extraction, Ogel was playing \"Kohls Admin House\" which brought "
                           "the abilities of the game with him. Unfortunately, the hastily put together machine had "
                           "the side effect of breaking the young boy's mind. His parents tried to heal their child, "
                           "but couldn't save him. After all, the power of a god is in the hands of a child who still "
                           "believes that he's in a game. Now abandoned, \"???\" has decided to use the boy for his "
                           "own entertainment and put him in an arena to fight to the death.""",
            "stats": {"HP": 1000, "Attack": 15, "Defense": 2000, "Speed": 25},
            "Movesets": [
                {
                    "name": "Speed Difference",
                    "description": "A basic attack with +1 priority.",
                    "damage": {"value": 12, "atk_type": "Physical"},
                    "unique_effect": [{"target": "self", "effect": "priority", "strength": "+1"}]
                },
                {
                    "name": "Sacred Swords",
                    "description": "Random choice of the divine swords.",
                    "damage": {"value": 0, "atk_type": "Special"},
                    "unique_effect": [{"target": "self", "effect": "random", "strength": "divine sword"}]
                },
                {
                    "name": "Can i has chezburger?",
                    "description": "Heals 15% HP.",
                    "damage": {"value": 0, "atk_type": "Buff"},
                    "unique_effect": [{"target": "self", "effect": "heal", "strength": 15}]
                },
                {
                    "name": "Boing!",
                    "description": "A basic two-hit attack with the chance to CONFUSE the opponent.",
                    "damage": {"value": 8, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "CONFUSE", "strength": 30}]
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
            "description": "...",
            "stats": {"HP": 900, "Attack": 12, "Defense": 1000, "Speed": 18},
            "Movesets": [
                {
                    "name": "Stab",
                    "description": "A basic attack with the chance of inflicting BLEED.",
                    "damage": {"value": 14, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "BLEED", "strength": 40}]
                },
                {
                    "name": "Perfect Counter",
                    "description": "If goes second and is hit then take no damage and hit for 1.5x.",
                    "damage": {"value": 18, "atk_type": "Counter"},
                    "unique_effect": [{"target": "self", "effect": "conditional counter", "strength": "1.5x"}]
                },
                {
                    "name": "I'm Better",
                    "description": "Increases attack power like Swords Dance.",
                    "damage": {"value": 0, "atk_type": "Buff"},
                    "unique_effect": [{"target": "self", "effect": "attack up", "strength": "2x"}]
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
            "description": "...",
            "stats": {"HP": 850, "Attack": 20, "Defense": 1500, "Speed": 10},
            "Movesets": [
                {
                    "name": "CHOMP",
                    "description": "A basic attack with a high chance to DECAY the opponent.",
                    "damage": {"value": 22, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "DECAY", "strength": 75}]
                },
                {
                    "name": "NIBBLE",
                    "description": "Does little damage. Adds 1 to the Counter.",
                    "damage": {"value": 5, "atk_type": "Physical"},
                    "unique_effect": [{"target": "self", "effect": "Counter", "strength": 1}]
                },
                {
                    "name": "BULLRUSH",
                    "description": "Damage scales with Counter. Chance of CONFUSION.",
                    "damage": {"value": 0, "atk_type": "Physical"},
                    "unique_effect": [
                        {"target": "opponent", "effect": "scaling damage", "strength": "Counter"},
                        {"target": "self", "effect": "CONFUSE", "strength": 30}
                    ]
                },
                {
                    "name": "REST",
                    "description": "Goes to sleep and recovers 25% HP.",
                    "damage": {"value": 0, "atk_type": "None"},
                    "unique_effect": [{"target": "self", "effect": "heal %", "strength": 25}]
                }
            ]
        }
    },
    "Human": {
        "Alexander": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "...",
            "stats": {"HP": 500, "Attack": 18, "Defense": 1777, "Speed": 15},
            "Movesets": [
                {
                    "name": "Kick",
                    "description": "A basic attack that does 1.5x of normal.",
                    "damage": {"value": 18, "atk_type": "Physical"},
                    "unique_effect": [{"target": "opponent", "effect": "dmg_multiply", "strength": 1.5}]
                },
                {
                    "name": "Grapple",
                    "description": "Locks one random move of the opponent.",
                    "damage": {"value": 5, "atk_type": "Control"},
                    "unique_effect": [{"target": "opponent", "effect": "lock move", "strength": "random"}]
                },
                {
                    "name": "Block",
                    "description": "Gain a good amount of defense for one turn.",
                    "damage": {"value": 0, "atk_type": "Buff"},
                    "unique_effect": [{"target": "self", "effect": "defense up", "strength": ("a", 80)}]
                },
                {
                    "name": "I'm Better",
                    "description": "Boosts attack like Swords Dance.",
                    "damage": {"value": 0, "atk_type": "Buff"},
                    "unique_effect": [{"target": "self", "effect": "attack", "strength": ("m", 2)}]
                }
            ]
        }
    },
}

print(characters["Beasts"]["Ichika"]["description"])


class Character:
    def __init__(self, race: Union[Literal["Gods"], Literal["Beasts"], Literal["Human"], Literal["Undead"]], name: str,
                 skin_list: dict[str: PathLike], hp: int, attack: int, defense: int, speed: int,
                 moveset: list[dict[str, str, dict[int, str], list[dict[str, str, Union[str, int]]]]]):
        self.__race = race
        self.__name = name
        self.__skin_list = skin_list
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

    def get_hp(self):
        return self.__max_hp

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_speed(self):
        return self.__speed

    def get_moveset(self):
        return self.__moveset

    def use_move(self, target, move_index: int):
        try:
            move_name, move_desc = self.get_moveset()[move_index]
            move_dmg, move_type = self.get_moveset()[move_index]['damage']
            move_effects = list()
            for effect in self.get_moveset()[move_index]['unique_effect']:
                move_effects.append(effect)

            if move_dmg > 0:
                for effect in move_effects:
                    c_effect_attr = effect["effect"]
                    c_move_dmg = self.get_moveset()[move_index]["unique_effect"][0]["strength"]


        except IndexError as e:
            print(f"An IndexError ({e}) was raised! Remember, the first item in a list is at 0.")
