# def length_of_longest_substring(s: str) -> int:
#     """
#     This function returns the length of the longest substring without repeating characters.

#     Args:
#         s (str): The input string.

#     Returns:
#         int: The length of the longest substring without repeating characters.
#     """
#     char_set = set()
#     left = 0
#     max_length = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)

#     return max_length

# # Example usage:
# print(length_of_longest_substring("abcabcbb"))  # Output: 3
# print(length_of_longest_substring("bbbbb"))  # Output: 1
# print(length_of_longest_substring("pwwkew"))  # Output: 3

srt='pwwkew'
sub_str=set()
max_lenth=0

for x in range(len(srt)):
    count=0
    while srt[x] not in sub_str:
        sub_str=sub_str.add(srt[x])
        count +=1
