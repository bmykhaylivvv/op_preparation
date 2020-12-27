def read_file(path):
    """
    (str) -> (set)
    Return set of lines from file
    """
    lines = []
    with open(path, 'r', encoding='utf-8') as films:
       for film in films:
           lines.append(film.rstrip())
    return set(lines[1:])

# print(read_file('brief_data.tsv'))

def votes_dict(lines_set, num_v):
    """
    (set, int) -> (dict)
    Return dict from set of lines if number of votes > num_v
    """
    lines_lst = list(lines_set)
    lst = []
    lst_with_proper_votes_number = []
    films_dct = {}

    for line in lines_lst:
        lst.append(line.split('\t'))

    for film_data in lst:
        if int(film_data[2]) > num_v:
            lst_with_proper_votes_number.append(film_data)

    for flm in lst_with_proper_votes_number:
        films_dct[flm[0]] = flm[1], flm[2]
    return films_dct

# print(votes_dict(read_file('brief_data.tsv'), 10000))

def films_id(n, dict_votes):
    """
    (int, dict) -> (set)
    Return of n films id with the highest rating

    {'tt0000439': ('7.3', '13529'), 'tt0000417': ('8.2', '34313')}
    """
    proper_rating = set()
    for item in dict_votes.items():
        if float(item[1][0]) > n:
            proper_rating.add(item[0])

    return proper_rating

# print(films_id(7, votes_dict(read_file('brief_data.tsv'), 1000)))

def write_films_id(set_films_id):
    """
    (set) -> None
    Write films id to file
    """
    with open('suitable_films', 'w', encoding='utf-8') as result:
        for id in list(set_films_id):
            result.write(f'{id}\n')

# write_films_id(films_id(7, votes_dict(read_file('brief_data.tsv'), 1000)))


def find_films_id(n = 10, num_v = 10**6):
    return write_films_id(films_id(n, votes_dict(read_file('brief_data.tsv'), num_v)))


find_films_id(5, 3000)