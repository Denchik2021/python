import os

MY_CONSTANT_ONE = 'my_project'
MY_CONSTANT_TWO = 'settings'
MY_CONSTANT_THREE = 'mainapp'
MY_CONSTANT_FOUR = 'adminapp'
MY_CONSTANT_FIVE = 'authapp'

dir_name = MY_CONSTANT_ONE
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

    os.chdir(MY_CONSTANT_ONE)

    if not os.path.exists(MY_CONSTANT_TWO):
        os.mkdir(MY_CONSTANT_TWO)
    if not os.path.exists(MY_CONSTANT_THREE):
        os.mkdir(MY_CONSTANT_THREE)
    if not os.path.exists(MY_CONSTANT_FOUR):
        os.mkdir(MY_CONSTANT_FOUR)
    if not os.path.exists(MY_CONSTANT_FIVE):
        os.mkdir(MY_CONSTANT_FIVE)
