import os
from datetime import datetime
import hashlib

POSTS_DIR = "_posts"


def slugify(text):
    return text.lower().replace(" ", "-")


def hash_content(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def apply_layout(layout, body):

    content = ""

    for i in layout["after_intro"]:
        content += f"{{% include {i} %}}\n\n"

    for i in layout["after_h1"]:
        content += f"{{% include {i} %}}\n\n"

    content += body + "\n\n"

    for i in layout["mid"]:
        content += f"{{% include {i} %}}\n\n"

    for i in layout["before_cta"]:
        content += f"{{% include {i} %}}\n\n"

    for i in layout["footer"]:
        content += f"{{% include {i} %}}\n\n"

    return content


def build_article(article, layout, body):
    title = article.get("title", "untitled")

    content_body = apply_layout(layout, body)

    return f"# {title}\n\n{content_body}"


def export_post(article, content):

    os.makedirs(POSTS_DIR, exist_ok=True)

    slug = slugify(article.get("title", "untitled"))
    path = f"{POSTS_DIR}/{datetime.now().strftime('%Y-%m-%d')}-{slug}.md"

    new_hash = hash_content(content)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()

        if hash_content(old) == new_hash:
            print(f"SKIP {slug}")
            return

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{article['title']}\"\n")
        f.write(f"permalink: /{slug}/\n")
        f.write("layout: post\n")
        f.write(f"content_hash: {new_hash}\n")
        f.write("---\n\n")
        f.write(content)

    print(f"UPDATED {slug}")
