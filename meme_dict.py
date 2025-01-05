meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "bir şakaya karşılık cevap", 
    "SHEESH": "onaylamamak", 
    
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("kelime var")
    print(meme_dict[word])
else:
    print("ne yazıkki kelime yok")
