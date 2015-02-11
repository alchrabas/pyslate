
class PyslateJsonBackend:

    TAGS = {
        "hello_world": {
            "en": "Hello world!",
            "pl": "Witaj swiecie!",
        }
    }

    def get_content(self, tag_name, language):
        return PyslateJsonBackend.TAGS[tag_name][language]
