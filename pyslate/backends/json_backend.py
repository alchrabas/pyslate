import json


class JsonBackend(object):
    """
    JSON-based backend. It has no external dependencies.

    """

    def __init__(self, file=None, json_data=None):
        """
        Must specify either file or json_data as string or json data as python dict.
        :param file: handle to file with JSON string
        :param json_data: JSON string or python dict with already parsed JSON string
        :return: backend to use in Pyslate
        """

        if file:
            self.tags = json.loads(file.read())
        else:
            if type(json_data) is str:
                self.tags = json.loads(json_data)
            else:
                self.tags = json_data

    def get_content(self, tag_names, languages):
        try:
            return self.get_record(tag_names, languages)[0]
        except:
            print("FAIL FOR", tag_names)
            raise

    def get_form(self, tag_names, languages):
        return self.get_record(tag_names, languages)[1]

    def get_record(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in self.tags.get(tag_name, {}):
                    translation = self.tags[tag_name][language]
                    if type(translation) is list:
                        return translation[0], translation[1]
                    return translation, None

