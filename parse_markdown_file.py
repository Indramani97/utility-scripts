import markdown

def parse_markdown(markdown_string):
    # Convert markdown string to HTML
    html_content = markdown.markdown(markdown_string)
    
    # Split HTML content into sections based on any header tags or table tags
    sections = html_content.split('<h')
    tables = html_content.split('<table')
    
    # Initialize multidimensional array to store contents
    contents = []
    
    # Loop through sections
    for section in sections[1:]:  # Skip the first element as it doesn't contain content
        # Extract section title
        title_end_index = section.find('</h')
        header_tag_index = section.find('>')
        header_level = section[header_tag_index + 1:title_end_index]
        section_title = section[title_end_index + 1:].strip()
        
        # Extract section content
        section_content = section[title_end_index + 5:]  # Skip '</h>' tag
        
        # Append title and content to multidimensional array
        contents.append([int(header_level), section_title, section_content])
    
    # Loop through tables
    for table in tables[1:]:  # Skip the first element as it doesn't contain content
        # Extract table content
        rows = table.split('<tr>')
        table_content = []
        for row in rows[1:]:
            cells = row.split('<td>')
            row_content = []
            for cell in cells[1:]:
                cell_content = cell.split('</td>')[0]
                row_content.append(cell_content.strip())
            table_content.append(row_content)
        
        # Append table content to multidimensional array
        contents.append(table_content)
    
    return contents

# Example usage
markdown_string = """
# Section 1
This is the content of section 1.

## Subsection 1.1
This is the content of subsection 1.1.

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

# Section 2
This is the content of section 2.
"""

parsed_contents = parse_markdown(markdown_string)
for item in parsed_contents:
    print(item)

