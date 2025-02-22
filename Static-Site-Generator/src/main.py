from text_node import TextNode, TextType
from copy_directory import CopyDirectory

def main():
    tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(tn)
    brain = CopyDirectory("static", "public")
    brain.copy_parent_dir()

# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()
