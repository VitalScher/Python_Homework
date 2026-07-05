from sqlalchemy import create_engine, text


class SubjectsTable:
    __scripts = {
        "select": text("select * from subject"),
        "select max id": text("select max(subject_id) from subject"),
        "insert new subject": text("insert into subject (\"subject_id\", \"subject_title\") values (:id, :subject)"),
        "update title": text("update subject set subject_title = :subject where subject_id = :id"),
        "delete by id": text("delete from subject where subject_id = :id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def max_subjects_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select max id"])
        max_id = result.mappings().all()
        conn.close()
        return max_id[0]["max"]

    def create_new_subjects(self, subject_id: int, subject_title: str):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert new subject"],
                     {"id": subject_id,
                      "subject": subject_title})
        conn.commit()
        conn.close()

    def change_subject_title(self, subject_id: int, subject_title: str):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update title"],
                     {"id": subject_id,
                      "subject": subject_title})
        conn.commit()
        conn.close()

    def delete(self, subject_id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete by id"],
            {"id_to_delete": subject_id}
        )
        conn.commit()
        conn.close()
