import re


class CreatePage():
    
    @staticmethod
    def extract_title(markdown: str) -> str:
        regex = r"^\s*#\s+(?P<block_header>.+)$"
        pattern = re.compile(regex, flags=re.MULTILINE)
        match = pattern.search(markdown)  # returns first match only
        
        if not match:
            raise ValueError("No H1 header found inside the markdown.")
        
        return match.group("block_header").strip()