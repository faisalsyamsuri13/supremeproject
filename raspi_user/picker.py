import glob
import os
def newest():
    files = glob.glob('C:/Users/ASUS/xampp/htdocs/supremeproject/raspi_user/qf/*.png')
    exist = max(files, key = os.path.getctime).split("\\")
    return exist[1]
