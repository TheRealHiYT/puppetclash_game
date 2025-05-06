import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import random

# --- Global Variables ---
frames = {}
player1_character = None
player2_character = None
turn = 1  # 1 for Player 1, 2 for Player 2
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
                "Ruthless": "Damage is based on Counter total when used. Chance of becoming CONFUSED.",
                "REST": "Go to sleep and recover 25% HP.",
            }
        }
    },
    "Human": {
        "Alexander": {
            "image": r"C:\Users\LengM\OneDrive\Desktop\placeholder.png",
            "description": "Humans are the weakest, most fragile thing to be. Even a breath could kill them. It's "
                           "like the whole of reality is against them. Thus, they found strength in numbers while "
                           "still being so strongly independent. To add on, in moments of desperation, "
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
player1_hp = None
player2_hp = None
battle_text = None
p1_moves_buttons = []
p2_moves_buttons = []


# --- Functions ---
def show_frame(frame_name):
    for frame in frames.values():
        frame.pack_forget()
    frames[frame_name].pack(fill="both", expand=True)


def main_menu():
    frame = tk.Frame(homo)
    frames["Main Menu"] = frame
    frame.pack(fill="both", expand=True)

    # menu_png = Image.open(r"C:\Users\LengM\OneDrive\Desktop\maybe2.png")
    menu_png = Image.open(fp=r"./assets/placeholders/sprites/backgrounds/background_1_alt.png")
    re_menu = menu_png.resize((1123, 866), Image.LANCZOS)
    menu_img = ImageTk.PhotoImage(re_menu)

    frame.menu_img = menu_img

    back_imge = tk.Label(frame, image=menu_img)
    back_imge.place(x=0, y=0, relwidth=1, relheight=1)
    back_imge.lower()

    title_label = tk.Label(homo, text="Puppet Clash: The Game", font=("Terminal", 30, "bold"), fg="Black",
                           bg="#f0f0f0")
    title_label.place(relx=0.5, rely=0.4, anchor="center")

    starto = tk.Button(homo, text="START", font=("Terminal", 12, "bold"), width=10, height=10,
                       command=lambda: show_frame("Character Selection"))
    starto.place(relx=0.5, rely=0.6, anchor="center")


player1 = None
player2 = None


def character_selection():
    frame = tk.Frame(homo)
    frames["Character Selection"] = frame
    frame.pack(fill="both", expand=True)

    # Preview image labels
    p1_image_label = tk.Label(frame)
    p1_image_label.place(x=100, y=550)

    p2_image_label = tk.Label(frame)
    p2_image_label.place(x=750, y=550)

    # # Background image
    # bg_image = Image.open(r"C:\Users\LengM\OneDrive\Desktop\maybe2.png")
    # resized_bg = bg_image.resize((1123, 866), Image.LANCZOS)
    # bg_photo = ImageTk.PhotoImage(resized_bg)
    # frame.bg_photo = bg_photo
    #
    # bg_label = tk.Label(frame, image=bg_photo)
    # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    # bg_label.lower()

    # Layout
    left_column = tk.Frame(frame)
    right_column = tk.Frame(frame)
    left_column.place(x=50, y=100)
    right_column.place(x=600, y=100)

    info_p1 = tk.Label(frame, text="Player 1: None", font=("Terminal", 12, "bold"))
    info_p2 = tk.Label(frame, text="Player 2: None", font=("Terminal", 12, "bold"))
    info_p1.place(x=50, y=50)
    info_p2.place(x=600, y=50)

    selected_p1 = tk.StringVar()
    selected_p2 = tk.StringVar()

    # Store selected skins
    skin_vars = {}
    skin_boxes = {}

    # Example skin sets for characters
    character_skins = {
        "Nosear": ["Default", "Moon Captured", "AM"],
        "Ogel": ["Default", "Arnold", "Pyro"],
        "Ichika": ["Default", "Nihmune", "Noppera-bō"],
        "Izmir the Ruthless": ["Default", "The Devil", "Scarlett King"],
        "Alexander": ["Default", "Mafia", "Spider-Man"],
        "skeleton": ["Default", "Sans", "Real"],
        "zombie octopus": ["Default", "Wizard", "Nanana"]
    }

    def on_select(name, player_num):
        select_character(name, player_num)
        skin_choice = skin_vars.get((name, player_num), tk.StringVar()).get()

        # Update player info
        if player_num == 1:
            selected_p1.set(name)
            info_p1.config(text=f"Player 1: {name}")
        else:
            selected_p2.set(name)
            info_p2.config(text=f"Player 2: {name}")

        # Load and show character image based on selected skin

        for game_categorys in characters.values():
            if name in game_categorys:
                images = game_categorys[name]["image"]

                try:
                    image_path = images.get(skin_choice, images.get("Default"))
                    img = Image.open(image_path)
                    img = img.resize((200, 300), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)

                    if player_num == 1:
                        p1_image_label.config(image=photo)
                        p1_image_label.image = photo  # Prevent garbage collection
                    else:
                        p2_image_label.config(image=photo)
                        p2_image_label.image = photo

                except Exception as e:
                    print(f"Error loading image for {name} with skin {skin_choice}: {e}")

        # Show correct combobox, hide others for this player
        for (char, pnum), box in skin_boxes.items():
            if pnum == player_num:
                if char == name:
                    box.place(x=70 if player_num == 1 else 620, y=430)
                else:
                    box.place_forget()

    def create_category_frame(parent, category_name, characters_dict, player_num):
        group_label = tk.Label(parent, text=category_name, font=("Terminal", 14, "bold"))
        group_label.pack(pady=(10, 2))

        container = tk.Frame(parent)
        container.pack()

        for char_name in characters_dict.keys():
            btn = tk.Button(container, text=char_name, width=20, font=("Terminal", 10),
                            command=lambda n=char_name, p=player_num: on_select(n, p))
            btn.pack(padx=5, pady=3)

            # Skin var and combobox for this char/player
            var = tk.StringVar(value=character_skins.get(char_name, ["Default"])[0])
            skin_vars[(char_name, player_num)] = var

            combo = ttk.Combobox(frame, textvariable=var,
                                 values=character_skins.get(char_name, ["Default"]),
                                 state="readonly", font=("Terminal", 10), width=18)
            skin_boxes[(char_name, player_num)] = combo
            combo.place_forget()  # Initially hidden

            # 👇 THIS IS THE IMPORTANT PART 👇
            combo.bind("<<ComboboxSelected>>", lambda e, c=char_name, p=player_num: on_select(c, p))

    # Create UI
    for category, char_dict in characters.items():
        create_category_frame(left_column, category, char_dict, 1)
        create_category_frame(right_column, category, char_dict, 2)

    # Confirm button
    def confirmation():
        print("Player 1:", selected_p1.get(), "| Skin:", skin_vars.get((selected_p1.get(), 1), tk.StringVar()).get())
        print("Player 2:", selected_p2.get(), "| Skin:", skin_vars.get((selected_p2.get(), 2), tk.StringVar()).get())
        # Do whatever comes next...

    confirm_button = tk.Button(frame, text="Confirm Characters", font=("Terminal", 14, "bold"),
                               command=battle_screen)
    confirm_button.place(x=450, y=800)


def select_character(name, player_num):
    global player1_character, player2_character
    if player_num == 1:
        player1_character = name
        print(f"Player 1 selected {name}")  # Debugging
    elif player_num == 2:
        player2_character = name
        print(f"Player 2 selected {name}")  # Debugging


def start_battle():
    global player1_character, player2_character
    if player1_character and player2_character:
        battle_screen()  # Make sure the battle frame is created before attempting to access it.
        show_frame("Battle")
        setup_battle()
    else:
        messagebox.showinfo("Hey!", "Please select characters for both players.")


def setup_battle():
    global player1_hp, player2_hp, battle_text, p1_moves_buttons, p2_moves_buttons

    frame = frames["Battle"]

    # Clear any existing widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Get character details
    p1_details = None
    p2_details = None
    for category in characters.values():
        if player1_character in category:
            p1_details = category[player1_character]
        if player2_character in category:
            p2_details = category[player2_character]

    # Initialize HP
    player1_hp = p1_details['stats']['HP']
    player2_hp = p2_details['stats']['HP']

    # Display HP
    player1_hp_label = tk.Label(frame, text=f"Player 1 ({player1_character}) HP: {player1_hp}", font=("Terminal", 12))
    player1_hp_label.place(relx=0.25, rely=0.1, anchor="center")

    player2_hp_label = tk.Label(frame, text=f"Player 2 ({player2_character}) HP: {player2_hp}", font=("Terminal", 12))
    player2_hp_label.place(relx=0.75, rely=0.1, anchor="center")

    # Battle Text Display
    battle_text = tk.Text(frame, height=10, width=50, font=("Terminal", 12))
    battle_text.place(relx=0.5, rely=0.4, anchor="center")

    # Function to create move buttons
    def create_move_buttons(player_num, moves, relx, rely):
        buttons = []
        for move, description in moves.items():
            move_button = tk.Button(frame, text=move, font=("Terminal", 10),
                                    command=lambda m=move, p_num=player_num: execute_move(m, p_num))
            move_button.place(relx=relx, rely=rely, anchor="center")
            buttons.append(move_button)
            rely += 0.05
        return buttons

    # Create move buttons for each player
    p1_moves = p1_details['Movesets']
    p2_moves = p2_details['Movesets']

    p1_moves_buttons = create_move_buttons(1, p1_moves, 0.25, 0.5)
    p2_moves_buttons = create_move_buttons(2, p2_moves, 0.75, 0.5)

    # Disable Player 2's buttons initially
    for button in p2_moves_buttons:
        button.config(state=tk.DISABLED)

    # Initial turn display
    update_battle_text("Player 1's turn")


def execute_move(move, player_num):
    global player1_hp, player2_hp, turn, p1_moves_buttons, p2_moves_buttons

    # Determine character details and target
    if player_num == 1:
        attacker_name = player1_character
        attacker_details = next(
            (category[player1_character] for category in characters.values() if player1_character in category), None)
        defender_hp = player2_hp
        defender_name = player2_character
        defender_details = next(
            (category[player2_character] for category in characters.values() if player2_character in category), None)
    else:
        attacker_name = player2_character
        attacker_details = next(
            (category[player2_character] for category in characters.values() if player2_character in category), None)
        defender_hp = player1_hp
        defender_name = player1_character
        defender_details = next(
            (category[player1_character] for category in characters.values() if player1_character in category), None)

    # Get attack value
    attack_value = attacker_details['stats']['Attack']

    # Calculate damage (basic implementation)
    damage = random.randint(attack_value // 2, attack_value)  # Random damage

    # Apply damage
    if player_num == 1:
        player2_hp -= damage
        update_battle_text(
            f"Player 1's {attacker_name} used {move} and dealt {damage} damage to Player 2's {defender_name}.\n")
        player2_hp = max(0, player2_hp)  # Ensure HP doesn't go below 0
    else:
        player1_hp -= damage
        update_battle_text(
            f"Player 2's {attacker_name} used {move} and dealt {damage} damage to Player 1's {defender_name}.\n")
        player1_hp = max(0, player1_hp)  # Ensure HP doesn't go below 0

    # Update HP labels (you might need to re-get these from the frame)
    frame = frames["Battle"]
    player1_hp_label = next(
        (w for w in frame.winfo_children() if isinstance(w, tk.Label) and "Player 1" in w.cget("text")), None)
    player2_hp_label = next(
        (w for w in frame.winfo_children() if isinstance(w, tk.Label) and "Player 2" in w.cget("text")), None)
    if player1_hp_label:
        player1_hp_label.config(text=f"Player 1 ({player1_character}) HP: {player1_hp}")
    if player2_hp_label:
        player2_hp_label.config(text=f"Player 2 ({player2_character}) HP: {player2_hp}")

    # Check for win condition
    if player1_hp <= 0 or player2_hp <= 0:
        winner = attacker_name
        messagebox.showinfo("Game Over", f"{winner} wins!")
        reset_battle()
        return

    # Switch turns
    turn = 3 - player_num  # Switches between 1 and 2
    switch_turns()


def switch_turns():
    global turn, p1_moves_buttons, p2_moves_buttons

    # Disable all buttons first
    for button in p1_moves_buttons:
        button.config(state=tk.DISABLED)
    for button in p2_moves_buttons:
        button.config(state=tk.DISABLED)

    # Enable buttons for the current player
    if turn == 1:
        for button in p1_moves_buttons:
            button.config(state=tk.NORMAL)
        update_battle_text("Player 1's turn.\n")
    else:
        for button in p2_moves_buttons:
            button.config(state=tk.NORMAL)
        update_battle_text("Player 2's turn.\n")


def update_battle_text(text):
    global battle_text
    battle_text.insert(tk.END, text)
    battle_text.see(tk.END)  # Scroll to the end


def reset_battle():
    global player1_character, player2_character, player1_hp, player2_hp, turn
    player1_character = None
    player2_character = None
    player1_hp = None
    player2_hp = None
    turn = 1
    show_frame("Character Selection")


def display_character(name, character_list):
    show_frame("Character Info")
    char_info = frames["Character Info"]

    for widget in char_info.winfo_children():
        widget.destroy()

    details = next((char_list[name] for char_list in character_list.values() if name in char_list), None)
    if not details:
        print(f"Character {name} not found.")
        return

    info_text = f"{name}\n\n{details['description']}\n\nStats: {details['stats']}"
    char_label = tk.Label(char_info, text=info_text, font=("Terminal", 14), wraplength=500)
    char_label.pack(pady=20)


def character_info():
    frame = tk.Frame(homo)
    frames["Character Info"] = frame
    # No need to pack here; managed by show_frame


def battle_screen():
    frame = tk.Frame(homo)
    frames["Battle"] = frame
    # The contents will be created dynamically


# --- Main ---
homo = tk.Tk()
homo.title("Puppet Clash: The Game")
homo.geometry("1123x866")

main_menu()
character_selection()
character_info()

show_frame("Main Menu")

homo.mainloop()
