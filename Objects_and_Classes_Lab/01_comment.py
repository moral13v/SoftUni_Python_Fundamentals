class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
comment2 = Comment("user2", "I hate books", 3)
comment3 = Comment("user3", "I can live with it", 18)

print(comment.username)
print(comment.content)
print(comment.likes)

print(comment2.username)
print(comment2.content)
print(comment2.likes)

print(comment3.username)
print(comment3.content)
print(comment3.likes)
