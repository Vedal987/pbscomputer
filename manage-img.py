import os
path = 'img/'
files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, 'tmp'.join([str(index), '.jpg'])))

files = os.listdir(path)

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
    print('<div class="carousel-item">\n    <div class="fill" style="background-image:url(\'img/' + str(index) + '.jpg\');"></div>\n</div>\n')