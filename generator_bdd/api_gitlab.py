import os
import gitlab
# from •create file import create_cucmber_file

class Gitlab:
    def __init__(self, URL_GITLAB, PRIVATE_TOKEN_GITLAB):
        self.URL_GITLAB = URL_GITLAB
        self.PRIVATE_TOKEN_GITLAB = PRIVATE_TOKEN_GITLAB

def create_cumber (**params):
    # Gitlab connect
    gl = gitlab.Gitlab(
        Gitlab.URL_GITLAB,
        private_token=Gitlab.PRIVATE_TOKEN_GITLAB,
        api_version=4,
        ssl_verify=False
    )
    # GROUP
    try:
        all_epic = params['all_epic']
    except KeyError:
        all_epic = True
    try:
        generator = params [ 'generator']
    except KeyError:
        generator = False
    group_id = params['group_id']
    group = gl.groups.get(group_id)
    # EPIC
    epi_iid = params ['epi_iid']
    epic = group.epics.get(epi_iid)
    print(epic)
    # Создаем файл .feature
    # create_cumber_file(
    #     # Заголовок еріс
    #     title=epic.title,
    #     # url еріс из которого формируется .feature
    #     web_url=epic.web_url,
    #     # дата обновления еріс для фиксации изменений
    #     updated_at=epic.updated_at,
    #     # автор еріс
    #     author=epic. author ['name' ],
    #     # все содержимое, сам еріс
    #     description=epic.description,
    #     # наименование файла .feature
    #     name_file=params ['name_file'],
    #     # номер по которому формируется feature (внутри еріс, например <scr-3-1>)
    #     scenario_number=params['scenario_number']:
    #     # работа с измнениеми только в блоке <scr-3-1><scr-3-1> или со всем еріс. (True/False)
    #     all_epic=all_epic,
    #     # для генерации теста из .feature в . ру
    #     generator=generator
    # )