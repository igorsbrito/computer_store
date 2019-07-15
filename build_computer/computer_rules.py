from .constants import CPU, MOTHER_BOARD, RAM_MEMORY, VIDEO_CARD


def find_component_by_name(dict, element_name):
    return next((element for element in dict if element['name'] == element_name), None)


# Verify if the computer have de minimum require component
def computer_components_exists(data):
    have_mother_board = False
    have_cpu = False
    have_ram = False

    if 'mother_board' in data:
        have_mother_board = True

    if 'cpu' in data:
        have_cpu = True

    if 'ram' in data:
        have_ram = True

    return have_ram and have_cpu and have_mother_board


# verify all the components and return the components objects
def components_amount(data):
    cpu_obj = cpu_amount(data)
    mother_board_obj = mother_board_amount(data)
    ram_list = ram_amount(data)

    video_card_obj = None
    if 'video_card' in data:
        video_card_obj = video_card_amount(data)

    components = {'cpu': cpu_obj, 'mother_board': mother_board_obj, 'ram': ram_list, 'video_card': video_card_obj}

    if cpu_obj is None or mother_board_obj is None or ram_list is None:
        return 'fail', components

    return 'success', components


def components_compatibility(components):
    no_issue = True
    msg = ''

    if not mother_board_support_cpu(components['mother_board'], components['cpu']):
        no_issue = False
        msg += ' Mother Board does not support CPU`s brand.\n'

    if not qnt_ram_support_mother_board(components['mother_board'], components['ram']):
        no_issue = False
        msg += ' The Quantity of memory ram is bigger than the quantity of mother board`s slots.\n '

    if not total_ram_support_mother_board(components['mother_board'], components['ram']):
        no_issue = False
        msg += ' The total amont Gb of the memory ram is bigger than the quantity of memory the mother board supports'

    if not mother_board_needs_video_card(components['mother_board'], components['video_card']):
        no_issue = False
        msg += ' The mother board does not have video built-in, you must select a video card'

    return no_issue, msg


def mother_board_needs_video_card(mother_board, video_card):
    if not mother_board['video_built_in'] and video_card is None:
        return False

    return True


def total_ram_support_mother_board(mother_board, ram_list):
    total = 0
    for ram in ram_list:
        total += ram['size']

    if total <= mother_board['total_ram']:
        return True
    return False


def qnt_ram_support_mother_board(mother_board, ram):
    if len(ram) <= mother_board['ram_slots']:
        return True
    return False


def mother_board_support_cpu(mother_board, cpu):
    cpu_brand = cpu['brand']
    if cpu_brand in mother_board['cpu_support']:
        return True
    return False


# verify if the slected cpu exists in the store list
def cpu_amount(data):
    cpu = data['cpu']
    return find_component_by_name(CPU, cpu)


# verify if the selected mother board exists in the store list
def mother_board_amount(data):
    mother_board = data['mother_board']
    return find_component_by_name(MOTHER_BOARD, mother_board)


# verify if the selected ram exists in the store list
def ram_amount(data):

    ram_list = data['ram']

    if len(ram_list) <= 0:
        return None

    ram_list_obj = []
    for ram in ram_list:
        ram_obj = find_component_by_name(RAM_MEMORY, ram['name'])

        if ram_obj is None:
            return None

        if not ram['size'] in ram_obj['sizes']:
            return None

        ram_list_obj.append(ram)

    return ram_list_obj


# verify if the selected video card exists in the store list
def video_card_amount(data):
    video_card = data['video_card']
    return find_component_by_name(VIDEO_CARD, video_card)
