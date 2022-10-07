import os
from datetime import datetime as dt
env_file = os.getenv('GITHUB_ENV')
path  = os.getcwd()
print(path)

version_path  = f'{os.path.dirname(path)}/github_actions_test/data-service/version.txt'
print(version_path)
x=dt.now()
with open(version_path, "r") as f:
  line  = f.readline()

with open(env_file, "a") as myfile:
  myfile.write(f"my_date={x}\n")
  myfile.write(f"my_var={line}")