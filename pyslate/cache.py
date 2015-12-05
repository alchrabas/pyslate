

class SimpleMemoryCache(object):

    def __init__(self):
        self.cache = {}

    def save(self, tag_name, language, content, form):
        self.cache[(tag_name, language)] = (content, form)

    def load(self, tag_name, language):
        if (tag_name, language) in self.cache:
            return self.cache[(tag_name, language)]
        return None

    def remove(self, tag_name):
        for tag_language_tuple in self.cache:
            if tag_language_tuple[0] == tag_name:
                self.cache.pop(tag_language_tuple, None)

    def clear(self):
        self.cache.clear()