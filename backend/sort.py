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

def insertion_sort(pokemon: list):

    for i in range(1, len(pokemon)):
        key = pokemon[i]
        j = i - 1

        while j >=0 and key < pokemon[j]:
            pokemon[j + 1] = pokemon[j]
            j -= 1
        pokemon[j + 1] = key
    
    return pokemon

def bubble_sort(pokemon: list):

    n = len(pokemon)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if pokemon[j] > pokemon[j + 1]:
                pokemon[j], pokemon[j + 1] = pokemon[j + 1], pokemon[j]
                swapped = True
        if (swapped == False):
            break
    return pokemon

def is_sorted(pokemon: list):
    n = len(pokemon)
    for i in range(0, n-1):
        if (pokemon[i] > pokemon[i+1]):
            return False
    return True

def shuffle(pokemon: list):
    n = len(pokemon)
    for i in range(0, n):
        r = random.randint(0, n-1)
        pokemon[i], pokemon[r] = pokemon[r], pokemon[i]

def bogo_sort(pokemon: list):
    n = len(pokemon)
    while (is_sorted(pokemon) == False):
        shuffle(pokemon)

    return pokemon

def merge_sort(pokemon: list):
    if len(pokemon) <= 1:
        return pokemon

    mid = len(pokemon) // 2
    left_half = merge_sort(pokemon[:mid])
    right_half = merge_sort(pokemon[mid:])

    sorted_list = []
    i = j = 0

    # Merge the two halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[j:])

    return sorted_list

def quick_sort(pokemon: list):
    def _quick_sort(pokemon, left, right):
        if left < right:
            part = partition(pokemon, left, right)
            _quick_sort(pokemon, left, part - 1)
            _quick_sort(pokemon, part + 1, right)

    _quick_sort(pokemon, 0, len(pokemon) - 1)
    return pokemon
