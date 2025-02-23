import os
import re

from block_markdown import BlockMarkdown


class CreatePage():

    template_file = "template.html"
    md_dir_file = {"dir": "content", "file": "index.md"}
    html_dir_file = {"dir": "public", "file": "index.html"}
 
    @staticmethod
    def root_dir() -> str:
        file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        return root_dir

    @staticmethod
    def extract_title(markdown: str) -> str:
        regex = r"^\s*#\s+(?P<block_header>.+)$"
        pattern = re.compile(pattern=regex, flags=re.MULTILINE)
        match = pattern.search(markdown)  # returns first match only
        
        if not match:
            raise ValueError("No H1 header found inside the markdown.")
        
        return match.group("block_header").strip()
    
    @staticmethod
    def read_md_and_template() -> list[str]:
        root_dir = CreatePage.root_dir()
        markdown_path = os.path.join(root_dir, CreatePage.md_dir_file["dir"], CreatePage.md_dir_file["file"])
        template_path = os.path.join(root_dir, CreatePage.template_file)

        with open(file=markdown_path, mode="r", encoding="utf-8") as md_file:
            markdown = md_file.read()
        with open(file=template_path, mode="r", encoding="utf-8") as html_file:
            template = html_file.read()

        return [markdown, template]

    @staticmethod
    def create_page() -> None:
        # read markdown and template files to variables
        markdown, template = CreatePage.read_md_and_template()

        # split markdown to blocks, convert to HTML, combine
        md_parts = CreatePage.split_markdown_parts(markdown)
        blocks = [BlockMarkdown(part) for part in md_parts]
        html_nodes = [block.to_html() for block in blocks]
        html = "".join(html_nodes)

        # clean html, extract page title, insert page html and title to template
        page_html = re.sub(pattern="</div><div>", repl="", string=html)
        page_title = CreatePage.extract_title(markdown)
        template = template.replace("{{ Title }}", page_title)
        template = template.replace("{{ Content }}", page_html)
        template = template.replace("</ul><p> </p><ul>", "")
        template = template.replace("</ol><p> </p><ol>", "")

        # write template to destination path if directory exists and path doesn't exist
        html_path = os.path.join(CreatePage.root_dir(), CreatePage.html_dir_file["dir"], CreatePage.html_dir_file["file"])
        dst_dir_path = os.path.dirname(html_path)
        if dst_dir_path and not os.path.exists(dst_dir_path):
            os.makedirs(dst_dir_path, exist_ok=True)
        with open(file=html_path, mode="w", encoding="utf-8") as page_file:
            page_file.write(template)

    @staticmethod
    def split_markdown_parts(markdown: str) -> list[str]:
        regex = r"(```[\s\S]*?```)"
        pattern = re.compile(pattern=regex, flags=re.MULTILINE)
        matches = re.split(pattern, markdown)
        parts = [part for part in matches if part] # removes empty strings but keeps whitespace inside blocks
        return parts
