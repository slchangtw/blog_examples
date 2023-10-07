class DuplicateRemover:
    def remove_duplicates_from_list(self, input_list: list[int]) -> list[int]:
        return list(dict.fromkeys(input_list))

    def remove_duplicates_from_tuple(self, input_tuple: tuple[int]) -> tuple[int]:
        return tuple(dict.fromkeys(input_tuple))
