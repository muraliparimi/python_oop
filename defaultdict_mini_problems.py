
# Count Page Visits per User
# Input

logs = [
    ("user1", "home"),
    ("user1", "home"),
    ("user1", "search"),
    ("user2", "home"),
    ("user2", "product"),
    ("user1", "home")
]

# output

expected = {
    "user1": {"home": 3, "search": 1},
    "user2": {"home": 1, "product": 1}
}

from collections import defaultdict

actual_page_visits_per_user = defaultdict(lambda: defaultdict(int)) 

for item in logs:
    actual_page_visits_per_user[item[0]][item[1]] +=1

print(dict(actual_page_visits_per_user))


# Group Product Reviews by Category and Rating Count

reviews = [
    ("books", 5, "Atomic Habits"),
    ("books", 4, "Deep Work"),
    ("books", 5, "The Power of Habit"),
    ("electronics", 5, "AirPods"),
    ("electronics", 4, "Kindle"),
]

expected_product_reviews = {
    "books": {
        5: ["Atomic Habits", "The Power of Habit"],
        4: ["Deep Work"]
    },
    "electronics": {
        5: ["AirPods"],
        4: ["Kindle"]
    }
}

actual_product_reviews = defaultdict(lambda: defaultdict(list))

for review in reviews:
    actual_product_reviews[review[0]][review[1]].append(review[2])

print(dict(actual_product_reviews))


# Track Word Frequencies Per Paragraph

entries = [
    (1, "data"), (1, "is"), (1, "powerful"),
    (1, "data"), (2, "python"), (2, "is"),
    (2, "powerful"), (2, "data")
]

expected_word_Freq_per_paragraph = {
    1: {"data": 2, "is": 1, "powerful": 1},
    2: {"python": 1, "is": 1, "powerful": 1, "data": 1}
}

actual_word_freq_per_paragraph = defaultdict(lambda: defaultdict(int))

for item in entries:
    actual_word_freq_per_paragraph[item[0]][item[1]] +=1

new_actual_word_freq_per_paragraph = {}
for key, value in actual_word_freq_per_paragraph.items():
    new_actual_word_freq_per_paragraph[key] = dict(value)
print(new_actual_word_freq_per_paragraph)

# sort by the frequencies
for cat in new_actual_word_freq_per_paragraph:
    for para in new_actual_word_freq_per_paragraph[cat]:
        new_actual_word_freq_per_paragraph[cat][para].sort()