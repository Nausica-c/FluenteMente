import yaml
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from engine.layout_engine import generate_layout
from engine.content_engine import generate_body
from engine.article_builder import build_article, export_post

INPUT_FILE = "_data/articles.yml"
OUTPUT_FILE = "_data/articles-linked.yml"


def load_articles():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def main():
    articles = load_articles()
    output = []

    for a in articles:

        a["cluster"] = a.get("cluster", "base")
        a["funnel"] = a.get("funnel", "tofu")

        if not a.get("seed"):
            a["seed"] = random.randint(1000, 9999)

        # 1. layout decision
        layout = generate_layout(a["cluster"], a["funnel"])

        # 2. content generation
        body = generate_body(a)

        # 3. final assembly
        final_article = build_article(a, layout, body)

        # 4. export markdown
        export_post(a, final_article)

        a["final_article"] = final_article
        a["layout"] = layout

        output.append(a)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(output, f, allow_unicode=True, sort_keys=False)

    print("🚀 BUILD COMPLETE")


if __name__ == "__main__":
    main()
