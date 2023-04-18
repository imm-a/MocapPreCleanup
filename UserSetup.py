import os
import shutil,stat

def my_super_copy(what, where):
    try:
        shutil.copy2(what, where+"NodesCleanup1.py")
        print('tried')
    except IOError:
        os.chmod(where, 777) #?? still can raise exception
        shutil.copy2(what, where+"testmobu.py")
        print('done')


what = 'NodesCleanup.py'
where = 'C:/Program Files/Autodesk/MotionBuilder 2023/bin/config/PythonStartup/'

my_super_copy(what,where)