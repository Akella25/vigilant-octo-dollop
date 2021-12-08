
def search_user(users: list, nickname: str):
    for user in users:
        if user.nickname == nickname:
            return user