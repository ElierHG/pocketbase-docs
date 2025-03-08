#!/usr/bin/env python3
import os
import html2text
import glob
import re
import jsbeautifier

# Define input and output directories
HTML_DIR = 'html'
MARKDOWN_DIR = 'markdown'

def ensure_dir_exists(dir_path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")

def remove_navigation(content):
    """Remove the navigation section from the markdown content"""
    # Remove the header navigation section
    content = re.sub(
        r'\[FAQ\].*?\[ __ Going to production \]\([^)]+\)\n+',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove the sidebar navigation sections
    content = re.sub(
        r'\[Extend with\s+\*\*Go\*\*\].*?\[JS Types reference \]\([^)]+\)\n+',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Clean up any resulting extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def format_js_code(code):
    """Format JavaScript code to be more readable using jsbeautifier"""
    # Fix comments (ensure they start with //)
    code = re.sub(r'(?<=[^/])/(?!\s*/)\s*([^/])', r'// \1', code)
    
    # Split multiple statements into separate lines
    code = re.sub(r';\s*(?=\S)', ';\n', code)
    
    # Configure jsbeautifier options
    opts = jsbeautifier.default_options()
    opts.indent_size = 4
    opts.indent_char = ' '
    opts.max_preserve_newlines = 2
    opts.preserve_newlines = True
    opts.keep_array_indentation = True
    opts.break_chained_methods = False
    opts.indent_scripts = True
    opts.brace_style = 'collapse'
    opts.space_before_conditional = True
    opts.unescape_strings = True
    opts.jslint_happy = False
    opts.end_with_newline = False
    opts.wrap_line_length = 0
    opts.indent_empty_lines = False
    opts.templating = ['auto']
    
    # Pre-process the code to handle special cases
    code = re.sub(r'(\w+)\s*=\s*([^;]+?)(?=\s+\w+\s*=|\s*$)', r'\1 = \2;\n', code)
    
    # Beautify the code
    formatted = jsbeautifier.beautify(code, opts)
    
    # Post-process to fix any remaining issues
    formatted = re.sub(r'\n\s*\n', '\n', formatted)  # Remove extra newlines
    formatted = re.sub(r'}\s*else', '} else', formatted)  # Fix else spacing
    formatted = re.sub(r'(\w+)\s*=\s*([^;]+?)\s+(?=\w+\s*=)', r'\1 = \2;\n', formatted)  # Fix missing semicolons
    
    return formatted

def fix_code_blocks(content):
    """Add language tags to code blocks and fix their formatting"""
    # First, handle multi-line code blocks
    content = re.sub(
        r'`([^`]+)`(?=\n|$)',
        lambda m: process_code_block(m.group(1)),
        content
    )
    
    # Then handle inline code (single line)
    content = re.sub(
        r'`([^`\n]+)`',
        r'`\1`',
        content
    )
    
    return content

def process_code_block(code):
    """Process individual code blocks to determine language and format"""
    # Clean up the code
    code = code.strip()
    
    # Skip if it's just a single word or line without spaces
    if '\n' not in code and ' ' not in code:
        return f'`{code}`'
    
    # Detect the language based on content
    language = detect_language(code)
    
    # Format JavaScript code
    if language == 'javascript':
        code = format_js_code(code)
    
    # Return formatted code block with 4-space indentation
    return f'\n```{language}\n{code}\n```\n'

def detect_language(code):
    """Detect the programming language based on code content"""
    # JavaScript indicators
    js_indicators = [
        'const ', 'let ', 'var ', '=>', 'function', 'console.log',
        'new ', '$app.', 'null,', 'true,', 'false,', 'options:', 'Collection', 'form.'
    ]
    # HTML indicators
    html_indicators = ['<html', '<div', '<p>', '<a', '<script']
    # SQL indicators
    sql_indicators = ['SELECT ', 'INSERT ', 'CREATE ', 'ALTER ', 'DROP ']
    
    code_lower = code.lower()
    
    if any(indicator.lower() in code_lower for indicator in js_indicators):
        return 'javascript'
    elif any(indicator.lower() in code_lower for indicator in html_indicators):
        return 'html'
    elif any(indicator.lower() in code_lower for indicator in sql_indicators):
        return 'sql'
    
    # If code contains newlines but no specific language is detected,
    # still mark it as javascript for this specific documentation
    if '\n' in code:
        return 'javascript'
    
    return ''  # Default to no language specification

def transform_urls(content):
    """Transform online doc URLs to local markdown references"""
    # Replace links to documentation pages while preserving section anchors
    content = re.sub(
        r'https?://pocketbase\.io/old/docs/([^)#\s]+)(?:#([^)]+))?',
        lambda m: f'./{m.group(1)}.md{("#" + m.group(2)) if m.group(2) else ""}',
        content
    )
    
    # Fix empty section links while preserving anchors
    content = re.sub(
        r'\(\./([^/]+)/\.md(#[^)]+)?\)',
        lambda m: f'(./{m.group(1)}.md{m.group(2) if m.group(2) else ""})',
        content
    )
    
    # Fix self-referencing section links
    content = re.sub(
        r'\(\./([\w-]+)\.md#\1\)',
        lambda m: f'#{m.group(1)}',
        content
    )
    
    # Replace JSVM documentation links with a note
    content = re.sub(
        r'\(https?://pocketbase\.io/old/jsvm/[^)]+\)',
        '(https://pocketbase.io/docs/jsvm/)',
        content
    )
    
    # Clean up any double slashes in paths
    content = re.sub(r'(?<!:)/+', '/', content)
    
    return content

def convert_html_to_md(html_file):
    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(html_file))[0]
    
    # Create markdown filename in the markdown directory
    md_file = os.path.join(MARKDOWN_DIR, f"{base_name}.md")
    
    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Configure html2text
    h2t = html2text.HTML2Text()
    h2t.body_width = 0  # Don't wrap text
    h2t.ignore_links = False
    h2t.ignore_images = False
    h2t.ignore_emphasis = False
    h2t.ignore_tables = False
    h2t.ignore_anchors = False  # Make sure we preserve anchor IDs
    
    # Convert HTML to Markdown
    markdown_content = h2t.handle(html_content)
    
    # Transform URLs to point to local markdown files
    markdown_content = transform_urls(markdown_content)
    
    # Fix code blocks
    markdown_content = fix_code_blocks(markdown_content)
    
    # Remove navigation
    markdown_content = remove_navigation(markdown_content)
    
    # Write markdown content
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Converted {os.path.basename(html_file)} -> {os.path.basename(md_file)}")

def main():
    # Ensure output directory exists
    ensure_dir_exists(MARKDOWN_DIR)
    
    # Find all HTML files in the html directory
    html_files = glob.glob(os.path.join(HTML_DIR, '*.html'))
    
    if not html_files:
        print(f"No HTML files found in {HTML_DIR} directory")
        return
    
    print(f"Found {len(html_files)} HTML files")
    
    # Convert each HTML file
    for html_file in html_files:
        convert_html_to_md(html_file)
    
    print("\nConversion complete!")

if __name__ == '__main__':
    main() 