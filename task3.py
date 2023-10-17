pin = "1235"
chars = ["0","1","2","3","4","5","6","7","8","9"]
# pin_guse = []

# # for simb in pin:
# #     for si in chars:
# #         if si == simb:
# #             pin_guse.append(si)
# # print(pin_guse)

# print([sign for sign in chars if sign in pin])

for f_1 in chars:
    for f_2 in chars:
        for f_3 in chars:
            for f_4 in chars:
                if f_1+f_2+f_3+f_4 == pin:
                    print(f_1+f_2+f_3+f_4)
                    break
                    
