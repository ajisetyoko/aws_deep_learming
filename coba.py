import subprocess
import os
import glob

name_list = ['tyler']
pointer = '../Documents/'

for name_ in name_list:
    video_list = [f for f in glob.glob(pointer+name_+"/*.mov")]
    for video in video_list:
        print(video)
        file_out_name = (video.split('/')[3]).split('.')[0]
        print(file_out_name)
        out_path =pointer + 'output/'+name_+'/'+file_out_name+'/'
        rc = subprocess.call('mkdir -p ' + out_path,shell=True)
        print('build',video,out_path)
        builder = './build/examples/openpose/openpose.bin --video '+video + ' --face --hand --display 0 --render_pose 0 --write_json '+out_path
        print(builder)
        rc = subprocess.call(builder,shell=True)
        print('#######################################################')
