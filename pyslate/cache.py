

class SimpleMemoryCache(object):

    def __init__(self):
        self.cache = {}

    def save(self, tag_name, language, content, form):
        self.cache[(tag_name, language)] = (content, form)

    def load(self, tag_name, language):
        if (tag_name, language) in self.cache:
            return self.cache[(tag_name, language)]
        return None
