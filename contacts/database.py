from abc import ABC
from sqlite3 import connect, Cursor, OperationalError
from typing import Optional


class Database(ABC):
    __database: str = './contacts/.contacts.s3db'
    __ADD: str = 'INSERT INTO contacts_list VALUES(NULL,?, ?,?)'
    __DELETE: str = 'DELETE FROM contacts_list WHERE name = ?'
    __UPDATE: str = 'UPDATE contacts_list SET number=? WHERE number =? AND name =?'

    @classmethod
    def execute(cls, query: str, parameters: tuple) -> bool:
        with connect(cls.__database) as database:
            cursor = database.cursor()
            try:
                cursor.execute(query, parameters)
                database.commit()
                return True
            except OperationalError:
                return False

    @classmethod
    def list(cls) -> Optional[list]:
        with connect(cls.__database) as database:
            cursor: Cursor = database.cursor()
            query: str = 'SELECT * FROM contacts_list ORDER BY name desc'
            try:
                cursor.execute(query)
                query: list = cursor.fetchall()
                return query
            except OperationalError:
                return None

    @classmethod
    def add(cls) -> str:
        return cls.__ADD

    @classmethod
    def delete(cls) -> str:
        return cls.__DELETE

    @classmethod
    def update(cls) -> str:
        return cls.__UPDATE
