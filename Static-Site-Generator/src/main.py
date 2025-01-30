from text_node import TextNode, TextType


def main():
    tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(tn)

# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()
