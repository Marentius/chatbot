"""Scrape marentius.no portfolio site and save pages as .md files.

Usage:
    python -m scripts.scrape_website [--output-dir docs/site]
"""
import argparse
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

PAGES = [
    ("https://marentius.no", "index"),
    ("https://marentius.no/projects/europris-bachelor", "europris-bachelor"),
    ("https://marentius.no/projects/visma-branding", "visma-branding"),
    ("https://marentius.no/projects/chatbot", "chatbot"),
    ("https://marentius.no/projects/regtime", "regtime"),
    ("https://marentius.no/projects/fileconverter", "fileconverter"),
    ("https://marentius.no/projects/almesus", "almesus"),
]


def get_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_content(soup: BeautifulSoup) -> tuple[str, str]:
    """Extract title and main content as markdown-like text."""
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Untitled"

    # Try to find the main content area
    content_area = (
        soup.find("main")
        or soup.find("article")
        or soup.find("body")
    )

    # Remove nav, header, footer, scripts, styles
    for tag in content_area.find_all(
        ["nav", "header", "footer", "script", "style", "form", "iframe"]
    ):
        tag.decompose()

    # Convert to markdown-like text
    lines = []
    for element in content_area.descendants:
        if element.name in ("h1", "h2", "h3", "h4"):
            level = int(element.name[1])
            text = element.get_text(" ", strip=True)
            if text:
                lines.append(f"\n{'#' * level} {text}\n")
        elif element.name == "li":
            text = element.get_text(" ", strip=True)
            if text:
                lines.append(f"- {text}")
        elif element.name == "p":
            text = element.get_text(" ", strip=True)
            if text:
                lines.append(f"\n{text}\n")

    content = "\n".join(lines)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return title, content.strip()


def scrape_and_save(output_dir: str):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved = 0
    for url, slug in PAGES:
        filepath = output_path / f"{slug}.md"
        print(f"  Scraping {url}...", end=" ")
        try:
            soup = get_soup(url)
            title, content = extract_content(soup)

            if len(content) < 50:
                print("SKIPPED (too short)")
                continue

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(f"Kilde: {url}\n\n")
                f.write(content)

            saved += 1
            print(f"OK ({len(content)} chars)")
            time.sleep(0.5)

        except Exception as e:
            print(f"ERROR: {e}")

    print(f"\nDone! Saved {saved} pages to {output_path}/")


def main():
    parser = argparse.ArgumentParser(description="Scrape marentius.no portfolio site")
    parser.add_argument("--output-dir", default="../docs/site")
    args = parser.parse_args()
    scrape_and_save(args.output_dir)


if __name__ == "__main__":
    main()
