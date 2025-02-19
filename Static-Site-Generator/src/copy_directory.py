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
