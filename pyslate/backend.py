import json


class PyslateJsonBackend(object):

    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.tags = json.loads(file.read())

    def get_content(self, tag_names, languages):
        return self.get_translation_record(tag_names, languages)[0]

    def get_form(self, tag_names, languages):
        return self.get_translation_record(tag_names, languages)[1]

    def get_translation_record(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in self.tags.get(tag_name, {}):
                    translation = self.tags.TAGS[tag_name][language]
                    if type(translation) is list:
                        return translation[0], translation[1]
                    return translation, None
