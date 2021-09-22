from sqlite3 import connect, OperationalError


class Database:
    __database: str = './contacts/.contacts.s3db'

    @classmethod
    def execute(cls, query: str, parameters: tuple) -> bool:
        with connect(cls.__database) as database:
            print(database)
            print('You have successfully connected to the Database')
            cursor = database.cursor()
            try:
                cursor.execute(query, parameters)
                database.commit()
                return True
            except OperationalError:
                return False
