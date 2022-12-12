from faker import Faker
import requests
from io import BytesIO
from PIL import Image
import imagehash
import os

fake = Faker(locale='en-us')


def compara_imagens(directory, paths = []):
    paths.append(directory)

    for path in paths:
        hash1 = imagehash.average_hash(Image.open(f"{directory}"))
        hash2 = imagehash.average_hash(Image.open(f"{path}"))
        diff = hash1 - hash2
        if diff == 0 and directory != path:
            paths.remove(directory)
            return True
    return False


def posta_imagem():
    imagem_url = fake.image_url(height=250, width=250)
    response = requests.get(imagem_url)
    img = Image.open(BytesIO(response.content))
    clrs = img.getcolors()
    if clrs is None:
        with open(f"media/post_img/{j}.png", "wb") as f:
            f.write(response.content)
        print(f.name)
        if compara_imagens(f.name):
            os.remove(f.name)
            posta_imagem()
        return f.name[6:]
    return ''


j = 0
for categoria_post_id in range(1, 5):  # Pressupõe 4 categorias
    for i in range(10):  # 10 posts para cada categoria
        j += 1
        Faker.seed(j)
        imagem_post = posta_imagem()
