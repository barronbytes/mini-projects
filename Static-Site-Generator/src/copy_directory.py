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

    def is_both_found(self) -> bool:
        file_path = __file__
        current_dir = os.path.dirname(file_path)
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))
        root_contents = os.listdir(root_dir)
        root_dirs = [item for item in root_contents if os.path.isdir(os.path.join(root_dir, item))]
        return all([self.source in root_dirs, self.destination in root_dirs, self.source != self.destination])

    def wipe_destination(self) -> None:
        is_both_found = self.is_both_found()
        if is_both_found:
            shutil.rmtree(self.destination)
            os.mkdir(self.destination)
