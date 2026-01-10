import os
import json

def generate_emby_icons_json(emby_dir, output_file):
    """
    扫描 Emby 目录下所有 PNG 图标，生成 EmbyIcons.json
    """

    base_url = "https://raw.githubusercontent.com/buhuizhuce/Logo/refs/heads/main/Emby"

    icons = []

    for filename in sorted(os.listdir(emby_dir)):
        if filename.lower().endswith(".png"):
            name = filename[:-4]  # 去掉 .png
            url = f"{base_url}/{filename}"

            icons.append({
                "name": name,
                "url": url
            })

    data = {
        "name": "🎞️ Emby",
        "description": "自用Emby服务icons，by 🏄🏻‍♂️ Frank",
        "icons": icons
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已生成 {output_file}")


if __name__ == "__main__":
    generate_emby_icons_json("Emby", "EmbyIcons.json")
