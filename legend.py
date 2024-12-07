import random

def read(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


characters = read('characters.txt')
places = read('places.txt')
events = read('events.txt')
secrets = read('secrets.txt')


def generate():
    character = random.choice(characters)
    place = random.choice(places)
    event = random.choice(events)
    secret = random.choice(secrets)

    legend = (f"В одном далёком королевстве, {character} был связан с {place}, где произошёл {event}. "
              f"Всё это было связано с загадочным кодом, который {secret}. Только тот, кто разгадает его, сможет раскрыть все тайны.")
    return legend


for i in range(100):
    print(f"Легенда {i + 1}:\n{generate()}\n")
