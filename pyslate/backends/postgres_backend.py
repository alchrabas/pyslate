

class PostgresBackend(object):
    """
    Backend storing data in the PostgreSQL database. The specified table MUST have columns:
     - name (VARCHAR(?)
     - language (VARCHAR(8))
     - content (STRING)
     - form (VARCHAR(8))
    """

    def __init__(self, conn, table_name):
        """
        Constructor taking a handle to psycopg2 connection object and name of the table containing translations.
        Please note the table_name is not escaped in any way, so it's your responsibility to avoid risk of SQL injection
        :param conn: psycopg2 connection
        :param table_name: name of the table with translations, IT'S NOT SAFE AGAINST SQL INJECTION
        :return: backend usable in Pyslate
        """
        self.conn = conn
        self.table_name = table_name

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
        with self.conn.cursor() as cur:
            for language in languages:
                for tag_name in tag_names:
                    query_str = "SELECT content, form FROM " + self.table_name + " WHERE name = %s AND language = %s"
                    cur.execute(query_str, (tag_name, language))
                    ret = cur.fetchone()
                    if ret:
                        return ret
        return None
