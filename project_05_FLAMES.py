
FLAMES_DICT = {'F': "Friends", 'L': "Lovers", 'A': "Affectionate",
               'M': "Marriage", 'E': "Enemies", 'S': "Sibling"}


def get_common_char(name):
    name_dict = {}
    for char in name:
        if char not in name_dict:
            name_dict[char] = 1
        else:
            name_dict[char] += 1
    return name_dict


def get_combined_dict(name1_dict, name2_dict):
    combined_dict = {}
    for value in name1_dict:
        if value in name2_dict:
            num_common = min(name1_dict[value], name2_dict[value])
            combined_dict[value] = num_common
    return combined_dict


def remove_common_chars(name, char_dict):
    new_name = ""
    seen_dict = {}

    for char in name:
        if char in char_dict and seen_dict.get(char, 0) < char_dict[char]:
            seen_dict[char] = seen_dict.get(char, 0) + 1
        else:
            new_name += char

    return new_name


def get_status_code(remaining_length):
    flames = "FLAMES"
    current_index = -1
    while len(flames) > 1:
        for _ in range(remaining_length):
            current_index += 1
            if current_index >= len(flames):
                current_index = 0
        flames = flames[:current_index] + flames[current_index + 1:]
        current_index -= 1
    return flames


def main():
    print("=================")
    print("FLAMES")
    print("=================\n")

    name1 = input("Enter Player One Name:\n>> ").lower()
    name2 = input("Enter Player Two Name:\n>> ").lower()

    name1_dict = get_common_char(name1)
    name2_dict = get_common_char(name2)

    combined_dict = get_combined_dict(name1_dict, name2_dict)

    new_name1 = remove_common_chars(name1, combined_dict)
    new_name2 = remove_common_chars(name2, combined_dict)

    remaining_length = len(new_name1) + len(new_name2)

    status_code = get_status_code(remaining_length)

    print(f"\nRelationship Status: {FLAMES_DICT[status_code]}")

    input("\nPress Enter to Exit\n")


if __name__ == "__main__":
    main()
