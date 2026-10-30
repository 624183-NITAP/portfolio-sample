import os
import re

def check_html(filename):
    print(f"Checking {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check asset paths
    srcs = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', content)
    missing = []
    for s in srcs:
        if s.startswith('public/') or s.startswith('assets/'):
            clean_path = s.split('?')[0].split('#')[0]
            if not os.path.exists(clean_path):
                missing.append(s)
    if missing:
        print(f"Missing files in {filename}:", missing)
    else:
        print(f"All local asset paths exist in {filename}!")
        
    # Check internal anchors
    ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
    anchors = re.findall(r'href=["\']#([^"\']+)["\']', content)
    broken_anchors = [a for a in anchors if a not in ids]
    if broken_anchors:
        print(f"Unresolved anchor links in {filename}:", set(broken_anchors))
    else:
        print(f"All internal anchor links match valid IDs in {filename}!")

check_html('index.html')
check_html('ece.html')
check_html('quantum.html')

