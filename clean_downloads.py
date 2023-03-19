"""
Write python code to go through files in Downloads folder, check their dates and
if they are older than 30 days, move them to folder called to_delete. Provide
code only. No comments. Make code adhere to pylint with a maximum line length of
100.
"""

import os
import shutil
from datetime import datetime, timedelta

downloads_folder = os.path.expanduser('~/Downloads')
to_delete_folder = os.path.expanduser('~/to_delete')

for f in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, f)
    if os.path.isfile(file_path):
        age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))
        if age > timedelta(days=30):
            shutil.move(file_path, to_delete_folder)
