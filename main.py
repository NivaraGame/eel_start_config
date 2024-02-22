import eel
import os
import back.main_back as main_back

dir_path = f'{os.path.dirname(os.path.realpath(__file__))}'
eel.init(dir_path)


@eel.expose
def example():
    print('back meow')
    main_back.meow()
    return 'return back meow'


html_path = os.path.dirname(os.path.realpath(__file__)).split('/')
html_path.remove(html_path[-1])
html_path = '/'.join(html_path)


eel.start(f'{html_path}\\front_eel\\home.html', size=(500, 300))
