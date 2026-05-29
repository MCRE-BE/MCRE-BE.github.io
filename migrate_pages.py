import os
import re

src_dir = "."
dest_dir = "hugo-site/content"
langs = {"en": "en", "fr": "fr", "nl": "nl"}

files = [f for f in os.listdir(src_dir) if f.endswith(".md") and "-" in f]

for f in files:
    name, ext = os.path.splitext(f)
    parts = name.split("-")
    lang = parts[-1]
    if lang in langs:
        base_name = "-".join(parts[:-1])
        
        with open(os.path.join(src_dir, f), "r", encoding="utf-8") as file:
            content = file.read()
        
        # Remove the language link line like <p style="text-align: center;"><a href="/aboutme-en">...
        content = re.sub(r'<p style="text-align: center;">.*?</a></p>\n*', '', content)
        
        # Remove layout: page
        content = re.sub(r'layout:\s*page\n', '', content)
        
        dest_path = os.path.join(dest_dir, langs[lang], f"{base_name}.md")
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        with open(dest_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Migrated {f} to {dest_path}")
