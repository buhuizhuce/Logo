import os
import json

IGNORE_DIRS = {".github", "scripts"}  # 不生成 JSON 的目录
BASE_URL = "https://raw.githubusercontent.com/buhuizhuce/Logo/refs/heads/main"


def generate_icons_for_folder(folder):
    """为单个目录生成 JSON 数据"""
    folder_path = folder
    icons = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith(".png"):
            name = filename[:-4]
            url = f"{BASE_URL}/{folder}/{filename}"
            icons.append({"name": name, "url": url})

    return icons


def main():
    all_icons = []

    for folder in sorted(os.listdir(".")):
        if not os.path.isdir(folder):
            continue
        if folder in IGNORE_DIRS:
            continue

        icons = generate_icons_for_folder(folder)
        if not icons:
            continue

        # 生成单独 JSON 文件
        output_file = f"{folder}_Icons.json"
        data = {
            "name": f"{folder} Icons",
            "description": f"{folder} 图标索引，自动生成 by 🏄🏻‍♂️ Frank",
            "icons": icons
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"已生成 {output_file}")

        # 汇总到 All_Icons.json
        all_icons.extend(icons)

    # 生成 All_Icons.json
    all_data = {
        "name": "🧩 All Icons",
        "description": "Logo 仓库内所有图标合集，自动生成 by 🏄🏻‍♂️ Frank",
        "icons": all_icons
    }

    with open("All_Icons.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("已生成 All_Icons.json")


if __name__ == "__main__":
    main()
