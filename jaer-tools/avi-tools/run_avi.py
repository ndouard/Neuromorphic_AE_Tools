from os import listdir, walk, system
from os.path import isfile, join
import logging
import time
import os

# print to the standard output and append to a log file
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('run_avi_output.log', 'a'))
print('*** Starting reconstrution on ' + time.ctime() + ' ***\n')

def register_pause_before_closing_console():
    import atexit
    if os.name == 'nt':
        from win32api import GetConsoleTitle
        if not GetConsoleTitle().startswith(os.environ['COMSPEC']):
            atexit.register(lambda: os.system('pause'))

files_path = '/home/nicolas/Desktop/test'

folders = [x[0] for x in walk(files_path)]
print(folders)

# drop current dir
folders.pop(0)

for k in range(len(folders)):	
	only_files = [f for f in listdir(folders[k]) if isfile(join(folders[k], f))]
	for l in range(len(only_files)):
		curr_file = folders[k] + '/' + only_files[l]
		print('Current File: ' + curr_file)
		avi_file = curr_file.rsplit(".", 1)[0] + '.avi'
		print('AVI Output: ' + avi_file)
		command = 'bash ./dvs-slice-avi-writer.sh -dimx=64 -dimy=64 -grayscale=100 -quality=1.0 -normalize=true -rectify=true -numevents=100 ' + curr_file + ' ' + avi_file
		print(command, '\n')
		system(command)

if __name__ == '__main__':
	register_pause_before_closing_console()

