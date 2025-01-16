import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import customtkinter
import requests
from io import BytesIO

def show_page(page):
    page.tkraise()

def fetch_and_display_pokemon(pokemon_name, page):
    if not pokemon_name:
        pokemon_name_label.config(text="Error fetching Pokémon list!")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon = response.json()
        update_pokemon_info(pokemon, page)
    else:
        pokemon_name_label.config(text="Error fetching Pokémon details!")

def update_pokemon_info(pokemon, page):
    # Clear previous info
    pokemon_image_label.config(image=None)
    pokemon_name_label.config(text="")
    pokemon_abilities_label.config(text="")
    pokemon_height_label.config(text="")
    pokemon_weight_label.config(text="")
    pokemon_types_label.config(text="")

    # Update new Pokémon info
    pokemon_name_label.config(text=f"Name: {pokemon['name'].capitalize()}")
    pokemon_abilities_label.config(text=f"Abilities: {', '.join(a['ability']['name'] for a in pokemon['abilities'])}")
    pokemon_height_label.config(text=f"Height: {pokemon['height'] / 10} m")
    pokemon_weight_label.config(text=f"Weight: {pokemon['weight'] / 10} kg")
    pokemon_types_label.config(text=f"Types: {', '.join(t['type']['name'].capitalize() for t in pokemon['types'])}")

    # Update the Pokémon image
    image_url = pokemon['sprites']['other']['official-artwork']['front_default']
    if image_url:
        pokemon_image = load_image(image_url, (500, 500))
        if pokemon_image:
            pokemon_image_label.config(image=pokemon_image)
            pokemon_image_label.image = pokemon_image
    
    # Show the details page
    show_page(page)

def load_image(url, size):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
    return None

def fetch_pokemon_list():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    print("Error fetching Pokémon list.")
    return []

def on_combobox_select(event):
    selected_pokemon = combobox.get()
    fetch_and_display_pokemon(selected_pokemon, page3_1)

pokemon_list = ['Pikachu', 'Charizard', 'Bulbasaur', 'Squirtle', 'Jigglypuff', 'Meowth', 'Eevee', 'Snorlax', 'Mewtwo']

def show_selected_pokemon(pokemon_name):
    fetch_and_display_pokemon(pokemon_name)
    show_page(page2_2)

root = customtkinter.CTk()
root.title("Pokemon")
root.geometry("1300x800")

pokemon_names = fetch_pokemon_list()
bg_color = "#38b6ff"
main_button_color = "#feca05"
font_color = "white"

root.configure(bg=bg_color)

style1 = font.Font(size=35)
style2 = font.Font(size=15)
style3 = font.Font(size=10)

pages = [tk.Frame(root, bg=bg_color) for _ in range(7)]
page1, page2, page2_1, page2_2, page3, page3_1, page4 = pages

for page in pages:
    page.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#load images
logo_img = ImageTk.PhotoImage(Image.open(r'C:\Users\princ\OneDrive\Documents\programming\ASSETS\PKLOGO.png').resize((800, 350), Image.LANCZOS))
poke_ball = ImageTk.PhotoImage(Image.open(r'C:\Users\princ\OneDrive\Documents\programming\ASSETS\PKBALL.png').resize((230, 230), Image.LANCZOS))
big_ball_img = ImageTk.PhotoImage(Image.open(r'C:\Users\princ\OneDrive\Documents\programming\ASSETS\PKBALL.png').resize((200, 200), Image.LANCZOS))
smaller_poke_img = ImageTk.PhotoImage(Image.open(r'C:\Users\princ\OneDrive\Documents\programming\ASSETS\PKLOGO.png').resize((230, 88), Image.LANCZOS))
page2_img = ImageTk.PhotoImage(Image.open(r"C:\Users\princ\OneDrive\Documents\programming\ASSETS\PG2.png").resize((500, 700), Image.LANCZOS))
back_button = ImageTk.PhotoImage(Image.open(r"C:\Users\princ\OneDrive\Documents\programming\ASSETS\arrow.png").resize((30, 30), Image.LANCZOS))
page3_img = ImageTk.PhotoImage(Image.open(r"C:\Users\princ\OneDrive\Documents\programming\ASSETS\PG3.png").resize((900, 400), Image.LANCZOS))

#page 1
tk.Label(page1, image=logo_img, bg=bg_color).place(relx=0.5, rely=0.35, anchor='center')
tk.Button(page1, image=poke_ball, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color, command=lambda: show_page(page2)).place(relx=0.5, rely=0.63, anchor='center')

#page2
tk.Label(page2, image=smaller_poke_img, bg=bg_color).place(relx=0.5, rely=0.1, anchor='center')
tk.Label(page2, image=page2_img, bg=bg_color).place(relx=0.05, rely=0.2)
tk.Label(page2, text="GET YOUR POKEMON!", font=style1, bg=bg_color, fg=font_color).place(relx=0.45, rely=0.45)
customtkinter.CTkButton(page2, text="CLICK HERE", command=lambda: show_page(page2_1), fg_color=main_button_color, text_color=font_color).place(relx=0.45, rely=0.55)
customtkinter.CTkButton(page2, text="", command=lambda: show_page(page2), fg_color=main_button_color, width=40, height=10).place(relx=0.45, rely=0.95,anchor='center')
customtkinter.CTkButton(page2, text="", command=lambda: show_page(page3), fg_color=font_color, width=40, height=10).place(relx=0.5, rely=0.95,anchor='center')
customtkinter.CTkButton(page2, text="", command=lambda: show_page(page4), fg_color=font_color, width=40, height=10).place(relx=0.55, rely=0.95,anchor='center')

# Page 2_1 content
tk.Label(page2_1, image=smaller_poke_img, bg=bg_color).place(relx=0.5, rely=0.1, anchor='center')
customtkinter.CTkButton(page2_1, text="", image=back_button, fg_color=bg_color, text_color=bg_color, hover_color=main_button_color, command=lambda: show_page(page2)).place(relx=0.05, rely=0.1)
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.35, rely=0.3, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.5, rely=0.3, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.65, rely=0.3, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.35, rely=0.5, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.5, rely=0.5, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.65, rely=0.5, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.35, rely=0.7, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.5, rely=0.7, anchor='center')
tk.Button(page2_1, image=big_ball_img, bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color).place(relx=0.65, rely=0.7, anchor='center')
tk.Label(page2_1, text="PRESS THE POKE BALL", font=style2, bg=bg_color, fg=font_color).place(relx=0.5, rely=0.9, anchor='center')
for i, pokemon in enumerate(pokemon_list):
    row = i // 3
    col = i % 3
    x = 0.35 + col * 0.15
    y = 0.3 + row * 0.2
    
    # Load Pokemon image (you'll need to have these images saved)
    pokemon_img = ImageTk.PhotoImage(Image.open(f'path/to/{pokemon.lower()}.png').resize((100, 100), Image.LANCZOS))
    
    # Create button with Pokemon image and name
    button = tk.Button(page2_1, image=pokemon_img, text=pokemon, compound=tk.TOP,
                       bg=bg_color, borderwidth=0, relief='flat', activebackground=bg_color,
                       command=lambda name=pokemon: show_selected_pokemon(name))
    button.image = pokemon_img  # Keep a reference to prevent garbage collection
    button.place(relx=x, rely=y, anchor='center')

# Remove the existing "PRESS THE POKE BALL" label

# Page 2_2 content
tk.Label(page2_2, image=smaller_poke_img, bg=bg_color).place(relx=0.5, rely=0.1, anchor='center')
customtkinter.CTkButton(page2_2,  text="", image=back_button, fg_color=bg_color, text_color=bg_color, hover_color=main_button_color, command=lambda:show_page(page2)).place(relx=0.05, rely=0.1)


tk.Label(page3, image=page3_img, bg=bg_color).place(relx=0.5, rely=0.55, anchor='center')
tk.Label(page3, text="SEARCH A POKEMON", font=style1, fg=font_color, bg=bg_color).place(relx=0.5, rely=0.25, anchor='center')
customtkinter.CTkButton(page3, text="CLICK HERE", command=lambda: show_page(page3_1), fg_color=main_button_color, text_color=font_color).place(relx=0.45, rely=0.8)
tk.Label(page3, image=smaller_poke_img, bg=bg_color).place(relx=0.5, rely=0.1, anchor='center')
customtkinter.CTkButton(page3, text="", command=lambda: show_page(page2), fg_color=font_color, width=40, height=10).place(relx=0.45, rely=0.95,anchor='center')
customtkinter.CTkButton(page3, text="", command=lambda: show_page(page3), fg_color=main_button_color, width=40, height=10).place(relx=0.5, rely=0.95,anchor='center')
customtkinter.CTkButton(page3, text="", command=lambda: show_page(page4), fg_color=font_color, width=40, height=10).place(relx=0.55, rely=0.95,anchor='center')

tk.Label(page3_1, image=smaller_poke_img, bg=bg_color).grid(row=0, column=0, pady=20, columnspan=2)

customtkinter.CTkButton(page3_1, text="", image=back_button, fg_color=bg_color, text_color=bg_color, hover_color=main_button_color, command=lambda: show_page(page3)).grid(row=0, column=1, padx=10, pady=10, sticky='w')

combobox = ttk.Combobox(page3_1, values=pokemon_names, state="normal", width=20)
combobox.grid(row=1, column=0, pady=10, columnspan=2)

pokemon_name_label = tk.Label(page3_1, font=style2, bg=bg_color, fg=font_color)
pokemon_name_label.grid(row=2, column=0, pady=5, columnspan=2)

pokemon_image_label = tk.Label(page3_1, bg=bg_color)
pokemon_image_label.grid(row=3, column=0, pady=10, columnspan=2)

pokemon_abilities_label = tk.Label(page3_1, font=style2, bg=bg_color, fg=font_color)
pokemon_abilities_label.grid(row=4, column=0, pady=5, columnspan=2)

pokemon_height_label = tk.Label(page3_1, font=style2, bg=bg_color, fg=font_color)
pokemon_height_label.grid(row=5, column=0, pady=5, columnspan=2)

pokemon_weight_label = tk.Label(page3_1, font=style2, bg=bg_color, fg=font_color)
pokemon_weight_label.grid(row=6, column=0, pady=5, columnspan=2)

pokemon_types_label = tk.Label(page3_1, font=style2, bg=bg_color, fg=font_color)
pokemon_types_label.grid(row=7, column=0, pady=5, columnspan=2)

combobox.bind("<<ComboboxSelected>>", on_combobox_select)

tk.Label(page4, image=smaller_poke_img, bg=bg_color).place(relx=0.5, rely=0.1, anchor='center')
customtkinter.CTkButton(page4, text="", command=lambda: show_page(page2), fg_color=font_color, width=40, height=10).place(relx=0.45, rely=0.95,anchor='center')
customtkinter.CTkButton(page4, text="", command=lambda: show_page(page3), fg_color=font_color, width=40, height=10).place(relx=0.5, rely=0.95,anchor='center')
customtkinter.CTkButton(page4, text="", command=lambda: show_page(page4), fg_color=main_button_color, width=40, height=10).place(relx=0.55, rely=0.95,anchor='center')

show_page(page1)
root.mainloop()
