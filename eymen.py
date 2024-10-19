meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MIDE": "Oyunlarda bulunan orta kısım",
            "SHORTS":"Kısa videolar",
            
            }

word = input("bana bi kısaltma söyle")


if word in meme_dict.keys():
    print(meme_dict[word],)
else:
    print("bu kelime bulunamadı")
