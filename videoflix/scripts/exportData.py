# functionality to automatically export model data (an alternative is to export model data is possible via admin interface of the app)
# this python script should regularly be called via shell script export-data.sh to automate model backups


# import sys 
from content.admin import MovieResource
# print(sys.path)

def run():
    print('Test')