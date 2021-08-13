from database.db_handler import DatabaseHandler
from database.models import Computer
from utils.util import generate_computer


handler = DatabaseHandler()


for i in range(15):
   generate_computer(handler, i)


print(handler.search(one='one', two='two', make='Dell', service_tag="10"))

computer = handler.search(service_tag="10")
if len(computer) == 1:
    handler.remove_computer(computer[0])
else:
    print("Can't delete multiple computers!")



