import random
import datetime
from database.models import Computer, User, Role

def generate_data(handler, count):
    """Generates fake data for database"""
    user_role = Role(
        name="User"
    )

    admin_role = Role(
        name="Admin"
    )
    handler.add_role(user_role)

    handler.add_role(admin_role)


    user_one = User(
        name="John Adams",
        username="jadams",
        password="password123",
        email="jadams@test.com",
        role=handler.search('Role', {'id': 1}).first()
    )
    handler.add_user(user_one)
    user_two = User(
        name="John Doe",
        username="jdoe",
        password="password123",
        email="jdoe@test.com",
        role=handler.search('Role', {'id': 2}).first()
    )
    handler.add_user(user_two)

    for i in range(count):
        handler.add_computer(generate_computer(handler, i))

def generate_computer(handler, service_tag):

    make = 'Dell',
    model = f'Latitude {random.randint(1000, 9000)}'
    service_tag = f'{service_tag}'
    asset_tag = f'{random.randint(124000, 126000)}'
    issued = random.choice([True, False])
    if issued:
        assigned_to = 'Test Issuee'
        on_hand = False
    else:
        assigned_to = 'Unassigned'
        on_hand = random.choice([True, False])

    if on_hand:
        on_location = False
        computer_location = 'Storage'
        class_location = 'N/A'
    else:
        on_location = True
        computer_location = f'Classroom {random.choice(["2400", "2401", "2300", "2301"])}'
        class_location = random.choice(['Lab', 'Podium'])

    checker = handler.search('User', {'id': random.randint(1, 2)}).first()
    time_checked = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 100), hours=random.randint(1, 12))

    computer = Computer(
        make=make,
        model=model,
        service_tag=service_tag,
        asset_tag=asset_tag,
        issued=issued,
        assigned_to=assigned_to,
        on_hand=on_hand,
        on_location=on_location,
        computer_location=computer_location,
        class_location=class_location,
        checker=checker,
        time_checked=time_checked,
        notes=None
    )

    return computer

    # success = handler.add_computer(computer)

    # if success:
    #     print('Successfully added')
