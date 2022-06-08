from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, filepath):
        """Create a list of words from a file"""
        self.words = self._create_list_from_file(filepath)
        print(f"{len(self.words)} words read")


    def _create_list_from_file(self, filepath):
        """Read in lines from file and return as list, stripping new lines"""
        with open(filepath, "r") as file:
            return [line.strip() for line in file]

    def random(self):
        """Return random word from dictionary"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder:
        Word Finder that excludes commented lines and blank lines
    """

    def _create_list_from_file(self, filepath):
        """Read in lines from file and return as list,
            stripping new lines, blank lines, and commented lines
        """
        return ([word for word in super()._create_list_from_file(filepath)
            if not word.startswith("#") and word != ""])
