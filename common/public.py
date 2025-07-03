
from pathlib import Path


class Public(object):
    def get_object_path(self):
        #
        current_file_path = Path(__file__).resolve()
        #
        project_root = current_file_path.parent.parent
        return str(project_root)






if __name__ == "__main__":
    res = Public().get_rsa_public_key1()
