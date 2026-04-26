import os
import re

POSTS_DIR = "_posts"

TEMPLATE = """---
title: "{title}"
permalink: {permalink}
layout: post
---

{% include tldr-box.html %}

{% include section-in-breve.html %}

{{ content }}

{% include trust-box.html %}
"""

def extract_title_from_file(content):
    # prova a prendere title YAML
    match = re.search(r"title:\s*\"(.+?)\"", content)
    if match:
        return match.group(1)

    # fallback: prima riga H1
    match = re.search(r"#\s*(.+)", content)
    if match:
        return match.group(1)

    return "articolo-inglese"

def slugify(title):
    return (
        title.lower()
        .replace(" ", "-")
        .replace("’", "")
        .replace("'", "")
    )

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    title = extract_title_from_file(content)
    slug = slugify(title)

    permalink = f"/{slug}/"

    new_content = TEMPLATE.format(
        title=title,
        permalink=permalink
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✔ FIXED: {path}")

def main():
    for root, _, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                fix_file(path)

if __name__ == "__main__":
    main()
