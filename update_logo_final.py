import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update .logo-text font-size: 4.5rem; to 3.8rem;
    # Update translateY(-5px) to translateY(-15px)
    
    # Let's do string replacement for safety if we know the exact strings, 
    # but the string format might slightly vary (spaces).
    # Since I just updated them recently, they probably look like this:
    # .logo-text {
    #     font-family: "Disney Script", cursive;
    #     font-size: 4.5rem;
    #     ...
    #     transform: translateY(-5px) rotate(-2deg);
    
    # 1. Update font size
    content = re.sub(r'(\.logo-text\s*\{[^}]*?font-size:\s*)4\.5rem;', r'\g<1>3.8rem;', content, flags=re.DOTALL)
    
    # 2. Update translateY
    content = re.sub(r'(\.logo-text\s*\{[^}]*?transform:\s*translateY\()-5px(\)\s*rotate\(-2deg\);)', r'\g<1>-15px\g<2>', content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated .logo-text in {file}")

print("All files processed.")
