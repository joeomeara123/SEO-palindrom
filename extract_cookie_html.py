#!/usr/bin/env python3
"""
Extract the exact cookie consent HTML structure and JavaScript references
"""

import re

def extract_cookie_consent(file_path):
    """Extract cookie consent HTML and JavaScript references"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into lines for easier processing
        lines = content.splitlines()
        
        # Find CDN script reference
        cdn_script = None
        for i, line in enumerate(lines):
            if 'flowappz' in line.lower() and 'cookie-consent' in line.lower() and 'script' in line.lower():
                cdn_script = {'line_num': i + 1, 'content': line.strip()}
                break
        
        # Find cookie consent HTML structure
        cookie_html = []
        in_cookie_section = False
        cookie_start = None
        
        for i, line in enumerate(lines):
            if 'flowappz-cookie-consent' in line.lower():
                if not in_cookie_section:
                    in_cookie_section = True
                    cookie_start = i
                    # Get some context before
                    start_context = max(0, i - 10)
                    for j in range(start_context, i):
                        cookie_html.append({'line_num': j + 1, 'content': lines[j]})
                
                cookie_html.append({'line_num': i + 1, 'content': line})
                
                # Continue collecting until we find the closing elements
                if 'reject' in line.lower() or 'approve' in line.lower():
                    # Get a few more lines for context
                    for j in range(i + 1, min(len(lines), i + 15)):
                        cookie_html.append({'line_num': j + 1, 'content': lines[j]})
                        # Stop if we find a closing div that seems to end the cookie section
                        if '</div>' in lines[j] and len(lines[j].strip()) < 10:
                            break
                    break
        
        return cdn_script, cookie_html
        
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, []

def main():
    file_path = '/Users/joeom/Joe Personal project/palindrom-website/public/index.html'
    
    print(f"Extracting cookie consent from: {file_path}")
    print("=" * 80)
    
    cdn_script, cookie_html = extract_cookie_consent(file_path)
    
    if cdn_script:
        print("\nCDN SCRIPT REFERENCE:")
        print("=" * 40)
        print(f"Line {cdn_script['line_num']}: {cdn_script['content']}")
        print()
    
    if cookie_html:
        print("\nCOOKIE CONSENT HTML STRUCTURE:")
        print("=" * 40)
        for item in cookie_html:
            marker = ">>> " if 'flowappz' in item['content'].lower() else "    "
            print(f"{marker}{item['line_num']}: {item['content']}")
        print()
    
    if not cdn_script and not cookie_html:
        print("No cookie consent elements found")

if __name__ == "__main__":
    main()