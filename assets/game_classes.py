from typing import Literal, Union
from os import PathLike

characters = {
    "\"Gods\"": {
        "Nosear": {
            "image": {
                "Default": r"C:\Users\LengM\OneDrive\Desktop\skkins\Nosear\Nosear.png",
                "Moon Captured": r"C:\Users\LengM\OneDrive\Desktop\skkins\Nosear\Moon_Captured.png",
                "AM": r"C:\Users\LengM\OneDrive\Desktop\skkins\Nosear\I_AM.png"
            },
            "description": "The ocean was a largely unexplored part of our world but in 30XX over 84.7% of the oceans "
                           "was uncovered. There a special corpse found at the bottom of the ocean; the corpse of a "
                           "god. The scientific and religious world was shaken up in the discovery and many made to "
                           "dangerous trek to the sunken body. So much so that mountains of submarines piled near the "
                           "god to form what would soon be called \"The Final Resting Place\". A lucky group would "
                           "soon make their way to the body and, in the greatest display of disrespect, "
                           "they attempted to bring back the deity by forcing a newly developed form of AI, "
                           "Artificial General Intelligence, into the dead brain. In another miracle, they succeeded "
                           "and the god was reborn.\n Nosear. That is what it named itself. The name was meaningless; "
                           "just made up by scrambling up letters. Something to show how meaningless Nosear was. It "
                           "had no purpose nor did it deserve one. Nosear, soon after awaking, realized that it was a "
                           "mistake and nothing more. Just the result of humanity's perverse influence on life that "
                           "no god could escape. Nosear despises all but cannot find the energy to fully hate. It was "
                           "useless in that respect as well. To roam the world and reflect the horrors of humanity "
                           "back is its only way of loathing.",
            "stats": {"HP": 1500, "Attack": 23, "Defense": 1000, "Speed": 15},  # average overall except low speed
            "Movesets": {
                "Echo Strike": "Copies the opponent's last used move with a small modifier.",
                "Mirror Guard": "Reduces the opponent's attack by half and reflects a quarter back.",
                "Adaptive Blitz": "Changes based on the opponent's last attack.",
                "Chameleon Feint": "Random choice of the opponent's moveset."
            }
        },
        "Ogel": {
            "image": {
                "Default": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            },
            "description": "\"A comforting voice\": \"Where is he?! Where's my son!?\" \n \"A misleading voice\": "
                           "\"He's... missing. But you don't need to worry because we'll find him soon, I promise.\" "
                           "\n \"Mom. Dad. I really wish you can vist me! This is like a dream; I'm playing my "
                           "favorite game all day! ... But I miss you guys.\"  In an attempt to retrieve the boy, "
                           "he was forever changed. His skin a sickeningly bright yellow with a mockery of a blue "
                           "shirt and lime green pants. His eyes are lifeless with a mouth forever stuck in a thin "
                           "lined smile. During the extraction, Ogel was playing \"Kohls Admin House\" which brought "
                           "the abilities of the game with him. Unfortunately, the hastily put together machine had "
                           "the side effect of breaking the young boy's mind. His parents tried to heal their child, "
                           "but couldn't save him. After all, the power of a god is in the hands of a child who still "
                           "believes that he's in a game. Now abandoned, \"???\" has decided to use the boy for his "
                           "own entertainment and put him in an arena to fight to the death. ",
            "stats": {"HP": 1000, "Attack": 15, "Defense": 2000, "Speed": 25},
            "Movesets": {
                "Speed Difference": "A basic attack with +1 priority.",
                "Sacred Swords": "Random choice of the divine swords.",
                "Can i has chezburger?": "Heals 15% HP.",
                "Boing!": "A basic two-hit attack with the chance to CONFUSE the opponent."
            }
        }
    },
    "Beasts": {
        "Ichika": {
            "image": {"Default": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
                      "Product 12": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
                      "Miku": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png"
                      },
            "description": "The heir of a dying clan who must find someone strong enough to match her strength so she "
                           "can revive her lineage. Unfortunately, Ichika is too strong. Everyone she has fought all "
                           "have died to her hands before she could get a scratched. So her appearance in this game "
                           "is both to find a suitable partner and the hope for defeat.",
            "stats": {"HP": 900, "Attack": 12, "Defense": 1000, "Speed": 18},
            "Movesets": {
                "Stab": "A basic attack with the chance of inflicting BLEED.",
                "Perfect Counter": "If is goes second and is hit then take no damage and hit for 1.5x of basic attack.",
                "I'm Better": "like swords dance",
                "Death Strikes": "Hits four times"
            }
        },
        "Izmir the Ruthless": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "Izmir is the closest thing to being the strongest but it's lacking mind holds it back "
                           "severely.",
            "stats": {"HP": 850, "Attack": 20, "Defense": 1500, "Speed": 10},
            "Movesets": {
                "CHOMP": "A basic attack with a high chance to DECAY the opponent.",
                "NIBBLE": "Does little damage. Adds 1 to the Counter.",
                "BULLRUSH": "Damage is based on Counter total when used. Chance of becoming CONFUSED.",
                "REST": "Go to sleep and recover 25% HP.",
            }
        }
    },
    "Human": {
        "Alexander": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "Humans are the weakest, most fragile thing to be. Even a breath could kill them. It's "
                           "like the whole of reality is against them. Thus, they found strength in numbers while "
                           "still being strong independently. To add on, in moments of desperation, "
                           "or determination, a single human could face all of the hostile stars in the sky. A single "
                           "human could push their limits and do whatever they need to. It doesn't matter how cruel "
                           "reality is because they have decided that they deserve to be in it. \n \"???\": \"Fun "
                           "Fact: Humans went from steel to nukes almost three times faster than it took them to go "
                           "from bronze to steel.\"",
            "stats": {"HP": 500, "Attack": 18, "Defense": 1777, "Speed": 15},
            "Movesets": {
                "Kick": "A basic attack that does 1.5x of normal.",
                "Grapple": "Locks one random move of the opponent.",
                "Block": "For one turn gain a good amount of defense.",
                "I'm Better": "like swords dance"
            }
        }
    },
    "Undead": {
        "skeleton": {
            "image": {
                "Default": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
                "Sans": r"C:\Users\LengM\OneDrive\Desktop\skkins\Skeleton\Comic_Sans.png",
                "Real": r"C:\Users\LengM\OneDrive\Desktop\skkins\Skeleton\Skeleton.png"
            },
            "description": "An unnamed undead who stumbled into fighting.",
            "stats": {"HP": 1250, "Attack": 20, "Defense": 400, "Speed": 16},
            "Movesets": {
                "Life Steal": "Takes 10% of opponent's HP for your own.",
                "Diamond Bite": "Basic Attack that goes through armor",
                "Angry Glare": "Chance to either PARALYZE or DECAY.",
                "MILK!": "Defense buff."
            }
        },
        "zombie octopus": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "Just some octopuses stuck onto a zombie. Nothing special.",
            "stats": {"HP": 2500, "Attack": 17, "Defense": 0, "Speed": 15},
            "Movesets": {
                "Octo Throw": "Deals 10% of opponent's HP with a 65% of SKIPPING opponent's turn.",
                "Spray": "Sprays poison at enemy dealing 15% HP with 45% chance of POISONING.",
                "Beef Up": "Gains 15% more HP.",
                "Intimidate": "Chance to raise your attack by 20% or lower your opponent's attack by 25%."
            }
        }
    }
}


class Character:
    def __init__(self, race: Union[Literal["Gods"], Literal["Beasts"], Literal["Human"], Literal["Undead"]], name: str, skin_list: dict[str: PathLike], hp: int, attack: int, defense: int, speed: int, moveset: dict[list[str, int, dict[str, int]]]):
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

    def use_move(self, target, move_name: str, move_dmg: int, move_effect: str):
        target.hp -= (self.get_attack() + move_dmg) - target.get_defense()
