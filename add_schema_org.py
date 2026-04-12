#!/usr/bin/env python3
"""
Add Schema.org structured data to city pages without it.
Reads the title and extracts FAQ data from each page.
"""

import os
import re
import json
import sys
from pathlib import Path
from html.parser import HTMLParser

# Base directory
BASE_DIR = Path(__file__).parent / "bestatter"

# Cities that already have Schema.org
EXISTING_CITIES = {"muenchen", "hamburg", "berlin", "koeln", "frankfurt"}

class TitleExtractor(HTMLParser):
    """Extract title and Bundesland from page"""
    def __init__(self):
        super().__init__()
        self.title = None
        self.in_title = False
        self.bundesland = None

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title and self.title is None:
            self.title = data.strip()

class FAQExtractor(HTMLParser):
    """Extract FAQ from <details><summary> pattern"""
    def __init__(self):
        super().__init__()
        self.faqs = []
        self.in_summary = False
        self.in_answer = False
        self.current_question = None
        self.current_answer = None
        self.answer_buffer = []

    def handle_starttag(self, tag, attrs):
        if tag == "summary":
            self.in_summary = True
            self.current_question = None
        elif tag == "div":
            attrs_dict = dict(attrs)
            if attrs_dict.get("class") == "faq-answer":
                self.in_answer = True
                self.answer_buffer = []

    def handle_endtag(self, tag):
        if tag == "summary":
            self.in_summary = False
        elif tag == "div":
            if self.in_answer:
                self.in_answer = False
                if self.current_question and self.answer_buffer:
                    answer_text = " ".join(self.answer_buffer).strip()
                    self.faqs.append({
                        "question": self.current_question.strip(),
                        "answer": answer_text
                    })

    def handle_data(self, data):
        if self.in_summary:
            if self.current_question is None:
                self.current_question = data
            else:
                self.current_question += data
        elif self.in_answer:
            text = data.strip()
            if text:
                self.answer_buffer.append(text)

def extract_title_and_bundesland(html_content):
    """Extract city name from title"""
    extractor = TitleExtractor()
    extractor.feed(html_content)

    if not extractor.title:
        return None, None

    # Extract city name from "Bestatter in {City} —"
    match = re.search(r'Bestatter in\s+([^—]*?)\s*—', extractor.title)
    if not match:
        match = re.search(r'Bestatter in\s+([^|]*)', extractor.title)

    city = match.group(1).strip() if match else None

    # Try to extract Bundesland from content
    bundesland_match = re.search(r'(Bayern|Baden-Württemberg|Hessen|Nordrhein-Westfalen|Schleswig-Holstein|Mecklenburg-Vorpommern|Brandenburg|Berlin|Bremen|Hamburg|Sachsen|Sachsen-Anhalt|Thüringen|Niedersachsen|Rheinland-Pfalz|Saarland)', html_content)
    bundesland = bundesland_match.group(1) if bundesland_match else None

    return city, bundesland

def extract_faqs(html_content):
    """Extract FAQs from page"""
    extractor = FAQExtractor()
    try:
        extractor.feed(html_content)
    except:
        return []

    return extractor.faqs

def generate_schema_org(city, bundesland, slug, faqs):
    """Generate Schema.org JSON-LD"""

    # Build FAQ items
    faq_items = []
    for faq in faqs[:5]:  # Limit to 5 FAQs
        faq_items.append({
            "@type": "Question",
            "name": faq["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["answer"]
            }
        })

    # Build the schema
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": f"Bestatter in {city} finden",
                "description": f"Vergleichen und finden Sie lokale Bestatter in {city}. Informationen zu Friedhöfen, Gebühren und Bestattungsrecht {bundesland}.",
                "areaServed": {
                    "@type": "City",
                    "name": city,
                    "addressRegion": bundesland
                } if bundesland else {
                    "@type": "City",
                    "name": city
                },
                "serviceType": "Funeral Services"
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Start",
                        "item": "https://machsruhig.de/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Bestatter finden",
                        "item": "https://machsruhig.de/bestatter"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": city,
                        "item": f"https://machsruhig.de/bestatter/{slug}"
                    }
                ]
            }
        ]
    }

    # Add FAQ if present
    if faq_items:
        schema["@graph"].append({
            "@type": "FAQPage",
            "mainEntity": faq_items
        })

    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

def get_insertion_point(html_content):
    """Find where to insert the Schema.org tag (before closing </head>)"""
    # Look for </style> tag first if it exists
    style_match = re.search(r'</style>\s*</head>', html_content, re.IGNORECASE)
    if style_match:
        return style_match.end() - len("</head>")

    # Otherwise look for </head>
    head_match = re.search(r'</head>', html_content, re.IGNORECASE)
    if head_match:
        return head_match.start()

    return None

def add_schema_org_to_file(file_path, city, bundesland, slug):
    """Add Schema.org to a single file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Check if already has Schema.org
    if 'application/ld+json' in html_content:
        return False, "Already has Schema.org"

    # Extract FAQs
    faqs = extract_faqs(html_content)

    # Generate Schema.org
    schema_json = generate_schema_org(city, bundesland, slug, faqs)
    schema_tag = f'\n<script type="application/ld+json">\n{schema_json}\n</script>\n'

    # Find insertion point
    insertion_point = get_insertion_point(html_content)
    if insertion_point is None:
        return False, "Could not find </head> tag"

    # Insert schema tag
    new_html = html_content[:insertion_point] + schema_tag + html_content[insertion_point:]

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    return True, f"Added Schema.org ({len(faqs)} FAQs)"

def main():
    """Process all city directories"""

    if not BASE_DIR.exists():
        print(f"Error: Base directory {BASE_DIR} does not exist")
        sys.exit(1)

    updated_files = []
    skipped_files = []

    # Get all city directories
    city_dirs = sorted([d for d in BASE_DIR.iterdir() if d.is_dir()])

    for city_dir in city_dirs:
        city_slug = city_dir.name

        # Skip existing cities
        if city_slug in EXISTING_CITIES:
            continue

        index_file = city_dir / "index.html"
        if not index_file.exists():
            skipped_files.append((city_slug, "No index.html found"))
            continue

        # Read file
        with open(index_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extract title and Bundesland
        city_name, bundesland = extract_title_and_bundesland(html_content)

        if not city_name:
            skipped_files.append((city_slug, "Could not extract city name"))
            continue

        # Add Schema.org
        success, message = add_schema_org_to_file(index_file, city_name, bundesland, city_slug)

        if success:
            updated_files.append((city_slug, city_name, message))
        else:
            skipped_files.append((city_slug, message))

    # Print results
    print("\n" + "="*60)
    print("Schema.org Update Summary")
    print("="*60 + "\n")

    print(f"UPDATED ({len(updated_files)} files):")
    for slug, city, message in updated_files:
        print(f"  ✓ {slug:20} ({city:20}) - {message}")

    if skipped_files:
        print(f"\nSKIPPED ({len(skipped_files)} files):")
        for slug, reason in skipped_files:
            print(f"  - {slug:20} - {reason}")

    print("\n" + "="*60)
    print(f"Total processed: {len(updated_files) + len(skipped_files)}")
    print(f"Updated: {len(updated_files)}, Skipped: {len(skipped_files)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
