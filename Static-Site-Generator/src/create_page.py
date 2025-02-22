import re


class CreatePage():
    
    def extract_title(html: str):
        regex = r"^\s*\#{1}(?!\*)\s(?P<block_text>.*)"