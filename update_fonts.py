import glob

html_files = glob.glob("*.html")

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update logo-text font size from 3.5rem to 4.5rem
    content = content.replace("font-size: 3.5rem;", "font-size: 4.5rem;")
    
    # 2. Update work-title font size and weights
    # In work.html, the CSS for .work-title is usually:
    # .work-title {
    #     font-family: 'Clearface', serif;
    #     font-size: 3.5rem;
    #     font-weight: 700;
    
    # Let's replace the specific block if it exists
    if '.work-title {' in content:
        # We know from the view_file that the exact block is:
        # .work-title {
        #     font-family: 'Clearface', serif;
        #     font-size: 3.5rem;
        #     font-weight: 700;
        
        # Replace font-size to 2.8rem and font-weight to 400
        content = content.replace("font-size: 3.5rem;\n            font-weight: 700;", "font-size: 2.8rem;\n            font-weight: 400;")
        
        # We also need to update .work-title.active
        # .work-title.active {
        #     opacity: 1;
        #     transform: scale(1.05);
        #     font-weight: 800;
        content = content.replace("transform: scale(1.05);\n            font-weight: 800;", "transform: scale(1.05);\n            font-weight: 700;")
        content = content.replace("transform: scale(1.05);\n            font-weight: 700;", "transform: scale(1.05);\n            font-weight: 700;") # Just in case it was 700

    # 3. Update inline .work-page-title in work.html
    if 'font-size: 5rem;' in content and 'work-page-title' in content:
        content = content.replace("font-size: 5rem;", "font-size: 3.5rem;")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fonts updated across HTML files.")
