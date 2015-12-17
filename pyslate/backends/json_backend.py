import json
import six


class JsonBackend(object):
    """
    JSON-based backend. It has no external dependencies.
    """

    def __init__(self, file_name=None, file=None, json_data=None):
        """
        Must specify one of these keyword arguments: file name, file handle
        or json_data as string or json data as python dict.
        :param file_name: name of file with
        :param file: handle to file with JSON string
        :param json_data: JSON string or python dict with already parsed JSON string
        :return: backend to use in Pyslate
        """

        if file_name:
            with open(file_name, "r") as file:
                self.tags = json.loads(file.read())
        elif file:
            self.tags = json.loads(file.read())
        elif json_data:
            if isinstance(json_data, six.string_types):
                self.tags = json.loads(json_data)
            else:
                self.tags = json_data
        else:
            raise ValueError("You must specify an input (file, file name, dict or string) in the constructor")

    def get_content(self, tag_names, languages):
        record = self.get_record(tag_names, languages)
        if record:
            return record[0]
        return None

    def get_form(self, tag_names, languages):
        record = self.get_record(tag_names, languages)
        if record:
            return record[1]
        return None

    def get_record(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in self.tags.get(tag_name, {}):
                    translation = self.tags[tag_name][language]
                    if type(translation) is list:
                        return translation[0], translation[1]
                    return translation, None
        return None
