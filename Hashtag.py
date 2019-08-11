def generate_hashtag(s):
    s_list = s.split();

    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()

    hashtag = "#" + ''.join(s_list)

    if len(hashtag) > 140 or s == "":
        return False

    return hashtag

print(generate_hashtag("hello world"))