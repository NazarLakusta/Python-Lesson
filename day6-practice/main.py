from db.models import create_table
from crud.users import *

create_table()

# create_user("Vasia",49)

print(get_users())

update_user(1,25)
print(get_users())

delete_user(3)
print(get_users())