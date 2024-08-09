import sys
import shutil
import os
import zipfile
import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py', 'config.py', '-id2gh.ico', '--onefile', '-ndota2-game-helper', '-p./gsi:./model:./common', '-w'
])

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
current_icon_path = os.path.join(current_dir, 'd2gh.ico')
current_resources_path = os.path.join(current_dir, 'resources')
current_cfg_path = os.path.join(current_dir, 'gamestate_integration_d2gh.cfg')

dist_dir = os.path.join(current_dir, 'dist')
build_dir = os.path.join(current_dir, 'build')
dist_icon_path = os.path.join(dist_dir, 'd2gh.ico')
dist_resources_path = os.path.join(dist_dir, 'resources')
dist_cfg_path = os.path.join(dist_dir, 'gamestate_integration_d2gh.cfg')

dist_zip_path = os.path.join(current_dir, 'dist.zip')

# copy to dist
shutil.copy2(current_icon_path, dist_icon_path)
shutil.copy2(current_cfg_path, dist_cfg_path)

if not os.path.exists(dist_resources_path):
    os.makedirs(dist_resources_path)

for item in os.listdir(current_resources_path):
    s = os.path.join(current_resources_path, item)
    d = os.path.join(dist_resources_path, item)
    shutil.copy2(s, d)

# zip
dist_zip = zipfile.ZipFile(dist_zip_path, "w", zipfile.ZIP_DEFLATED)
for path, dir_names, filenames in os.walk(dist_dir):
    fpath = path.replace(dist_dir, '')
    for filename in filenames:
        dist_zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
dist_zip.close()

# delete
shutil.rmtree(build_dir)
shutil.rmtree(dist_dir)

