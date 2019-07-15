CPU = [{'name': 'Processador Intel Core i5', 'brand': 'Intel'},
       {'name': 'Processador Intel Core i7', 'brand': 'Intel'},
       {'name': 'Processador AMD Athlon', 'brand': 'AMD'},
       {'name': 'Processador AMD Ryzen 7', 'brand': 'AMD'},
       ]

MOTHER_BOARD = [{'name': 'Placa Mãe Asus Prime', 'cpu_support': ['Intel'], 'ram_slots': 2, 'total_ram': 16,
                 'video_built_in': False},
                {'name': 'Placa Mãe Gigabyte', 'cpu_support': ['AMD'], 'ram_slots': 2, 'total_ram': 16,
                 'video_built_in': False},
                {'name': 'Placa Mãe ASRock Fatal', 'cpu_support': ['Intel', 'AMD'], 'ram_slots': 4, 'total_ram': 16,
                 'video_built_in': True},
                ]
RAM_MEMORY = [{'name':'Hiper X', 'sizes': [4, 8,  16, 32, 64]}]

VIDEO_CARD = [{'name': 'Placa de Video Gigabyte Geforce GTX 1060 6GB'},
              {'name': 'Placa de Video PNY RTX 2060 6GB'},
              {'name': 'Placa de Video Radeon RX 580 8GB'},
              ]
