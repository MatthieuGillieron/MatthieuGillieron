
from datetime import datetime

current_date = datetime.now().strftime("%d %B %Y")

custom_message = f"On {current_date}, the choice is still ine the Matrix ⏳"

with open("README.md", "r") as file:
    content = file.readlines()

new_content = []
message_found = False
for line in content:
    if line.startswith("On") and "the choice is still ine the Matrix ⏳" in line:
        new_content.append(custom_message + "\n")  # Remplace la ligne existante
        message_found = True
    else:
        new_content.append(line)

if not message_found:
    new_content.append("\n" + custom_message + "\n")

with open("README.md", "w") as file:
    file.writelines(new_content)
