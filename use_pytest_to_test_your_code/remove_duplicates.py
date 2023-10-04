def remove_duplicates(input_list: list[int]) -> list[int]:
    return list(dict.fromkeys(input_list))
