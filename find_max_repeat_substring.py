from collections import defaultdict


def find_all_occurences(s, sub, start=0):
    indices = []
    while start < len(s):
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += 1
    return indices


def find_most_common_substring(s: str, length: int) -> str:
    # TODO: implement the function
    if length > len(s):
        return ""
    elif length == len(s):
        return s
    else:
        subs = defaultdict(int)
        window = s[:length]
        subs[window] += 1
        subs[window] += len(find_all_occurences(s[length:], window))
        i = 1
        while i < len(s) - length + 1:
            end_idx = length + i
            window = s[i: end_idx]
            subs[window] += 1
            subs[window] += len(find_all_occurences(s[end_idx:], window))
            i += 1
        new_subs = defaultdict(list)
        for item, value in subs.items():
            new_subs[value].append(item)
        ls = list(new_subs.items())
        ls.sort(key=lambda x: x[0], reverse=True)
        #print(ls)
        return sorted(ls[0][1])[0]