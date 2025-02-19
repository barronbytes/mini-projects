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
        current_dir = os.path.dirname(__file__)
        root_dir = os.path.abspath(path=os.path.join(current_dir, ".."))
        root_contents = os.listdir(root_dir)
        root_dirs = [item for item in root_contents if os.path.isdir(os.path.join(root_dir, item))]
        return all([self.source in root_dirs, self.destination in root_dirs, self.source != self.destination])
