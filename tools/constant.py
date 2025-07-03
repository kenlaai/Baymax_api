import os

from common.public import Public

# root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_dir = Public().get_object_path()
log_dir = os.path.join(root_dir, 'log')
# open_api_case_dir = os.path.join(root_dir, 'open_api_data')