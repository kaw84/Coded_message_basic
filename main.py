alphabet1 = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = 'friends'
message1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


def decoder(message, alphabet, offset):
    # creating separate lists
    new_word = []

    for i in message:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                new_word.append(alphabet[(j + offset) % len(alphabet)])
                break
            elif not i in alphabet:
                new_word.append(i)
                break
    return new_word


def encoder(message, alphabet, offset):
    new_word = []
    for i in message:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                new_word.append(alphabet[(j - offset) % len(alphabet)])
                break
            elif not i in alphabet:
                new_word.append(i)
                break
    return new_word


message_2 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!."
print(decoder(message_2, alphabet2, 7))



