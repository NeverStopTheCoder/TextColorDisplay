import pyfiglet 

colorArray = {
    "red": "\033[1;31m",
    "orange": "\033[1;38;5;208m",
    "yellow": "\033[1;33m",
    "green": "\033[1;32m",
    "blue": "\033[1;34m",
    "purple": "\033[1;35m",
    "cyan": "\033[1;36m",
    "black": "\033[1;30m",
    "white": "\033[1;37m",
}
RESET = "\033[0m"
DIM = "\033[2m"
valid_choices = ['red','orange','yellow','green','blue','purple','cyan','black','white']

def DrawColoredText():
    while True:
        user_choice = input("Pick a Color From (red,orange,yellow,green,blue,purple,cyan,black,white): ").strip().lower()
        user_choice2 = input("What Letter: ").strip()
        user_choice3 = colorArray.get(user_choice)
        
        if user_choice in valid_choices:
            final_color = user_choice3
            tags = {
                ":R:": "\033[1;31m",
                ":O:": "\033[1;38;5;208m",
                ":Y:": "\033[1;33m",
                ":G:": "\033[1;32m",
                ":B:": "\033[1;34m",
                ":P:": "\033[1;35m",
                ":C:": "\033[1;36m",
                ":B2:": "\033[1;30m",
                ":W:": "\033[1;37m",
                ":UR:": "\033[4;31m",
                ":UO:": "\033[4;38;5;208m",
                ":UY:": "\033[4;33m",
                ":UG:": "\033[4;32m",
                ":UB:": "\033[4;34m",
                ":UP:": "\033[4;35m",
                ":UC:": "\033[4;36m",
                ":UB2:": "\033[4;30m",
                ":UW:": "\033[4;37m",
            }

            remaining_text = user_choice2
            chunks = []  

            while remaining_text:
                earliest_idx = len(remaining_text)
                earliest_tag = None
                earliest_ansi = None

                for tag, ansi_code in tags.items():
                    idx = remaining_text.find(tag)
                    if idx != -1 and idx < earliest_idx:
                        earliest_idx = idx
                        earliest_tag = tag
                        earliest_ansi = ansi_code

                if earliest_tag:
                    left_part = remaining_text[:earliest_idx]
                    if left_part:
                        chunks.append((left_part, current_color))
                    
                    current_color = earliest_ansi
                    remaining_text = remaining_text[earliest_idx + len(earliest_tag):]
                else:
                    chunks.append((remaining_text, current_color))
                    remaining_text = ""

            chunk_arts = []
            for text, color in chunks:
                art_lines = pyfiglet.figlet_format(text, font="univers").splitlines()
                chunk_arts.append((art_lines, color))

            max_rows = max(len(art[0]) for art in chunk_arts) if chunk_arts else 0

            for i in range(max_rows):
                line_output = ""
                for art_lines, color in chunk_arts:
                    row = art_lines[i] if i < len(art_lines) else ""
                    line_output += f"{color}{row}"
                print(f"{line_output}{RESET}")

            break
        else:
            print("Invalid choice. Please try again.")
