from faker import Faker

fake = Faker(locale='en-us')

j = 0
for i in range(1, 6):  # 5 comentários por post
    for post_comentario_id in range(1, 41):  # Assume 40 posts criados
        j += 1
        Faker.seed(j)
        nome_comentario = fake.first_name()
        email_comentario = nome_comentario[0].lower() + '@email.com'
        comentario = fake.text(max_nb_chars=300)
        data_comentario = str(fake.past_datetime(start_date='-3y'))
        # publicar todos comentários, caso queira que a publicação ou a não publicação seja aleatória, colocar o seguinte código -> from random import randint -> publicado_post = random.randint(0, 1)
        publicado_comentario = 1
        usuario_comentario_id = 1  # id do seu super usuário

        sql_comentario = (f"INSERT INTO blog_django.comentarios_comentario"
        f"(nome_comentario,email_comentario,comentario,data_comentario,"
        f"publicado_comentario,post_comentario_id,usuario_comentario_id)"
        f"VALUES ('{nome_comentario}','{email_comentario}','{comentario}',"
        f"'{data_comentario}',{publicado_comentario},{post_comentario_id},"
        f"{usuario_comentario_id});")

        print(sql_comentario)
        print()
