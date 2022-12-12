from faker import Faker
import requests
from io import BytesIO
from PIL import Image
import imagehash
import os

fake = Faker(locale='en-us')
j = 0
Faker.seed(j)

def compara_imagens_baixadas(directory, paths=[]):
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
        if compara_imagens_baixadas(f.name):
            os.remove(f.name)
            posta_imagem()
        return f.name[6:]
    return ''


for categoria_post_id in range(1, 5):  # Pressupõe 4 categorias
    for i in range(10):  # 10 posts para cada categoria
        j += 1
        titulo_post = fake.sentence(nb_words=8)
        data_post = str(fake.past_datetime(start_date='-3y'))
        conteudo_post = fake.text(max_nb_chars=800)
        excerto_post = f"{conteudo_post[:200]}"
        # usa o fake_image_url para baixar a imagem, verifica se ela é válida e escreve.
        imagem_post = posta_imagem()
        if not os.path.isfile(f"media/{imagem_post}"):
            imagem_post = ''
        # caso queira o modo aleatório colocar -> from random import randint -> publicado_post = random.randint(0, 1)
        publicado_post = 1
        autor_post_id = 1  # id do seu super usuário

        sql_post = (f"INSERT INTO blog_django.posts_post"
                    f"(titulo_post,data_post,conteudo_post,excerto_post,imagem_post,"
                    f"publicado_post,autor_post_id,categoria_post_id)"
                    f"VALUES ('{titulo_post}','{data_post}','{conteudo_post}',"
                    f"'{excerto_post}','{imagem_post}',{publicado_post},"
                    f"{autor_post_id},{categoria_post_id});")

        print(sql_post)
        print()
