def dict_to_class(_dict):
    """ Works only on a one nested level dict """

    class dotdict(dict):
        """dot.notation access to dictionary attributes"""

        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

    for i in _dict:
        if type(_dict[i]) == dict:
            _dict[i] = dotdict(_dict[i])

    return dotdict(_dict)


def round_to_nearest(num, nearest):
    return round(num / nearest) * nearest


def closest_dist_to_sc(sc, planets):

    min_dist = 1e6
    for planet in planets:
        dist = sc.calc_distance(planet)
        if dist < min_dist:
            min_dist = dist

    return min_dist


def vector_norm(array: list) -> float:
    return sum([i ** 2 for i in array]) ** 0.5


def add_two_vectors(v1: list, v2: list) -> list:
    return [i + j for i, j in zip(v1, v2)]


def subtract_two_vectors(v1: list, v2: list) -> list:
    return [i - j for i, j in zip(v1, v2)]


def euclidian_distance(v1, v2):
    return vector_norm(subtract_two_vectors(v1, v2))


def clip(val, min_val=None, max_val=None) -> float:

    new_val = val

    if min_val and val < min_val:
        new_val = min_val

    if max_val and val > max_val:
        new_val = max_val

    return new_val
