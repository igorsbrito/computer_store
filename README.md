# Computer Store

- This is a simple store backend system in which the main functionality is the user can build a computer. This computer can
have 4 peaces of hardware, a mother board, a cpu, a memory ram and a video card.

- There`s only the following options of hardware

```
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

```

- The user must build the computer based on the following rules
(In Portuguese)
```
Processador
    ● É possível selecionar apenas um processador por máquina
Placa Mãe
    ● É possível selecionar apenas uma placa mãe por máquina
    ● A placa mãe deve suportar a marca (AMD ou Intel) do processador escolhido. Ex: Não
    deve ser possível selecionar a Placa Mãe Gigabyte (que suporta apenas AMD) se o
    processador escolhido foi o Processador Intel Core i5 (Intel)
Memória RAM
    ● A máquina deve ter pelo menos uma memória RAM
    ● A quantidade total de memórias que podem ser escolhidas dependem do quantidade
    de slots de memória da placa mãe escolhida. Ex: Não deve ser possível selecionar 4
    memórias RAM se a placa mãe escolhida foi a Placa Mãe Gigabyte (que possui apenas 2
    slots de memória)
    ● A quantidade total de armazenamento (em GB) não deve superar o total de memória
    RAM suportado pela placa mãe. Ex: Não deve ser possível selecionar 2 memórias RAM
    de 16 GB (totalizando 32 GB) se a placa mãe selecionada foi a Placa Mãe Gigabyte (que
    suporta até 16 GB)
Placa de Vídeo
    ● É possível selecionar apenas uma placa de vídeo para compor a máquina
    ● Se a placa mãe escolhida não possui vídeo integrado, o cliente deve selecionar
    obrigatoriamente uma placa de vídeo. Caso contrário, selecioná-la é opcional. Ex: Se a
    placa mãe selecionada foi a Placa Mãe ASRock Fatal (que possui vídeo integrado), não é
obrigatório selecionar uma placa de vídeo
```

## Built with
   - [Django](https://www.djangoproject.com/) - The web framework to make a web service with python
   - [Django Rest Framework](https://www.django-rest-framework.org/) - It`s a toolkit to help the the development of Web Apis on top of Django


## Installation and Configuration

In the root folder of the project i must have a virtual env with python 3.
Inside the env run a follow command to install all libraries required for the project.
```
    pip install -r requirements.txt
``` 

Locally this project will run with a sqlite database, the default database for django.

To create the tables execute the migrations like:

```
    python manage.py migrate
```

after that run the follow command to run the application

```
    python manage.py runserver 0.0.0.0:8000
```

### Django Admin (optional)
If you want to see the storage data in a "pretty UI", follow the next steps.

Create a super user
```
    python manage.py createsuperuser
```
fill the form creatingo your user to access the django admin, and enter in the url [localhost:8000/admin/](http://localhost:8000/admin/).

## Author
   - [Igor Brito](https://www.linkedin.com/in/igor-brito-916a60b1/)