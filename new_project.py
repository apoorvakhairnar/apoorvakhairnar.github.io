#!/usr/bin/env python3
"""
new_project.py

Automates creation of a Jekyll project page in the _projects collection,
with date-based front-matter and image metadata. Automatically commits & pushes.
"""
import argparse
import datetime
import os
import subprocess

# Paths
COLLECTION_DIR = os.path.join(os.getcwd(), '_projects')
ASSETS_DIR     = os.path.join(os.getcwd(), 'assets', 'projects')  # store images here

FRONT_MATTER = '''---
layout: default
title: "{title}"
date: {date}
image: "{image_path}"
permalink: /pages/projects/{slug}/
extra_css:
  - project_style.css
---
'''

CONTENT_TEMPLATE = '''{description}'''

COMMIT_MSG = 'Add project: {title}'


def slugify(text):
    # simple slug: lowercase, spaces to hyphens, strip non-alphanum
    import re
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", '-', slug).strip('-')
    return slug


def main():
    parser = argparse.ArgumentParser(
        description="Create a new Jekyll project in the _projects collection"
    )
    parser.add_argument('--title', required=True, help='Project title')
    parser.add_argument('--date', help='Project date YYYY-MM-DD', default=None)
    parser.add_argument('--image', required=True,
                        help='Image filename (must exist in assets/projects/)')
    parser.add_argument('--desc', required=True,
                        help='Path to Markdown file with project description')
    parser.add_argument('--slug', help='URL slug (auto-generated from title)')
    args = parser.parse_args()

    title = args.title.strip()
    date_str = args.date or datetime.date.today().isoformat()
    slug = args.slug.strip() if args.slug else slugify(title)
    image_name = os.path.basename(args.image)
    image_path = f"/assets/projects/{image_name}"
    desc_path = args.desc

    # Validate description
    if not os.path.isfile(desc_path):
        print(f"Error: Description file '{desc_path}' not found.")
        return
    with open(desc_path, 'r', encoding='utf-8') as f:
        description = f.read().rstrip() + '\n'

    # Ensure collection dir exists
    os.makedirs(COLLECTION_DIR, exist_ok=True)
    page_file = os.path.join(COLLECTION_DIR, f"{slug}.md")
    if os.path.exists(page_file):
        print(f"Error: '{page_file}' already exists. Aborting.")
        return

    # Build front matter and content
    fm = FRONT_MATTER.format(
        title=title.replace('"', '\"'),
        date=date_str,
        image_path=image_path,
        slug=slug
    )
    content = CONTENT_TEMPLATE.format(description=description)
    full = fm + '\n' + content

    # Write file
    with open(page_file, 'w', encoding='utf-8') as f:
        f.write(full)
    print(f"Created project page at: {page_file}")

    # Git operations
    try:
        subprocess.run(['git', 'add', page_file], check=True)
        subprocess.run(['git', 'commit', '-m', COMMIT_MSG.format(title=title)], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Committed and pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("Git error:", e)

if __name__ == '__main__':
    main()
