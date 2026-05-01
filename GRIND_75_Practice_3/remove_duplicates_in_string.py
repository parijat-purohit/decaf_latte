def identify_adjacent(s: str, k: int) -> str:
    st = []

    for c in s:
        st.append(c)
        if len(st) >= k:
            if len(set(st[-k:])) == 1:
                st = st[:-k]

    return "".join(st)


# debug your code below
print(identify_adjacent("daaabbbaa", 3))
print(identify_adjacent("aaabbbacd", 3))
print(identify_adjacent("pbbcggttciiippooaais", 2))
print(identify_adjacent("abcdef", 2))
