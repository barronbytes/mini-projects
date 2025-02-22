import os
import shutil


class CopyDirectory():

    def __init__(self, source: str, destination: str):
        '''
        Initializes a CopyDirectory instance.

        Parameters:
            source (str): String for source directory name.
            destination (str): String for destination directory name.
=        '''
        self.source = source
        self.destination = destination

    # object string representation
    def __repr__(self) -> str:
        return (
            f"CopyDirectory(source=\"{self.source}\", destination=\"{self.destination}\")"
        )
    
    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, CopyDirectory):
            equality = True if self.source == other.source and self.destination == other.destination else False
        return equality

    def root_dir(self) -> str:
        file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        return root_dir

    def is_both_found(self) -> bool:
        root_dir = self.root_dir()
        root_contents = os.listdir(root_dir)
        root_dirs = [item for item in root_contents if os.path.isdir(os.path.join(root_dir, item))]
        return all([self.source in root_dirs, self.destination in root_dirs, self.source != self.destination])

    def wipe_destination(self) -> None:
        root_dir = self.root_dir()
        dst_path = os.path.join(root_dir, self.destination)
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        os.mkdir(dst_path)

    def copy_child_dir(self, src_path: str, dst_path: str) -> None:
        os.mkdir(dst_path)
        source_contents = os.listdir(src_path)
        if source_contents:
            for item in source_contents:  # copy contents of the subfolder
                src_item = os.path.join(src_path, item)
                dst_item = os.path.join(dst_path, item)
                is_file = os.path.isfile(src_item)
                shutil.copy(src_item, dst_item) if is_file else self.copy_child_dir(src_item, dst_item)

    def copy_parent_dir(self) -> None:
        root_dir = self.root_dir()

        if self.is_both_found():
            src_path = os.path.join(root_dir, self.source)
            dst_path = os.path.join(root_dir, self.destination)
            self.wipe_destination()
            source_contents = os.listdir(src_path)
            for item in source_contents:
                src_item = os.path.join(src_path, item)
                dst_item = os.path.join(dst_path, item)
                is_file = os.path.isfile(src_item)
                shutil.copy(src_item, dst_item) if is_file else self.copy_child_dir(src_item, dst_item)
