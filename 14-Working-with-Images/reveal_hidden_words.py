from PIL import Image

matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

matrix.show()
mask.show()

matrix_size = matrix.size
mask_size = mask.size

print(matrix_size)
print(mask_size)

mask = mask.resize((matrix_size))
mask.putalpha(100)
#mask.show()

hidden_words = matrix.copy()
hidden_words.paste(mask, (0,0), mask)
hidden_words.show()