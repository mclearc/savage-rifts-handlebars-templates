import os
import re
import html
from urllib.parse import unquote

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace [[Compendium...|...]] with [[...]]
    content = re.sub(r'\[\[Compendium\.[^\|]*\|([^\]]*)\]\]', r'[[\1]]', content)

    # Decode HTML entities
    content = html.unescape(content)

    # Decode URL encoded characters in image links
    content = re.sub(r'\[\[z_assets/_images/(.*?)\]\]', lambda m: f"[[z_assets/_images/{unquote(m.group(1))}]]", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    # Replace 'path/to/your/obsidian/vault' with the path to your Obsidian vault or Markdown files
    vault_path = '/Users/roambot/Library/Mobile Documents/iCloud~md~obsidian/Documents/Savage Rifts'
    process_directory(vault_path)
