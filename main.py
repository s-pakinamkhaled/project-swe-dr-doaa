
import random
import pytest
from main import movies, clothes, traveling, food, gaming, sports, recommend_games



def test_movies():
    assert movies('action', 'short', 'series') == ['night agent']
    assert movies('comedy', 'long', 'movie') == ['jumanji']
    assert movies('fiction', 'invalid_time', 'series') == "Invalid time preference. Please choose short or long."


def test_clothes():
    assert clothes('hot', 'event', 'red') == ['formal cocktail dress']
    assert clothes('cold', 'gym', 'blue') == ['blue hoodie and sweatpants']
    assert clothes('invalid_weather', 'event', 'black') == "Invalid weather. Please choose hot or cold."


def test_traveling():
    assert traveling('yes', 'touristic', 'cold') == ['switzerland']
    assert traveling('no', 'fun', 'hot') == ['kazakhstan']
    assert traveling('invalid_choice', 'touristic', 'cold') == "Invalid choice for beach. Please choose yes or no."


def test_food():
    assert food('midday', 'yes', 'wednesday') == 'rice and steamed broccoli'
    assert food('evening', 'no', 'sunday') == 'spaghetti and chicken'
    assert food('morning', 'invalid_choice', 'tuesday') == "Invalid choice for allergies. Please choose yes or no."


def test_gaming():
    assert gaming('girls', 'boring') == ['dance competition']
    assert gaming('boys', 'happy') == ['playstation', 'chess']
    assert gaming('invalid_gathering', 'party') == "Invalid gathering. Please choose boys or girls."


def test_sports():
    assert sports('teenagers') in ['football', 'tennis']
    assert sports('child') == 'swimming'
    assert sports('invalid_age') == "Invalid age group. Please choose child, teenagers, or adult."


def test_recommend_games():
    assert recommend_games('home') in ['play cards or chess']
    assert recommend_games('outdoors') in ['horseshoes', 'dodgeball']
    assert recommend_games('invalid_location') == "Invalid location. Please choose home, outdoors, indoors, beach, or park."


def movies(mood, time, series_movie):
    movies = [['maze runner', 'fiction', 'long', 'movie'],
              ['divergent', 'fiction', 'short', 'movie'],
              ['the vampire diaries', 'fiction', 'long', 'series'],
              ['julie and the phantoms', 'fiction', 'short', 'series'],
              ['top gun', 'action', 'short', 'movie'],
              ['fast and furious', 'action', 'long', 'movie'],
              ['night agent', 'action', 'short', 'series'],
              ['breaking bad', 'action', 'long', 'series'],
              ['never have i ever', 'comedy', 'short', 'series'],
              ['jumanji', 'comedy', 'long', 'movie'],
              ['friends', 'comedy', 'long', 'series'],
              ['free guy', 'comedy', 'short', 'movie']]


    if mood not in ['fiction', 'action', 'comedy']:
        return "Invalid mood. Please choose fiction, action, or comedy."

    if time not in ['short', 'long']:
        return "Invalid time preference. Please choose short or long."

    if series_movie not in ['movie', 'series']:
        return "Invalid preference. Please choose movie or series."


    result = [item[0] for item in movies if item[1] == mood and item[2] == time and item[3] == series_movie]
    return result if result else "No matching movies found."


def clothes(weather, occasion, colors):
    femaleclothes = [['event', 'cold', 'red', 'formal long sleeve dress or formal red suit jacket with matching pants'],
                     ['hang out', 'cold', 'red', 'puffed red jacket with black jeans'],
                     ['event', 'hot', 'red', 'formal cocktail dress'],
                     ['gym', 'hot', 'red', 'red joggers with white t-shirt'],
                     ['gym', 'cold', 'red', 'red hoodie with joggers'],
                     ['event', 'cold', 'blue', 'blue suit with a black coat'],
                     ['hang out', 'cold', 'blue', 'blue jeans with black puffer jacket'],
                     ['event', 'hot', 'blue', 'blue skirt with a white top'],
                     ['gym', 'hot', 'blue', 'blue tank top with sweat shorts'],
                     ['gym', 'cold', 'blue', 'blue hoodie and sweatpants'],
                     ['event', 'cold', 'black', 'black coat with a dress'],
                     ['gym', 'cold', 'black', 'black hoodie with joggers'],
                     ['hangout', 'cold', 'black', 'black hoodie and jeans'],
                     ['gym', 'hot', 'black', 'black sweatpants and a t-shirt'],
                     ['event', 'hot', 'black', 'black dress'],
                     ['event', 'cold', 'pink', 'pink suit'],
                     ['event', 'hot', 'pink', 'pink dress or pink suit'],
                     ['hangout', 'cold', 'pink', 'pink jacket with black pants'],
                     ['hangout', 'hot', 'pink', 'pink shorts with a white tank top'],
                     ['gym', 'hot', 'pink', 'pink sweats and tank top'],
                     ['gym', 'cold', 'pink', 'pink hoodie and sweatpants']]


    if weather not in ['hot', 'cold']:
        return "Invalid weather. Please choose hot or cold."

    if occasion not in ['hang out', 'event', 'gym']:
        return "Invalid occasion. Please choose hang out, event, or gym."

    if colors not in ['red', 'black', 'blue', 'pink']:
        return "Invalid color. Please choose red, black, blue, or pink."

    # Filter clothes based on user preferences
    result = [item[3] for item in femaleclothes if item[0] == occasion and item[1] == weather and item[2] == colors]
    return result if result else "No matching clothes found."


def traveling(beach, touristic_fun, weather):
    destinations = {
        'yes': {
            'touristic': {
                'hot': ['spain (canary island)', 'portugal', 'paris'],
                'cold': ['switzerland'],
            },
            'fun': {
                'hot': ['austria', 'serbia'],
                'cold': ['cyprus', 'maldives', 'kazakhstan'],
            },
        },
        'no': {
            'touristic': {
                'hot': ['iceland', 'italy', 'germany'],
                'cold': ['new zealand', 'canada'],
            },
            'fun': {
                'hot': ['kazakhstan'],
                'cold': ['zambia'],
            },
        },
    }


    if beach not in ['yes', 'no']:
        return "Invalid choice for beach. Please choose yes or no."

    if touristic_fun not in ['touristic', 'fun']:
        return "Invalid choice for touristic/fun. Please choose touristic or fun."

    if weather not in ['hot', 'cold']:
        return "Invalid weather. Please choose hot or cold."


    result = destinations.get(beach, {}).get(touristic_fun, {}).get(weather, [])
    return result if result else "No matching destinations found."


def food(date, allergies, day):
    menu = {
        'morning': {'no': {'sunday': 'waffle and coffee or pancakes',
                           'monday': 'omelette and orange juice',
                           'tuesday': 'salmon with coffee',
                           'wednesday': 'nuts and sandwich'},
                    'yes': {'sunday': 'oats and orange juice',
                            'monday': 'muffin and orange juice',
                            'tuesday': 'cupcake with tea',
                            'wednesday': 'waffle'}},
        'midday': {'no': {'sunday': 'rice and chicken stew and coleslaw',
                          'monday': 'shawarma and cola',
                          'tuesday': 'fish with cola',
                          'wednesday': 'burger'},
                   'yes': {'sunday': 'swallow soup',
                           'monday': 'tuna',
                           'tuesday': 'pizza and juice',
                           'wednesday': 'rice and steamed broccoli'}},
        'evening': {'no': {'sunday': 'spaghetti and chicken',
                            'monday': 'tuna salad with cola',
                            'tuesday': 'pizza and cola',
                            'wednesday': 'sushi'},
                    'yes': {'sunday': 'steak and rice',
                            'monday': 'sandwich',
                            'tuesday': 'fruit salad',
                            'wednesday': 'potato'}}
    }


    if date not in ['morning', 'midday', 'evening']:
        return "Invalid time of day. Please choose morning, midday, or evening."

    if allergies not in ['yes', 'no']:
        return "Invalid choice for allergies. Please choose yes or no."

    if day not in ['sunday', 'monday', 'tuesday', 'wednesday']:
        return "Invalid day. Please choose sunday, monday, tuesday, or wednesday."


    result = menu.get(date, {}).get(allergies, {}).get(day, "No matching food found.")
    return result


def gaming(gathering, mood):
    games = {
        'boys': {'happy': ['playstation', 'chess'],
                 'sad': ['soccer'],
                 'relaxing': ['super smash'],
                 'party': ['just dance'],
                 'fighting': ['mortal kombat'],
                 'competitive': ['fifa']},
        'girls': {'happy': ['chess'],
                  'sad': ['singing'],
                  'party': ['dancing and singing'],
                  'boring': ['dance competition']}
    }


    if gathering not in ['boys', 'girls']:
        return "Invalid gathering. Please choose boys or girls."

    if mood not in ['happy', 'sad', 'relaxing', 'party', 'fighting', 'competitive']:
        return "Invalid mood. Please choose happy, sad, relaxing, party, fighting, or competitive."


    result = games.get(gathering, {}).get(mood, "No matching games found.")
    return result


def sports(age):
    sports_dict = {
        'child': 'swimming',
        'teenagers': random.choice(['football', 'tennis']),
        'adult': random.choice(['hockey', 'hiking'])
    }


    if age not in ['child', 'teenagers', 'adult']:
        return "Invalid age group. Please choose child, teenagers, or adult."


    result = sports_dict.get(age, "No matching sport found.")
    return result


def recommend_games(location):
    games_dict = {
        'home': 'play cards or chess',
        'outdoors': random.choice(['horseshoes', 'dodgeball']),
        'indoors': random.choice(['pool', 'tennis']),
        'beach': random.choice(['volleyball', 'sandcastle building']),
        'park': 'soccer'
    }


    if location not in ['home', 'outdoors', 'indoors', 'beach', 'park']:
        return "Invalid location. Please choose home, outdoors, indoors, beach, or park."


    result = games_dict.get(location, "No matching game found.")
    return result



if __name__ == "__main__":
    print("Movies Recommendation:", movies('action', 'short', 'series'))
    print("Clothes Recommendation:", clothes('hot', 'event', 'red'))
    print("Traveling Recommendation:", traveling('yes', 'touristic', 'cold'))
    print("Food Recommendation:", food('midday', 'yes', 'wednesday'))
    print("Gaming Recommendation:", gaming('girls', 'boring'))
    print("Sports Recommendation:", sports('adult'))
    print("Recommend Games:", recommend_games('mountains'))
