

class RedisBackend(object):
    """
    Redis backend.
    Requires redis-py library (https://github.com/andymccurdy/redis-py)

    Redis database should contain key-value pairs, where key follow the following pattern: "[PREFIX][TAGKEY]:[LANGUAGE]".
    E.g. for "hello_world" tag key in English it should be "pyslate_hello_world:en".
    Value should be a hash with fields "content" (required) and "form" (optional).
    Examples:
        pyslate_hello_world:en => {"content": "Hello world!"}
        pyslate_judy:en => {"content": "Policewoman Judy", "form": "f"}
    """

    def __init__(self, strict_redis, prefix="pyslate_"):
        """
        Must specify instance of StrictRedis class.
        :param strict_redis: handle to strict redis database
        :param prefix: prefix used in keys for all tag hashes
        :return: backend to use in Pyslate
        """

        self.redis = strict_redis
        self.prefix = prefix

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
        pipe = self.redis.pipeline()
        for language in languages:
            for tag_name in tag_names:
                pipe.hmget(self.prefix + tag_name + ":" + language, ["content", "form"])
        result_records = pipe.execute()

        for record in result_records:
            if record[0] is not None:
                return [self._save_decode_bytes(r) for r in record]
        return None

    @staticmethod
    def _save_decode_bytes(var):
        if var is None:
            return None
        return var.decode("utf-8")
