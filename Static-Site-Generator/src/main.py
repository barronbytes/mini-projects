from copy_directory import CopyDirectory
from create_page import CreatePage


def main():
    brain = CopyDirectory("static", "public")
    brain.copy_parent_dir()
    CreatePage.create_pages()


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()
