import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

URL= 'https://api.github.com/search/repositories?q=language:java&sort=star&page=3'
r = requests.get(URL)
"""获取状态"""
print("Status code",r.status_code)
"""转为json"""
repo_dicts = r.json()
"""总项目量"""
print("total_count",repo_dicts['total_count'])
# 研究有关仓库的信息
repo_dict = repo_dicts['items']
# 获取names starts
names,repo_stars = [],[]
for repo in repo_dict:
    names.append(repo['name'])
    plot_dict = {'value':repo['stargazers_count'],
                 'label':str(repo['description']),
                 'xlink':repo['html_url']}
    repo_stars.append(plot_dict)

my_style = LS('#58dada', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
# 设置图表标题
my_config.title_font_size = 24
# 设置图表副标题
my_config.label_font_size = 14
# 设置图表主标题
my_config.major_label_font_size = 18
# 设置x轴上名称最多15字+省略号
my_config.truncate_label = 15
# 隐藏图表中的水平线
my_config.show_y_guides = False

my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = "Most-Started Python Projects on GitHub"
chart.x_labels = names
chart.add('',repo_stars)
chart.render_to_file('github_starts_1.svg')
