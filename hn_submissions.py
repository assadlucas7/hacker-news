import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Endpoint da API para obter as principais histórias do Hacker News
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Convertendo a resposta em uma lista de IDs de histórias
submission_ids = r.json()

# Listas para armazenar nomes de histórias e seus detalhes
names, submission_dicts = [], []
for submission_id in submission_ids[:30]:
    # Endpoint da API para obter os detalhes de uma história específica
    url2 = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url2)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # Coletando o título da história
    names.append(response_dict['title'])

    # Criando um dicionário com detalhes da história
    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# Ordenando as histórias por número de comentários
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Configurando o estilo do gráfico
my_style = LS('#333366', base_style=LCS)

# Configurando propriedades do gráfico
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# Inicializando o gráfico de barras
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Discussões mais entusiasmadas do momento no Hacker News'
chart.x_labels = names

# Preparando os dados para o gráfico com links clicáveis
comment_data = []
for sd in submission_dicts:
    data_point = {
        'value': sd['comments'],  # Número de comentários
        'label': sd['title'], # titulo do artigo 
        'xlink': sd['link']  # Link da página de discussão
    }
    comment_data.append(data_point)

# Adicionando os dados ao gráfico
chart.add('', comment_data)

# Renderizando o gráfico para um arquivo SVG
chart.render_to_file('hn_submissions.svg')






