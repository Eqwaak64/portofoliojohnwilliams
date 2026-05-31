import re

def update_award_assets():
    with open('awards.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Hero Images
    content = content.replace('assets/emmy_ph.jpg', 'assets/emmy.jpg')
    content = content.replace('assets/globe_ph.jpg', 'assets/golden_globe.jpg')
    content = content.replace('assets/grammy_ph.jpg', 'assets/grammy.jpg')
    content = content.replace('assets/oscar_ph.jpg', 'assets/oscar.jpg')
    content = content.replace('assets/tony_ph.jpg', 'assets/tony.jpg')

    # Update Icon Images
    content = content.replace('assets/icon_emmy.svg', 'assets/05a19f03-42e4-42f1-806a-3b8920b04dec.png')
    content = content.replace('assets/icon_globe.svg', 'assets/9656ba6d-7fb9-43de-b527-b1b5be9d32c4.png')
    content = content.replace('assets/icon_grammy.svg', 'assets/c2a9cffc-eed2-493c-95d7-14fcf6473282.png')
    content = content.replace('assets/icon_oscar.svg', 'assets/7d35e49b-59fa-42ba-a05c-059dff755c04.png')
    content = content.replace('assets/icon_tony.svg', 'assets/5e05936d-c82b-4808-88ca-61ae7a20d0e5.png')

    with open('awards.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_award_assets()
