import re
from datetime import datetime

readme_file = "README.md"

with open(readme_file, "r") as file:
    content = file.read()

new_date = datetime.now().strftime("%d %B %Y")
updated_content = re.sub(r"On \d{1,2} \w+ \d{4}", f"On {new_date}", content)

if updated_content != content:
    with open(readme_file, "w") as file:
        file.write(updated_content)
    print("README.md updated.")
else:
    print("No changes made.")
