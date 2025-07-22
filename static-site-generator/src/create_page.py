import os
import re

from block_markdown import BlockMarkdown


class CreatePage():

    template_file = "template.html"
    src_dir_file = {"dir": "content", "file": ".md"}
    dst_dir_file = {"dir": "public", "file": ".html"}
 
    @staticmethod
    def root_dir() -> str:
        file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        return root_dir

    @staticmethod
    def find_md_paths(md_dir: str) -> list[str]:
        """
        Returns 'content' folder files ending in 'index.md'
        """
        md_paths = []
        # os.walk() traverses directory to return folders, subfolders (ignored here), files
        for folder, _, files in os.walk(md_dir):
            md_paths.extend(
                os.path.join(folder, file)
                for file in files
                if file.endswith(CreatePage.src_dir_file["file"])
            )
        return md_paths

    @staticmethod
    def read_template() -> str:
        template_path = os.path.join(CreatePage.root_dir(), CreatePage.template_file) 
        with open(file=template_path, mode="r", encoding="utf-8") as html_file:
            template = html_file.read()
        return template

    @staticmethod
    def read_markdown(md_path: str) -> str:
        with open(file=md_path, mode="r", encoding="utf-8") as md_file:
            markdown = md_file.read()
        return markdown

    @staticmethod
    def extract_title(markdown: str) -> str:
        regex = r"^\s*#\s+(?P<block_header>.+)$"
        pattern = re.compile(pattern=regex, flags=re.MULTILINE)
        match = pattern.search(markdown)  # returns first match only
        
        if not match:
            raise ValueError("No H1 header found inside the markdown.")
        
        return match.group("block_header").strip()

    @staticmethod
    def md_to_html(markdown: str) -> str:
        """
        Use CODE type to split markdown into parts, convert to HTML nodes, join nodes
        """
        md_parts = CreatePage.split_markdown_parts(markdown)
        blocks = [BlockMarkdown(part) for part in md_parts]
        html_nodes = [block.to_html() for block in blocks]
        html = "".join(html_nodes)
        return CreatePage.clean_html(html)

    @staticmethod
    def split_markdown_parts(markdown: str) -> list[str]:
        regex = r"(```[\s\S]*?```)"
        pattern = re.compile(pattern=regex, flags=re.MULTILINE)
        matches = re.split(pattern, markdown)
        parts = [part for part in matches if part] # removes empty strings but keeps whitespace inside blocks
        return parts

    @staticmethod
    def clean_html(html: str) -> str:
        clean_html = re.sub(pattern="</div><div>", repl="", string=html)
        clean_html = clean_html.replace("</ul><p> </p><ul>", "")
        clean_html = clean_html.replace("</ol><p> </p><ol>", "")
        clean_html = clean_html.replace("<p> </p>", "")
        return clean_html    

    @staticmethod
    def create_template(template: str, title: str, html: str) -> str:
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        return template

    @staticmethod
    def write_page(template: str, dst_path: str) -> None:
        base_folder = os.path.join(CreatePage.root_dir(), CreatePage.dst_dir_file["dir"])
        relative_path = os.path.relpath(path=dst_path, start=base_folder)
        dst_dir = os.path.join(base_folder, os.path.dirname(relative_path))
        os.makedirs(dst_dir, exist_ok=True)
        with open(file=dst_path, mode="w", encoding="utf-8") as page_file:
            page_file.write(template)

    @staticmethod
    def create_pages() -> None:
        md_dir = os.path.join(CreatePage.root_dir(), CreatePage.src_dir_file["dir"])
        md_paths = CreatePage.find_md_paths(md_dir) 
        markdowns = [CreatePage.read_markdown(path) for path in md_paths]
        titles = [CreatePage.extract_title(md) for md in markdowns]
        htmls = [CreatePage.md_to_html(md) for md in markdowns]

        template = CreatePage.read_template()
        templates = [CreatePage.create_template(template, title, html) for title, html in zip(titles, htmls)]

        dst_paths = [path.replace(CreatePage.src_dir_file["dir"], CreatePage.dst_dir_file["dir"]) for path in md_paths]
        dst_paths = [path.replace(CreatePage.src_dir_file["file"], CreatePage.dst_dir_file["file"]) for path in dst_paths]
        for temp, path in zip(templates, dst_paths):
            CreatePage.write_page(temp, path)
