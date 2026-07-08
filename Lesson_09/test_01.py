from sqlalchemy import create_engine
from pages.sql_page import SubjectsTable


db_connection_string = "postgresql://postgres:DominA@localhost:5433/QA"

db = create_engine(db_connection_string)

st = SubjectsTable(db_connection_string)


def test_add_new_subject():
    body = st.get_subjects()
    len_before = len(body)

    max_id_before = st.max_subjects_id()
    new_id = max_id_before + 1
    new_subject = "Sociology"

    st.create_new_subjects(new_id, new_subject)

    body = st.get_subjects()
    len_after = len(body)
    max_id_after = st.max_subjects_id()

    st.delete(max_id_after)

    assert len_after - len_before == 1


def test_change_subject_title():
    max_id_before = st.max_subjects_id()
    new_id = max_id_before + 1
    new_subject = "Sociology"

    st.create_new_subjects(new_id, new_subject)

    new_title = "Psychology"
    st.change_subject_title(new_id, new_title)

    body = st.get_subjects()
    result = body[-1]["subject_title"]

    max_id_after = st.max_subjects_id()
    st.delete(max_id_after)

    assert result == new_title


def test_delete():
    max_id_before = st.max_subjects_id()
    new_id = max_id_before + 1
    new_subject = "Sociology"

    st.create_new_subjects(new_id, new_subject)
    st.delete(new_id)
    max_id_after = st.max_subjects_id()

    assert max_id_before == max_id_after
