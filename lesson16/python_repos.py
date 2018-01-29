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
names,starts = [],[]
for repo in repo_dict:
    names.append(repo['name'])
    starts.append(repo['stargazers_count'])


# 可视化 -----------------------------------------------
# my_style = LS('#333366', base_style=LCS)
# # 让标签绕x 轴旋转45度（x_label_rotation=45 ）,并隐藏了图例（show_legend=False)
# chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
# chart.title = "Most-Started Python Projects on GitHub"
# chart.x_labels = names
# chart.add('GitHub most started',starts)
# chart.render_to_file('github_starts.svg')
# 可视化 -----------------------------------------------

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
chart.add('',starts)
chart.render_to_file('github_starts.svg')
