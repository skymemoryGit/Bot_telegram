import subprocess


def convert():
    shell_cmd = "ffmpeg -i {0} -f mp3 {1}.mp3".format("audio_file.oga","audio_file")
    p = subprocess.Popen(shell_cmd, shell=True,stdout=subprocess.PIPE)
    
    
    


convert()