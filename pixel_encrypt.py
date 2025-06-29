from PIL import Image

def encrypt_image(image_path, output_path, key=50):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print("Image encrypted and saved as", output_path)

def decrypt_image(image_path, output_path, key=50):
    encrypt_image(image_path, output_path, -key)

# encrypt_image("input.png", "encrypted.png")
# decrypt_image("encrypted.png", "decrypted.png")