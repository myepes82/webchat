from psycopg2 import connect
from utils import error_message

CONNECTION_PARAMS = {
    "host": "localhost",
    "port": 5532,
    "database": "chatweb",
    "password": 1234
}
class Database:
    connection: any
    def start(self):
        try:
            self.connection = connect(CONNECTION_PARAMS)
            return self.connection
        except ConnectionError as error:
            error_message(f'Error connecting database -> {error}')
            raise(error)
    
    def close(self) -> None:
         self.connection.close()
    