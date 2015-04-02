
class PyslateJsonBackend:

    TAGS = {
        "hello_world": {
            "en": "Hello world!",
            "pl": "Witaj swiecie!",
        }
    }

    def get_content(self, tag_names, languages):
        return [PyslateJsonBackend.TAGS[tag_name][languages]for tag_name in tag_names]

    def get_form(self, tag_names, languages):
        pass
