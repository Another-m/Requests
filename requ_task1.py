import requests

def get_hero(name_hero):
    url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
    response = requests.get(url + name_hero)

    if response.status_code == 200:
        heroes = response.json()
        intelligence = heroes['results'][0]['powerstats']['intelligence']
        return (name_hero, intelligence)
    else: print(response.status_code)

if __name__ == "__main__":
    hero_1 = get_hero('Hulk')
    hero_2 = get_hero('Captain America')
    hero_3 = get_hero('Thanos')

    result_dict = {hero_1[0]: hero_1[1], hero_2[0]: hero_2[1], hero_3[0]: hero_3[1]}

    print(result_dict)
    best_hero = list(max(result_dict.items()))
    print(f'Самый умный герой: {best_hero[0]}, Уровень интеллекта: {best_hero[1]}')