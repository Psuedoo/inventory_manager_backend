import random
import datetime
from models import Computer


def generate_computer(handler):
    make = 'Dell',
    model = f'Latitude {random.randint(1000, 9000)}'
    service_tag = f'{service_tag}'
    asset_tag = random.randint(124000, 126000)
    issued = random.choice([True, False])
    if issued:
        issuee = 'Test Issuee'
        on_hand = False
    else:
        issuee = None
        on_hand = random.choice([True, False])

    if on_hand:
        on_location = False
        location = None
        class_location = None
    else:
        on_location = True
        location = f'Classroom {random.choice(["2400", "2401", "2300", "2301"])}'
        class_location = random.choice(['Lab', 'Podium'])

    checker = random.choice(['Tracy', 'Stefan', 'Josh', 'Austin'])
    time_checked = datetime.datetime.now()
    notes = None

    computer = Computer(
        make=make,
        model=model,
        service_tag=service_tag,
        asset_tag=asset_tag,
        issued=issued,
        issuee=issuee,
        on_hand=on_hand,
        on_location=on_location,
        location=location,
        class_location=class_location,
        checker=checker,
        time_checked=time_checked,
        notes=notes
    )

    success = handler.add_computer(computer)

    if success:
        print('Successfully added')