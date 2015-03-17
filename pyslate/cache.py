__author__ = 'Aleksander Chrabaszcz'


class SimpleMemoryCache:

    def __init__(self):
        self.cache = {}

    def save(self, tag_name, language, contents):
        self.cache[(tag_name, language)] = contents

    def load(self, tag_name, language):
        if (tag_name, language) in self.cache:
            return self.cache[(tag_name, language)]
        return None
