#!/usr/bin/env python3
import re

# Read the file
with open('/Users/joeom/Joe Personal project/palindrom-website/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the CDN script
cdn_match = re.search(r'<script.*?flowappz.*?cookie-consent.*?</script>', content, re.DOTALL | re.IGNORECASE)
if cdn_match:
    print("CDN SCRIPT FOUND:")
    print("=" * 40)
    print(cdn_match.group())
    print()

# Find the cookie consent HTML elements
cookie_matches = re.findall(r'[^>]*flowappz-cookie-consent[^<]*', content, re.IGNORECASE)
if cookie_matches:
    print("COOKIE CONSENT ELEMENTS:")
    print("=" * 40)
    for match in cookie_matches:
        print(match)
    print()

# Search for the complete cookie consent structure
cookie_section = re.search(r'<div[^>]*flowappz-cookie-consent[^>]*>.*?</div>', content, re.DOTALL | re.IGNORECASE)
if cookie_section:
    print("COMPLETE COOKIE CONSENT STRUCTURE:")
    print("=" * 40)
    print(cookie_section.group())