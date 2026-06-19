import json
import sys

SITE_DATA = {
    "name": "C7 Entertainment Official",
    "url": "https://portal-c7entertainments.com",
    "keywords": ["c7娱乐", "entertainment portal", "gaming platform"],
    "tags": ["portal", "entertainment", "c7"],
    "description": "C7 Entertainment provides a comprehensive online entertainment platform with diverse gaming and interactive services.",
    "language": "en",
    "region": "global"
}

def load_summary_config():
    return {
        "title": "Site Summary Report",
        "separator": "=",
        "line_width": 60
    }

def format_keywords(keywords):
    return ", ".join(keywords)

def format_tags(tags):
    return ", ".join(tags)

def build_summary_block(data):
    block_lines = []
    block_lines.append(f"Site Name: {data['name']}")
    block_lines.append(f"URL: {data['url']}")
    block_lines.append(f"Keywords: {format_keywords(data['keywords'])}")
    block_lines.append(f"Tags: {format_tags(data['tags'])}")
    block_lines.append(f"Description: {data['description']}")
    block_lines.append(f"Language: {data['language']}")
    block_lines.append(f"Region: {data['region']}")
    return block_lines

def print_separator(config):
    sep_char = config["separator"]
    width = config["line_width"]
    print(sep_char * width)

def print_header(config):
    print_separator(config)
    title = config["title"]
    width = config["line_width"]
    print(f"{title:^{width}}")
    print_separator(config)

def print_summary(data, config):
    print_header(config)
    block = build_summary_block(data)
    for line in block:
        print(f"  {line}")
    print_separator(config)

def generate_json_output(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

def display_json(data):
    json_str = generate_json_output(data)
    print("\nStructured JSON equivalent:\n")
    print(json_str)

def main():
    config = load_summary_config()
    data = SITE_DATA
    print_summary(data, config)
    if "--json" in sys.argv:
        display_json(data)

if __name__ == "__main__":
    main()