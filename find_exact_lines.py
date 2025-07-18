#!/usr/bin/env python3
"""
Find exact lines containing flowappz cookie consent elements
"""

def find_exact_lines(file_path):
    """Find exact lines containing flowappz elements"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"Total lines in file: {len(lines)}")
        
        # Search for flowappz-cookie-consent
        for i, line in enumerate(lines):
            if 'flowappz-cookie-consent' in line:
                print(f"\nFound at line {i+1}:")
                print(f"  {line.strip()}")
                
                # Show context
                start = max(0, i - 3)
                end = min(len(lines), i + 4)
                print("\nContext:")
                for j in range(start, end):
                    marker = ">>> " if j == i else "    "
                    print(f"{marker}{j+1}: {lines[j].rstrip()}")
                print("-" * 50)
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    files = [
        '/Users/joeom/Joe Personal project/palindrom-website/index.html',
        '/Users/joeom/Joe Personal project/palindrom-website/public/index.html'
    ]
    
    for file_path in files:
        print(f"\n{'='*60}")
        print(f"File: {file_path}")
        print(f"{'='*60}")
        find_exact_lines(file_path)

if __name__ == "__main__":
    main()