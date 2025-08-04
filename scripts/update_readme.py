import json
from datetime import datetime

def generate_readme(data_path, readme_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Sort data by update_date in descending order
    data.sort(key=lambda x: datetime.strptime(x['update_date'], '%Y-%m-%d'), reverse=True)

    # Start generating markdown content
    markdown = "# LLM Model Updates Tracker\n\n"
    markdown += "A tracker for the latest updates on Large Language Models from various companies.\n\n"
    markdown += "*Last updated: {}*\n\n".format(datetime.now().strftime('%Y-%m-%d'))

    # Create table header
    markdown += "| Company      | Model Version                      | Update Date | Improvements & Features                                      |\n"
    markdown += "| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |\n"

    # Populate table rows
    for item in data:
        # Format date back to Month-Day for display if desired, e.g., 07-23
        display_date = datetime.strptime(item['update_date'], '%Y-%m-%d').strftime('%m月%d日')
        markdown += f"| {item['company']} | {item['model_name']} | {display_date} | {item.get('features', '')} |\n"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

if __name__ == '__main__':
    # Assuming the script is in the 'scripts' directory
    # and data.json is in the same directory.
    # The README.md is in the parent directory.
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, 'data.json')
    readme_file = os.path.join(script_dir, '..', 'README.md')
    generate_readme(data_file, readme_file)
    print("README.md has been updated successfully.")