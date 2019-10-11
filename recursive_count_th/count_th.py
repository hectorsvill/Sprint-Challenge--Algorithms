'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     i = 0
#     count = 0
#     while i < len(word) - 1:
#         if word[i] == 't' and word[i + 1] == 'h':
#             count += 1
#         i += 1

#     return count



def count_th(word):
    print(word)
    i = 0
    if len(word) <= 1:
        return len(word)/2
    else:
        if word[i] == 't' and word[i + 1] == "h":
            print(word[:2])
            return count_th(word[2:])
        else:
            return count_th(word[1:])





# def print_c(word):
#     print(word)
#     i = 0
#     if len(word) <= 1:
#         return i

#     else:
#         i += 1
#         return print_c(word[1:])




# if __name__ == "__main__":
    # print(count_th("abcthefthghith")) #3
# count_down(5)

print(count_th("hecthtorthfsd"))
