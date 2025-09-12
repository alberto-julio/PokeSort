import random

def swap(pokemon: list, i: int, j: int):
    pokemon[i], pokemon[j] = pokemon[j], pokemon[i]

def partition(pokemon: list, left: int, right: int):
    pivot_index = random.randint(left, right)
    pivot_value = pokemon[pivot_index]
    
    # Move pivot to end temporarily
    swap(pokemon, pivot_index, right)

    i = left - 1
    for j in range(left, right):
        if pokemon[j] < pivot_value:
            i += 1
            swap(pokemon, i, j)

    # Place pivot in correct position
    swap(pokemon, i + 1, right)
    return i + 1

def quick_sort(pokemon: list):
    def _quick_sort(pokemon, left, right):
        if left < right:
            part = partition(pokemon, left, right)
            _quick_sort(pokemon, left, part - 1)
            _quick_sort(pokemon, part + 1, right)

    _quick_sort(pokemon, 0, len(pokemon) - 1)
    return pokemon
