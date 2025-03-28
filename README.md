# decaf_latte
# GRIND 75 Problems and their nuts and bolts

This repository contains my solutions to the GRIND 75 problems. The aim of this repository is to reflect my self-improvement journey in coding by documenting my progress in problem-solving skills. [Grind 75](https://www.techinterviewhandbook.org/grind75)

## Problem List

| # | Title | Solution | Brute Force Complexity | Optimized Complexity|
| --- | --- | --- | --- | --- |
| 1 | Two Sum | [Solution](./GRIND_75/leetcode_1_two_sum.py) | T: _O(n²)_ <br> S: _O(1)_ | T: _O(n)_ <br> S: _O(n)_ |
| 20 | Valid Parentheses | [Solution](./GRIND_75/leetcode_20_valid_parentheses.py) | | T: _O(len(s)_ <br> S: _O(len(s)_ |
| 21 | Merge Two Sorted Lists | [Solution](./GRIND_75/leetcode_21_merge_two_sorted_lists.py) | | m = len(list1), n = len(list2) <br> T: _O(m+n)_ <br> S: _O(1)_ (additional nodes just point to list1 or list2)|
| 121 | Best Time to Buy and Sell Stock | [Solution](./GRIND_75/leetcode_121_best_time_to_buy_and_sell_stock.py) | T: _O(n²)_ <br> S: _O(1)_ | T: _O(n)_ <br> S: _O(1)_ |
| 125 | Valid Palindrome | [Solution](./GRIND_75/leetcode_125_valid_palindrome.py) | T: _O(n)_ <br> S: _O(n)_ | T: _O(n)_ <br> S: _O(1)_ |
| 226 | Invert Binary Tree | [Solution](./GRIND_75/leetcode_226_invert_binary_tree.py) | | DFS with Recursion <br> T: _O(n)_ <br> S: _O(n)_ <br><br> DFS with Stack <br> T: _O(n)_ S: _O(n)_ <br><br> BFS <br> T: _O(n)_ <br> S: _O(n)_ |
| 242 | Valid Anagram | [Solution](./GRIND_75/leetcode_242_valid_anagram.py) | T: _O(nlogn)_ <br> S: _O(1) or _O(n)_ <br> (Depending on Sorting Algorithm) | For ASCII (Solution 3), frequence of 26 letters are calculated <br> T: _O(n)_ S: _O(1)_ <br> For Unicode (Solution 3) <br> T: _O(n)_ <br> S: _O(U)_, U= # of unique UNICODE characters |
| 704 | Binary Search | [Solution](./GRIND_75/leetcode_704_binary_search.py) | T: _O(logN)_ <br> S: _O(logN)_ (recursion stack) | T: _O(logN)_ <br> S: _O(1)_ |
| 733 | Flood Fill | [Solution](./GRIND_75/leetcode_733_flood_fill.py) | | m = # of rows, n = # of columns <br> T: _O(mxn)_ <br> S: _O(mxn)_ |
| 235 | Lowest Common Ancestor of a Binary Search Tree | [Solution](./GRIND_75/leetcode_235_lowest_common_ancestor_of_a_BST.py) | height, h = logN <br> T: _O(h)_ <br> S: _O(h)_ | T: _O(h)_ <br> S: _O(1)_ |
| 110 | Balanced Binary Tree | [Solution](./GRIND_75/leetcode_110_balanced_binary_tree.py) | | T: _O(n)_ <br> S: _O(n)_ |
| 141 | Linked List Cycle | [Solution](./GRIND_75/leetcode_141_linked_list_cycle.py) | T: _O(n)_ <br> S: _O(n)_ | T: _O(n)_ <br> S: _O(1)_ |
| 232 | Implement Queue using Stacks | [Solution](./GRIND_75/leetcode_232_implement_queue_using_stacks.py) | | T: <br> push: _O(1)_ <br> pop: Amortized _O(1)_ <br> peek: Amortized _O(1)_ <br> empty: _O(1)_ <br> S: _O(n)_ |
| 278 | First Bad Version | [Solution](./GRIND_75/leetcode_278_first_bad_version.py) | | T: _O(logN)_ <br> S: _O(1)_ |
| 383 | Ransom Note | [Solution](./GRIND_75/leetcode_383_ransom_note.py) | | m = len(ransomNote) <br> n = len(magazine) <br> T: _O(max(m,n))_ <br> S: _O(1)_ |
| 70 | Climbing Stairs | [Solution](./GRIND_75/leetcode_70_climbing_stairs.py) | | T: _O(n)_ <br> S: _O(1)_ |
| 409 | Longest Palindrome | [Solution](./GRIND_75/leetcode_409_longest_palindrome.py) | | T: _O(n)_ <br> S: _O(1)_ |
| 206 | Reverse Linked List | [Solution](./GRIND_75/leetcode_206_reverse_linked_list.py) | T: _O(n)_ <br> S: _O(n)_ | T: _O(n)_ <br> S: _O(1)_ |
| 169 | Majority Element | [Solution](./GRIND_75/leetcode_169_majority_element.py) | T: _O(n)_ <br> S: _O(n)_ | Voting Algorithm Utilized <br> T: _O(n)_ <br> S: _O(1)_ |
| 67 | Add Binary | [Solution](./GRIND_75/leetcode_67_add_binary.py) | | m = len(a), n = len(b) <br> T: _O(max(m,n))_ <br> S: _O(max(m,n))_ |
| 543 | Diameter of Binary Tree | [Solution](./GRIND_75/leetcode_543_diameter_of_a_binary_tree.py) | | T: _O(n)_ <br> S: _O(n)_ |
| 876 | Middle of the Linked List | [Solution](./GRIND_75/leetcode_876_middle_of_the_linked_list.py) | | T: _O(n)_ <br> S: _O(1)_ |
| 104 | Maximum Depth of Binary Tree | [Solution](./GRIND_75/leetcode_104_maximum_depth_of_binary_tree.py) | | T: _O(n)_ <br> S: _O(n)_ |
| 217 | Contains Duplicate | [Solution](./GRIND_75/leetcode_217_contains_duplicate.py) | With Optimized Sorting Algorithm <br> T: _O(nlogn)_ <br> S: _O(1) <br> | T: _O(n)_ <br> S: _O(n)_ |
| 252 (from neetcode)| Meeting Rooms | [Solution](./GRIND_75/leetcode_252_meeting_rooms.py) | | T: _O(nlogn)_ <br> S: _O(1)_ <br> with best sorting algo |
| 13 | Roman to Integer | [Solution](./GRIND_75/leetcode_13_roman_to_integer.py) | | T: _O(n)_ <br> S: _O(1)_ | 
| 844 | Backspace String Compare | [Solution](./GRIND_75/leetcode_844_backspace_string_compare.py) | T: _O(n)_ <br> S: _O(n)_ | # TBD |
| 53 | Maximum Subarray | [Solution](./GRIND_75/leetcode_53_maximum_subarray.py)| T: _O(n²)_ <br> S: _O(1)_ | T: _O(n)_ <br> S: _O(1)_ |
| 57 | Insert Interval | [Solution](./GRIND_75/leetcode_57_insert_interval.py) | | T: _O(n)_ <br> S: _O(n)_ |
| 542 | 01 Matrix | [Solution](./GRIND_75/leetcode_542_01_matrix.py) | | T: _O(mxn)_ <br> S: _O(mxn)_ <br> queue could hold upto _mxn_ entries. |
| 973 | K Closest Points to Origin | [Solution](./GRIND_75/leetcode_973_k_closest_points_to_origin.py) | T: _O(nlogn)_ <br> S: _O(1)_ | Min Heap Solution <br> T: _O(n + klogn)_ <br> S: _O(n)_ <br><br> Max Heap Solution <br> T: _O(nlogk)_ <br> S: _O(k)_ |
| 3 | Longest Substring Without Repeating Characters | [Solution](./GRIND_75/leetcode_3_longest_substring_without_repeating_characters.py) | T: _O(n*m)_ worst case _O(n²)_ <br> S: _O(m)_ <br> n = length of the string <br> m = length of the longest substring without repeating characters | T: _O(n)_ <br> S: _O(m)_ |
| 102 | Binary Tree Level Order Traversal | [Solution](./GRIND_75/leetcode_102_binary_tree_level_order_traversal.py) | | T: _O(n)_ <br> S: _O(n)_ |
| 15 | 3Sum | [Solution](./GRIND_75/leetcode_15_3sum.py) | | T: _O(n²)_ <br> The problem asks us to return all triplets. Hence, we are not using any auxiliary space to solve the problem. <br> S: _O(1)_ <br> |

## Analysis

### Time Complexity

The time complexity of each solution is analyzed and documented in the table above. The notation used for time complexity is Big O notation.

### Space Complexity

The space complexity of each solution is analyzed and documented in the table above. The notation used for space complexity is Big O notation.

# A tale of GIT
[Link](./Git_Documentation)

# A handy link of DocString (cmd + shift + 2)
[Docstring Extension and Details](https://github.com/NilsJPWerner/autoDocstring/tree/c9da64126fd9e667decd9d85b4e5b53c60372ea7?tab=readme-ov-file)

# Powerful Action Verbs for a Resume
Harvard action verbs are a curated list of powerful, descriptive verbs often recommended by career advisors and resume experts. These verbs are specifically chosen to help job seekers articulate their accomplishments and skills more effectively and vividly on their resumes and in interviews. By using these action verbs, individuals can present their experiences and achievements in a dynamic and impactful way, making it easier for employers to recognize their potential value and contributions to a role or organization. This approach aids in creating a more engaging and persuasive narrative about one's professional journey. You will find the action verbs in the following link.
[Action Verbs](https://www.alumni.hbs.edu/Documents/careers/ActionVerbsList.pdf)

# What to Sort and Not to Sort, That's the Question
[Link](./sorting)
## Contributing
Constructive criticism is welcome. I would appreciate your comments, feedback, and any other suggestions you may have.
