from typing import Dict, List, TypedDict


def count_words_in_str(string: str) -> int:
    return len(string.split())

def count_char_occur(string: str) -> Dict:
    res_dict = {}
    for char in string:
        lower_char = char.lower()
        if lower_char not in res_dict:
            res_dict[lower_char] = 0
        res_dict[lower_char] += 1
    return res_dict

Char_Dict = TypedDict('Char_Dict', { "char": str, "num": int })
def form_sorted_list_of_dicts(dict: Dict[str, int]) -> List[Char_Dict]:
    res_list: List[Char_Dict] = []
    for key in dict:
        res_list.append({ "char": key, "num": dict[key] })
        res_list.sort(reverse=True, key=lambda x : x["num"])
    return res_list

def write_report(filepath: str, word_count: int, dict_list: List[Char_Dict]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in dict_list:
        if not dict['char'].isalpha():
            continue
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

