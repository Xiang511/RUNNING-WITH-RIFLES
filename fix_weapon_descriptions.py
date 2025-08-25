#!/usr/bin/env python3
"""
Script to fix truncated weapon descriptions in the markdown file
by extracting complete descriptions from the original HTML file.
"""

import re
import os
from bs4 import BeautifulSoup

def extract_weapon_data_from_html(html_file):
    """Extract weapon data from the original HTML file."""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    weapon_data = {}
    
    # Use regex to find weapon entries in the HTML
    # Look for patterns like: <td>WeaponName</td>\n<td>Description</td>
    weapon_pattern = r'<td>([^<]+)</td>\s*\n\s*<td>([^<]+(?:<br[^>]*>[^<]*)*)</td>'
    matches = re.findall(weapon_pattern, content, re.MULTILINE | re.DOTALL)
    
    for weapon_name, description in matches:
        # Clean up the weapon name and description
        weapon_name = weapon_name.strip()
        description = re.sub(r'<br[^>]*>', ' ', description)  # Replace <br> tags with spaces
        description = re.sub(r'\s+', ' ', description).strip()  # Normalize whitespace
        
        # Skip if this looks like a table header or empty
        if weapon_name and description and not weapon_name.startswith('Image') and not weapon_name.startswith('Name'):
            weapon_data[weapon_name] = description
    
    return weapon_data

def fix_markdown_descriptions(markdown_file, weapon_data):
    """Fix truncated descriptions in the markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    modified = False
    
    for i, line in enumerate(lines):
        # Check if this is a weapon table row with truncated description
        if line.startswith('| ![') and '...' in line:
            # Extract weapon name from the line
            parts = line.split('|')
            if len(parts) >= 4:
                weapon_name = parts[2].strip()
                type_description = parts[3].strip()
                
                # If description is truncated and we have the full description
                if type_description.endswith('...') and weapon_name in weapon_data:
                    full_description = weapon_data[weapon_name]
                    # Replace the truncated description with the full one
                    parts[3] = f" {full_description} "
                    lines[i] = '|'.join(parts)
                    modified = True
                    print(f"Fixed description for: {weapon_name}")
    
    if modified:
        # Write back the fixed content
        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print("All truncated descriptions have been fixed!")
    else:
        print("No truncated descriptions found to fix.")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(script_dir, 'website', 'docs', 'resources', 'test.md')
    markdown_file = os.path.join(script_dir, 'website', 'docs', 'resources', 'Weapons and equipment.md')
    
    print("Extracting weapon data from HTML file...")
    weapon_data = extract_weapon_data_from_html(html_file)
    print(f"Extracted data for {len(weapon_data)} weapons")
    
    print("Fixing markdown descriptions...")
    fix_markdown_descriptions(markdown_file, weapon_data)

if __name__ == "__main__":
    main()
