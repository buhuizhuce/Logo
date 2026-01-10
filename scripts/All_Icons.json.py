import os
import json

def generate_all_icons_json(root_dir, output_file):
    """
    扫描 Logo 仓库所有一级目录下的 PNG 图标，生成 All_Icons.json
    """
    base_url = "https://raw.githubusercontent.com/buhuizhuce/Logo/refs/heads/main"
    icons = []

    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for filename in sorted(os.listdir(folder_path)):
            if filename.lower().endswith(".png"):
                name = filename[:-4]  # 去掉 .png
                url = f"{base_url}/{folder}/{filename}"
                icons.append({
                    "name": name,
                    "url": url
                })

    data = {
        "name": "🧩 All Icons",
        "description": "Logo 仓库内所有图标合集，by 🏄🏻‍♂️ Frank",
        "icons": icons
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已生成 {output_file}")


if __name__ == "__main__":
    generate_all_icons_json(".", "All_Icons.json")
