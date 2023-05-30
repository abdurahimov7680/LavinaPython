# 3.mahsulotlar degan ro'yxat yarating va kamida 10 ta turli
#  mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating
#   va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni
#    so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor"
#  aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# 4.Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 
# 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda 
# bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q 
# mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas
#  ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" 
#  degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." 
#  degan xabarni chiqaring.


# 4.Massala
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")



# 5.foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
#  Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
#  loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
#   Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
#    aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.


# foydalanuvchilar = ['abdulloh', 'sardor', 'karim', 'mister', 'dost']
# yangi = input("Istemolchi yangi login yarating: ")
# if yangi.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz istemolchi. Sizning loginiz {yangi}. ")



# 6.Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan
#  sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 



# son = int(input("Foyadalunuvchi butun son kiriting: "))
# for h in range(2,11):
#     if not (son%h):
#         print(f"{son} soni {h} ga qoldiqsiz bo'linadi")

