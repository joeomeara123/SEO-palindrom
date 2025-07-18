#!/usr/bin/env python3
"""
Search for cookie consent configuration in HTML files
"""

import re
import os

def search_cookie_content(file_path):
    """Search for cookie-related content in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Search for cookie-related patterns
        patterns = [
            r'cookie-consent',
            r'cookieConsent',
            r'CookieConsent',
            r'Allow.*cookie',
            r'Decline.*cookie',
            r'Accept.*cookie',
            r'Reject.*cookie',
            r'privacy.*policy',
            r'analytics',
            r'tracking',
            r'flowappz',
            r'cookie.*banner',
            r'cookie.*popup'
        ]
        
        lines = content.split('\n')
        results = []
        
        for i, line in enumerate(lines):
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Get context around the match
                    start = max(0, i - 3)
                    end = min(len(lines), i + 4)
                    context = lines[start:end]
                    
                    results.append({
                        'line_num': i + 1,
                        'pattern': pattern,
                        'line': line.strip(),
                        'context': context
                    })
                    break
        
        return results
        
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def main():
    # Search both index.html files
    files_to_search = [
        '/Users/joeom/Joe Personal project/palindrom-website/index.html',
        '/Users/joeom/Joe Personal project/palindrom-website/public/index.html'
    ]
    
    for file_path in files_to_search:
        if os.path.exists(file_path):
            print(f"\n{'='*50}")
            print(f"Searching in: {file_path}")
            print(f"{'='*50}")
            
            results = search_cookie_content(file_path)
            
            if results:
                for result in results:
                    print(f"\nLine {result['line_num']} (matched: {result['pattern']}):")
                    print(f"  {result['line']}")
                    print("\nContext:")
                    for j, context_line in enumerate(result['context']):
                        line_num = result['line_num'] - 3 + j
                        marker = ">>> " if j == 3 else "    "
                        print(f"{marker}{line_num}: {context_line}")
                    print("-" * 40)
            else:
                print("No cookie-related content found")

if __name__ == "__main__":
    main()