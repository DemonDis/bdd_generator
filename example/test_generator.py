import sys
import os

from dotenv import load_dotenv, find_dotenv
sys.path.append('..')  # ".." означает один уровень вверх по дереву директорий
from generator_bdd.api_gitlab import Gitlab_api

load_dotenv(find_dotenv())
URL_GITLAB = os.environ.get('URL_GITLAB')
PRIVATE_TOKEN_GITLAB_WORK = os.environ.get('PRIVATE_TOKEN_GITLAB_WORK')

Gitlab_api.URL_GITLAB = URL_GITLAB
Gitlab_api.PRIVATE_TOKEN_GITLAB = PRIVATE_TOKEN_GITLAB_WORK

Gitlab_api.create_cumber(project_id='59216833', issue_iid=1)
# Gitlab_api.create_cumber()

# from src.utils.api
# _gitlab import create
# _cumber
# 2
# 3
# 4
# 5
# 7
# 9
# 10
# 11
# create cumber
# group_id = 137,
# epi_11d = 2,
# name file= test generator' scenario_number='scr-1-1,' generator=True
# # Пример для эксперементов generator