import json
import re
from datetime import datetime
import os

def generate_readme(data_path, readme_path):
    # Load and sort data
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data.sort(key=lambda x: datetime.strptime(x['update_date'], '%Y-%m-%d'), reverse=True)

    # --- Generate new content ---

    # 1. Generate new "Last updated" section
    last_updated_content = f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*"

    # 2. Generate new table
    table_content = "| Company      | Model Version                      | Update Date | Improvements & Features                                      |\n"
    table_content += "| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |\n"
    for item in data:
        display_date = datetime.strptime(item['update_date'], '%Y-%m-%d').strftime('%Y-%m-%d')
        
        # Check if there's a blog_url and add badge under company name
        company_name = item['company']
        if 'blog_url' in item and item['blog_url']:
            # Create a blog badge that links to the technical blog
            badge_url = f"https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger"
            company_name = f"{item['company']}<br/>[![Blog]({badge_url})]({item['blog_url']})"
        
        table_content += f"| {company_name} | {item['model_name']} | {display_date} | {item.get('features', '')} |\n"

    # --- Update README.md ---

    # Read existing README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_contents = f.read()

    # Use regex to replace the "Last updated" section
    readme_contents = re.sub(
        r'(?<=<!-- LAST_UPDATED_START -->\n)(.*?)(?=\n<!-- LAST_UPDATED_END -->)',
        last_updated_content,
        readme_contents,
        flags=re.DOTALL
    )

    # Use regex to replace the table section
    readme_contents = re.sub(
        r'(?<=<!-- TABLE_START -->\n)(.*?)(?=\n<!-- TABLE_END -->)',
        table_content,
        readme_contents,
        flags=re.DOTALL
    )

    # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_contents)

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, 'data.json')
    readme_file = os.path.join(script_dir, '..', 'README.md')
    generate_readme(data_file, readme_file)
    print("README.md has been updated successfully.")