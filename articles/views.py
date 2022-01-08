from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse
# import library to create dummy data
from datetime import datetime
from faker import Faker
fake = Faker()

"""
article structure:
- id
- title
- slug
- category
- content
- thumbnail
- author
- profile
- created_at
- updated_at
"""

def random_article(idx):
    title = fake.paragraph(nb_sentences=1).replace('.', '')
    return {
        'id': idx + 1,
        'title': title,
        'slug': title.lower().replace(' ', '-'),
        'category': fake.word().title(),
        'content': ' '.join(fake.texts(nb_texts=10)),
        'thumbnail': fake.image_url(),
        'author': fake.name(),
        'profile': fake.job(),
        #'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'created_at': datetime.now().strftime('%B %d, %Y'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# add some functions
def get_all_articles(request):
    articles = [ random_article(idx) for idx in range(10)]
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
