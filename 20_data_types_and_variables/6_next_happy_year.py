number = int(input())

str_num = str(number)

while True:
    number += 1
    str_number = str(number)

    if len(set(str_number)) == len(str_number):
        print(number)
        break

# # This solution does not work 🫣
#
# def happy_year(a, b, c, d):
#     if a != b and a != c and a != d and b != c and b != d and c != d:
#         return True
#     else:
#         return False
#
#
# number = int(input())
# number += 1
#
# str_num = str(number)
#
# q = range(0, 11)
#
# o = int(str_num[3])
# p = int(str_num[2])
# i = int(str_num[1])
# u = int(str_num[0])
#
# is_year = False
#
# for r in q:
#     for h in q:
#         for j in q:
#             for k in q:
#                 if happy_year(u, i, p, o):
#                     print(f'{int(u)}{int(i)}{int(p)}{int(o)}')
#                     is_year = True
#                     break
#
#                 o += 1
#                 if o == 10:
#                     o = 0
#                     break
#             if is_year:
#                 break
#             p += 1
#             o = 0
#             if p == 10:
#                 p = 0
#                 break
#
#         if is_year:
#             break
#         i += 1
#         p = 0
#         if i == 10:
#             i = 0
#             break
#
#     if is_year:
#         break
#     u += 1
#     i = 0
#     if u == 10:
#         u = 0
#         break
