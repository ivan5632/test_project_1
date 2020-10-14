import os

path, dirs, files = next(os.walk("/media/sf_Projects/Machine Learning/train"))
print('\n', path, '\n', dirs, '\n', 'number of files: ', len(files))
