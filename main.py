from pathlib import Path
from github import Github
from github import Auth

ALLOWED_CHARS_NO_HYPHEN = "abcdefghijklmnopqrstuvwxyz1234567890"
ALLOWED_CHARS = ALLOWED_CHARS_NO_HYPHEN + "-"

def get_usernames(length: int): #cant do aa-a
    usernames: list[list[str]] = []
    usernames.append(ALLOWED_CHARS_NO_HYPHEN)
    for i in range(0, length):
        usernames.append(next_usernames(usernames[i], i == (length - 2)))
    usernames.pop(0)
    usernames.pop(0)
    return usernames

def next_usernames(a: list[str], last_character: bool):
    result: list[str] = []
    for string1 in a:
        allowed_next_chars = ALLOWED_CHARS_NO_HYPHEN if string1[-1] == '-' or last_character else ALLOWED_CHARS
        for string2 in allowed_next_chars:
            result.append(string1 + string2)
    return result

def __main__():
    with open('secret.txt') as f:
        access_token = f.read()

    auth = Auth.Token(access_token)
    g = Github(auth=auth)

    print(g.get_rate_limit())

    Path("./out").mkdir(exist_ok=True)

    file_available = open('out/available.txt', 'w')
    file_taken = open('out/taken.txt', 'w')

    for list in get_usernames(3):
        for username in list:
            try:
                g.get_user(username)
                file_taken.write(username + '\n')
            except Exception:
                file_available.write(username + '\n')
            print(username + ' checked')

    file_available.close()
    file_taken.close()
    g.close()

__main__()
