import os
import re


class CreatePage():

    template_file = "template.html"
    markdown_file = "index.md"
    md_dir = "content"
    src_dir = "src"
    dst_dir = "public"

    @staticmethod
    def root_dir() -> str:
        file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        return root_dir

    @staticmethod
    def extract_title(markdown: str) -> str:
        regex = r"^\s*#\s+(?P<block_header>.+)$"
        pattern = re.compile(regex, flags=re.MULTILINE)
        match = pattern.search(markdown)  # returns first match only
        
        if not match:
            raise ValueError("No H1 header found inside the markdown.")
        
        return match.group("block_header").strip()
    
    @staticmethod
    def read_md_and_template() -> list[str]:
        root_dir = CreatePage.root_dir()
        markdown_path = os.path.join(root_dir, CreatePage.md_dir, CreatePage.markdown_file)
        template_path = os.path.join(root_dir, CreatePage.template_file)

        with open(file=markdown_path, mode="r", encoding="utf-8") as md_file:
            markdown = md_file.read()
        with open(file=template_path, mode="r", encoding="utf-8") as html_file:
            template = html_file.read()

        return [markdown, template]
    
    @staticmethod
    def create_page():
        markdown, template = CreatePage.read_md_and_template()
        pass
