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
            f"CopyDirectory(source=\"{self.source}\", destination={self.destination})"
        )
    
    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, CopyDirectory):
            equality = True if self.source == other.source and self.destination == other.destination else False
        return equality

    def root_dir(self) -> str:
        file_path = __file__
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        return root_dir

    def is_both_found(self) -> bool:
        root_dir = self.root_dir()
        root_contents = os.listdir(root_dir)
        root_dirs = [item for item in root_contents if os.path.isdir(os.path.join(root_dir, item))]
        return all([self.source in root_dirs, self.destination in root_dirs, self.source != self.destination])

    def wipe_destination(self) -> None:
        shutil.rmtree(self.destination)
        os.mkdir(self.destination)

    def copy_child_dir(self, dst_path: str) -> None:
        print(f"Creating directory: {dst_path}")
        parent_dir = os.path.dirname(dst_path)
        print("parent_dir: ", parent_dir)
        os.makedirs(dst_path)

    def copy_parent_dir(self) -> None:
        root_dir = self.root_dir()

        if self.is_both_found():
            source_dir = os.path.join(root_dir, self.source)
            destination_dir = os.path.join(root_dir, self.destination)
            self.wipe_destination()
            source_contents = os.listdir(source_dir)
            for item in source_contents:
                src_path = os.path.join(source_dir, item)
                dst_path = os.path.join(destination_dir, item)
                is_file = os.path.isfile(src_path)
                shutil.copy(src_path, dst_path) if is_file else self.copy_child_dir(dst_path)
