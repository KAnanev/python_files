def find_longest_length(string):
    longest = 0
    for start_index in range(len(string)):
        contains = set()
        for letter in string[start_index:]:
            if letter in contains:
                break
            contains.add(letter)
        longest = max(longest, len(contains))
    return longest

# def find_longest_length(string):
#     ptr, max_len = 0, 0
#     store = {}
#     for (i, ch) in enumerate(string):
#         if ch not in store:
#             store[ch] = i
#         else:
#             max_len = max(max_len, i - ptr)
#             ptr = store[ch] + 1
#     return max(max_len, len(string) - ptr)


assert find_longest_length('') == 0
assert find_longest_length('a') == 1
assert find_longest_length('jabjcdel') == 7
assert find_longest_length('abcddef') == 4
assert find_longest_length('abbccddeffg') == 3
assert find_longest_length('abcd') == 4
assert find_longest_length('1234561qweqwer') == 9



