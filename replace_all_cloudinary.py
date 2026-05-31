import re
import glob

cloudinary_base = "https://res.cloudinary.com/dir57w3tf/image/upload/"

replacements = {
    "assets/vintage_90s_bg.png": f"{cloudinary_base}vintage_90s_bg_qvydjd.png",
    "assets/johnwilliams_biography.png": f"{cloudinary_base}johnwilliams_biography_e0qdxd.png",
    "assets/johnwilliams_biography.jpg": f"{cloudinary_base}johnwilliams_biography_e0qdxd.png",
    "assets/john_williams.png": f"{cloudinary_base}johnwilliams_biography_e0qdxd.png",
    "assets/background.png": f"{cloudinary_base}background_lfgcyo.png",
    "assets/oscar_reward.jpg": f"{cloudinary_base}oscar_reward_jyy7ub.jpg",
    "assets/saturn_reward.png": f"{cloudinary_base}saturn_reward_b61iia.png",
    "assets/afi_reward.png": f"{cloudinary_base}afi_reward_h2sufp.png",
    "assets/bafta_reward.png": f"{cloudinary_base}bafta_reward_du0pbx.png",
    "assets/bmi_reward.png": f"{cloudinary_base}bmi_reward_u7fxyd.png",
    "assets/national_board_reward.png": f"{cloudinary_base}national_board_reward_jyxoyg.png",
    "assets/afi_awards_sketch.png": f"{cloudinary_base}afi_awards_sketch_zrblni.png",
    "assets/bafta_awards_sketch.png": f"{cloudinary_base}bafta_awards_sketch_ucnhze.png",
    "assets/bmi_awards_sketch.png": f"{cloudinary_base}bmi_awards_sketch_thmjdx.png",
    "assets/emmy_awards_sketch.png": f"{cloudinary_base}emmy_awards_sketch_y8qbwp.png",
    "assets/golden_globes_reward.png": f"{cloudinary_base}golden_globes_reward_o5qygv.png",
    "assets/golden_globe_reward.png": f"{cloudinary_base}golden_globe_reward_vad1e8.png",
    "assets/grammy_awards_sketch.png": f"{cloudinary_base}grammy_awards_sketch_qiylry.png",
    "assets/national_board_awards_sketch.png": f"{cloudinary_base}national_board_awards_sketch_q7jepb.png",
    "assets/academy_awards_sketch.png": f"{cloudinary_base}academy_awards_sketch_scpdvx.png",
    "assets/saturn_awards_sketch.png": f"{cloudinary_base}saturn_awards_sketch_jnxodr.png",
}

files = ['index.html', 'awards.html', 'biography.html', 'faq.html', 'work.html']

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated standard assets in {file}")
    except FileNotFoundError:
        print(f"File {file} not found")

# Replace Photo Placeholders in biography.html with Cuplikan_layar images
try:
    with open('biography.html', 'r', encoding='utf-8') as f:
        bio_content = f.read()

    cuplikan = [
        "Cuplikan_layar_2026-05-31_013842_yygoiy",
        "Cuplikan_layar_2026-05-31_013929_ogo72l",
        "Cuplikan_layar_2026-05-31_014006_p1anq1",
        "Cuplikan_layar_2026-05-31_014056_sjuisv",
        "Cuplikan_layar_2026-05-31_014136_avewdu",
        "Cuplikan_layar_2026-05-31_014225_xoilo8",
        "Cuplikan_layar_2026-05-31_014307_mg36bg",
        "Cuplikan_layar_2026-05-31_014336_jixubs",
        "Cuplikan_layar_2026-05-31_014425_alemqb",
        "Cuplikan_layar_2026-05-31_014514_yum2v0",
        "Cuplikan_layar_2026-05-31_014544_mkrr9o",
        "Cuplikan_layar_2026-05-31_014616_fcpmdd",
        "Cuplikan_layar_2026-05-31_014638_cjrvc8",
        "Cuplikan_layar_2026-05-31_014721_xjlekd",
        "Cuplikan_layar_2026-05-31_014807_avrhl4",
        "Cuplikan_layar_2026-05-31_014832_sqonwu",
        "Cuplikan_layar_2026-05-31_014854_kbb18j",
        "Cuplikan_layar_2026-05-31_014934_bi0qvq"
    ]

    import re

    def replacer(match):
        if not hasattr(replacer, 'index'):
            replacer.index = 0
            
        # Determine number of images for this section (mix of 2 and 3 to use all 18 images across 8 placeholders)
        # 8 placeholders. If 6 placeholders get 2 images (12) and 2 placeholders get 3 (6), that's 18!
        num_images = 3 if replacer.index in [3, 6] else 2
        
        html = '<div style="display: flex; flex-direction: column; gap: 20px;">\n'
        for _ in range(num_images):
            if replacer.index < len(cuplikan):
                img_id = cuplikan[replacer.index]
                html += f'    <img src="{cloudinary_base}{img_id}.png" style="width: 100%; height: auto; object-fit: cover; display: block; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" alt="Biography Event">\n'
                replacer.index += 1
        html += '</div>'
        return html

    bio_content = re.sub(r'<div[^>]*>Photo Placeholder</div>', replacer, bio_content, flags=re.IGNORECASE)

    with open('biography.html', 'w', encoding='utf-8') as f:
        f.write(bio_content)
    print("Replaced placeholders in biography.html")

except FileNotFoundError:
    print("biography.html not found")
