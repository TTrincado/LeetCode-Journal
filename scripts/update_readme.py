import os
import re

ROOT_DIR = '.'
README_PATH = 'README.md'
EXTENSIONS = {'.py'}
IGNORE_DIRS = {'.git', '.github', 'scripts', '__pycache__', '.idea', '.vscode'}


def get_stats():
    total_solved = 0
    category_counts = {}

    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in EXTENSIONS:
                total_solved += 1
                path_parts = os.path.normpath(root).split(os.sep)
                if len(path_parts) > 1:
                    category = path_parts[1]
                    if len(path_parts) > 2 and "neetcode" in path_parts[1].lower():
                        category = path_parts[2]
                    category_counts[category] = category_counts.get(
                        category, 0) + 1

    if category_counts:
        top_category = max(category_counts, key=category_counts.get)
        top_count = category_counts[top_category]
    else:
        top_category = "None"
        top_count = 0

    return total_solved, top_category, top_count


def update_readme(total, top_cat, top_cat_count):
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    stats_text = (
        "\n"
        f"![Solved](https://img.shields.io/badge/Solved-{total}-blue?style=for-the-badge&logo=leetcode)\n"
        f"![Focus](https://img.shields.io/badge/Main_Focus-{top_cat}_({top_cat_count})-orange?style=for-the-badge)\n"
    )

    new_content = re.sub(
        r'<!-- STATS:START -->.*?<!-- STATS:END -->',
        f'<!-- STATS:START -->{stats_text}<!-- STATS:END -->',
        content,
        flags=re.DOTALL
    )

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)


if __name__ == "__main__":
    total, top_cat, top_count = get_stats()
    print(f"Total: {total}, Top Category: {top_cat} ({top_count})")
    update_readme(total, top_cat, top_count)
