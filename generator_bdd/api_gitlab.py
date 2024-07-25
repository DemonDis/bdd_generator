# лНиТЬ
# Терминал Справка
# api_ gitlab.py x
# src › utils ›
# api_gitlab.py › ( create_cucmber
# import
# 05
# 3
# 5
# import gitlab
# from dotenv import load _dotenv, find_dotenv from
# •create file import create_cucmber_file
# 7
# load
# dotenv(find
# dotenv())
# PRIVATE
# TOKEN = 05. environ. get ("PRIVATE_TOKEN")
# URL_GIT = os. environ. get ("URL_GIT" )
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19 2021 22 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# gl = gitlab. Gitlab(
# URL_GIT,
# private
# token=PRIVATE_TOKEN,
# api_version=4, ssl_verify=False
# def create_cumber (**params) :
# # GROUP
# try:
# all epic = params['all_epic']
# except KeyError:
# all
# _epic = True
# 43
# 46
# 47
# 48
# 4950515253545586
# try:
# generator = params [ 'generator']
# except KeyError:
# generator = False
# group
# id = paramsI 'group_id']
# group = gl.groups.get (group_id)
# # EPIC
# epi
# iid = params ['epi
# iid']
# epic = group.epics.get (epi
# iid）
# # Создаем файл
# • feature
# create
# _cumber_file(
# # Заголовок еріс
# title=epic.title,
# # url еріс из которого формируется - feature
# web_url=epic.web_url,
# # дата обновления
# еріс для
# фиксации изменений
# updated
# _at=epic, updated
# Lat,
# # автор еріс
# author=epic. author ['name' ],
# # все содержимое,
# сам еріс
# description=epic.description,
# # наименование файла . feature
# name_file=params [' name_
# file'],
# * номер по которому формируется feature (внутри еріс, например <scr-3-1>)
# scenario_ number-params [' scenario_number']:
# # работа с измнениеми только в блоке <scr-3-1»<scr-3-1> или со всем еріс. (True/False)
# all epic=all_epic,
# # для генерации теста из .feature в . ру
# generator-generator