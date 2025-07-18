#!/usr/bin/env python3
"""
Find the exact flowappz cookie consent elements
"""

import re

def find_flowappz_elements(file_path):
    """Find flowappz cookie consent elements in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the specific flowappz elements
        patterns = [
            r'id="flowappz-cookie-consent"',
            r'id="flowappz-cookie-consent-approve"',
            r'id="flowappz-cookie-consent-reject"',
            r'flowappz-cookie-consent'
        ]
        
        lines = content.split('\n')
        results = []
        
        for i, line in enumerate(lines):
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Get more context around the match
                    start = max(0, i - 5)
                    end = min(len(lines), i + 6)
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
    files_to_search = [
        '/Users/joeom/Joe Personal project/palindrom-website/index.html',
        '/Users/joeom/Joe Personal project/palindrom-website/public/index.html'
    ]
    
    for file_path in files_to_search:
        print(f"\n{'='*60}")
        print(f"Searching in: {file_path}")
        print(f"{'='*60}")
        
        results = find_flowappz_elements(file_path)
        
        if results:
            for result in results:
                print(f"\nLine {result['line_num']} (matched: {result['pattern']}):")
                print(f"  {result['line']}")
                print("\nContext:")
                for j, context_line in enumerate(result['context']):
                    line_num = result['line_num'] - 5 + j
                    marker = ">>> " if j == 5 else "    "
                    print(f"{marker}{line_num}: {context_line}")
                print("-" * 50)
        else:
            print("No flowappz cookie consent elements found")

if __name__ == "__main__":
    main()