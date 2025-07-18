#!/usr/bin/env python3
"""
Script to find cookie banner code in HTML file
"""

import re

def find_cookie_banner(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Search patterns for cookie banner
    patterns = [
        r'cookie',
        r'consent',
        r'privacy',
        r'analytics',
        r'tracking',
        r'Allow',
        r'Decline',
        r'Accept',
        r'Reject'
    ]
    
    lines = content.split('\n')
    found_lines = []
    
    for i, line in enumerate(lines):
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                found_lines.append((i+1, line.strip(), pattern))
                break
    
    return found_lines

if __name__ == "__main__":
    results = find_cookie_banner('index.html')
    print(f"Found {len(results)} lines with cookie-related content:")
    print("="*50)
    
    for line_num, line_content, pattern in results:
        print(f"Line {line_num} (matched: {pattern}):")
        print(f"  {line_content}")
        print()