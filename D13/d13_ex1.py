posts = [
    {"Fotos": 5, "Likes": 24, "Comentários": 1},
    {"Likes": 15, "Comentários": 6, "Compartilhamentos": 3},
    {"Fotos": 11, "Likes": 45, "Comentários": 15, "Compartilhamentos": 10},
    {"Comentários": 14, "Compartilhamentos": 1},
    {"Fotos": 12, "Comentários": 3, "Compartilhamentos": 3},
    {"Fotos": 5, "Likes": 24, "Comentários": 5},
]

total_likes = 0

for post in posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        pass

print(f"Total de likes: {total_likes}")