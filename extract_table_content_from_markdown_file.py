import re

def extract_tables_from_markdown(markdown_string):
    # Define regular expression pattern for table
    table_pattern = r'\|(.+?)\|\n\|(.+?)\|(?=\n|$)'
    
    # Find all matches of table pattern in the markdown string
    table_matches = re.findall(table_pattern, markdown_string, re.DOTALL)
    
    # Initialize list to store extracted tables
    tables = []
    
    # Process each table match
    for match in table_matches:
        # Split each row of the table
        rows = match[1].split('\n|')
        
        # Remove leading and trailing whitespaces from each row
        cleaned_rows = [row.strip() for row in rows]
        
        # Split each row into cells
        table_data = [row.split('|') for row in cleaned_rows]
        
        # Remove leading and trailing whitespaces from each cell
        cleaned_table_data = [[cell.strip() for cell in row] for row in table_data]
        
        # Append cleaned table data to tables list
        tables.append(cleaned_table_data)
    
    return tables

# Example usage
markdown_string = """
This is some text.

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

This is some more text.

| Fruit    | Quantity |
|----------|----------|
| Apple    | 3        |
| Banana   | 6        |
"""

tables = extract_tables_from_markdown(markdown_string)
for table in tables:
    for row in table:
        print(row)
    print()

