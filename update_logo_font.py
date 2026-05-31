import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update .logo-text font-size: Xrem; to font-size: 4.5rem;
    # Using regex to find .logo-text { ... font-size: Xrem; ... } is a bit tricky,
    # let's just find the block.
    # It usually looks like:
    # .logo-text {
    #     font-family: 'Disney Script', cursive;
    #     font-size: 3.5rem;
    
    # regex approach to find font-size inside .logo-text
    # We can match `.logo-text { [anything not }] font-size: <value>;`
    
    pattern = r'(\.logo-text\s*\{[^}]*?font-size:\s*)[0-9.]+rem;'
    new_content = re.sub(pattern, r'\g<1>4.5rem;', content, flags=re.DOTALL)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated .logo-text in {file}")
