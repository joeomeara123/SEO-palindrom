#!/usr/bin/env python3
"""
Extract cookie consent HTML structure and JavaScript
"""
import re

def extract_cookie_consent(file_path):
    """Extract cookie consent related code from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find flowappz cookie consent elements
        lines = content.split('\n')
        
        # Look for flowappz-cookie-consent elements
        consent_lines = []
        for i, line in enumerate(lines):
            if 'flowappz-cookie-consent' in line.lower():
                # Get extended context for the cookie consent banner
                start = max(0, i - 20)
                end = min(len(lines), i + 20)
                consent_lines.append({
                    'line_num': i + 1,
                    'context': lines[start:end]
                })
        
        # Look for JavaScript related to cookie consent
        js_sections = []
        in_script = False
        script_start = 0
        
        for i, line in enumerate(lines):
            if '<script' in line.lower():
                in_script = True
                script_start = i
            elif '</script>' in line.lower() and in_script:
                script_content = '\n'.join(lines[script_start:i+1])
                if any(keyword in script_content.lower() for keyword in ['cookie', 'consent', 'flowappz', 'approve', 'reject']):
                    js_sections.append({
                        'start_line': script_start + 1,
                        'end_line': i + 1,
                        'content': script_content
                    })
                in_script = False
        
        return consent_lines, js_sections
        
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return [], []

def main():
    file_path = '/Users/joeom/Joe Personal project/palindrom-website/index.html'
    
    print(f"Extracting cookie consent from: {file_path}")
    print("=" * 60)
    
    consent_lines, js_sections = extract_cookie_consent(file_path)
    
    if consent_lines:
        print("\nCOOKIE CONSENT HTML STRUCTURE:")
        print("=" * 40)
        for section in consent_lines:
            print(f"\nFound around line {section['line_num']}:")
            for j, line in enumerate(section['context']):
                line_num = section['line_num'] - 20 + j
                if 'flowappz-cookie-consent' in line.lower():
                    print(f">>> {line_num}: {line}")
                else:
                    print(f"    {line_num}: {line}")
            print("-" * 40)
    
    if js_sections:
        print("\nJAVASCRIPT SECTIONS WITH COOKIE CONSENT:")
        print("=" * 40)
        for section in js_sections:
            print(f"\nScript section (lines {section['start_line']}-{section['end_line']}):")
            print(section['content'])
            print("-" * 40)
    
    if not consent_lines and not js_sections:
        print("No cookie consent related code found")

if __name__ == "__main__":
    main()