import os
import wget
import time
os.system('IF EXIST .\\tmp (rmdir /s /q tmp)')
os.system('IF NOT EXIST .\\tmp (mkdir tmp)')
os.system('IF NOT EXIST .\\out (mkdir out)')
MBRSTMLink = 'http://puccistuff.weebly.com/uploads/4/6/0/6/46068159/multi_brstm_builder_with_gui_tool.rar'
FFMpegLink = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z'
print "Downloading the necessary files. Please wait this could take a while..."
print " "
wget.download(MBRSTMLink, '.\\tmp')
wget.download(FFMpegLink, '.\\tmp\\ffmpeg.7z')
os.system('"C:\\Program Files\\WinRAR\\unrar.exe" x .\\tmp\\multi_brstm_builder_with_gui_tool.rar .\\tmp')
os.system('"C:\\Program Files\\WinRAR\\unrar.exe" x .\\tmp\\ffmpeg.7z .\\tmp')
raw_input("Multi BRSTM Builder and ffmpeg have been downloaded, MBRSTM should uncompress himself (ffmpeg doesn't, when you uncompress ffmpeg please change the folder name to ffmpeg) if it doesn't, please uncompress it yourself it's in the tmp folder. Press ENTER to continue: ")
print " "
#The code creates and/or deletes the necessary folder, 
#downloads MultiBrstm Builder, ffmpeg and then uncompresses them

direc = os.getcwd() 
audioft = str(raw_input('Which audio file extension will you be using? (i.e. .mp3): '))
print " "
file_dict = {} 
audio_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == audioft]
for f in audio_files:
    with open(os.path.join(direc,f)) as file_object:
        file_dict[f] = file_object.read()
#The code creates the necessary dictionaries
#to know which file to interact with later

n=0
for i in file_dict:
 n=n+1
 cn=0
 cnc=0
 nc=0
 ncc=0
 wn=0
 wn2=0
 txt=""
 txtf=""
 AudioChannels=int(raw_input('How many channels for the song ' + str(i) + '?: '))
 acc=AudioChannels
 acc2=AudioChannels
 acc3=AudioChannels
 print " "
 Decibels=int(raw_input('How many decibels do you want to increase?: '))
 print " "
 Samples=int(raw_input('How many samples does that song have?: '))
 print " "
 while AudioChannels>0:
   nc=nc+1
   AudioChannels=AudioChannels-1
   cn=cn+1
   os.system('.\\tmp\\ffmpeg\\bin\\ffmpeg.exe -i "' + str(i) + '" -acodec pcm_s16le -filter:a "volume=' + str(Decibels) + 'dB" -ac 1 ' + '".\\tmp\\c' + str(cn) + str(i.replace(audioft, '.wav')) + '"')
   os.system('.\\tmp\\ffmpeg\\bin\\ffmpeg.exe -i ".\\tmp\\c' + str(cn) + str(i.replace(audioft, '.wav')) + '" -acodec pcm_s16le -filter:a "atempo=1.35" ".\\tmp\\fastc' + str(cn) + str(i.replace(audioft, '.wav')) +'"')
 FastSamples=str(raw_input('How many samples does fastcx' + str(i.replace(audioft, '.wav') + " (located at the tmp folder) have?: ")))
 while acc>0:
  acc=acc-1
  cnc=cnc+1
  ncc=ncc+1
  f= open('./tmp/DSPADPCM.bat', 'w+') 
  f.write('"' + str(direc)+ '\\tmp\\Multi BRSTM Builder with GUI Tool\\DSPADPCM.exe" -e ".\\tmp\\c' + str(ncc) + str(i.replace(audioft, '.wav')) + '" "tmp\\c' + str(ncc) + str(i.replace(audioft, '.dsp')) + '" -l0-' + str(Samples))
  f.write('' + '\n')
  f.write('"' + str(direc)+ '\\tmp\\Multi BRSTM Builder with GUI Tool\\DSPADPCM.exe" -e ".\\tmp\\fastc' + str(ncc) + str(i.replace(audioft, '.wav')) + '" "tmp\\fastc' + str(ncc) + str(i.replace(audioft, '.dsp')) + '" -l0-' + str(FastSamples))
  f.close() 
  os.system('.\\tmp\\DSPADPCM.bat')
 while acc2>0:
  acc2=acc2-1
  wn=wn+1
  txt=txt + '".\\c' + str(wn) + str(i.replace(audioft, '.dsp')) + '" '
 f= open('./tmp/wdrev.bat', 'w+')
 f.write('cd .\\tmp') 
 f.write('' + '\n')
 f.write('"' + str(direc)+ '\\tmp\\Multi BRSTM Builder with GUI Tool\\wdrev.exe" --build "' + str(direc) + "\\out\\" +  str(i.replace(audioft, '.brstm')) + '" ' + str(txt))
 f.write('' + '\n')
 f.write('"' + str(direc)+ '\\tmp\\Multi BRSTM Builder with GUI Tool\\wdrev.exe" --build "' + str(direc) + "\\out\\fast" +  str(i.replace(audioft, '.brstm')) + '" ' + str(txt.replace('c', 'fastc')))
 f.write('' + '\n')
 f.write('exit')
 f.close()
 os.system('start cmd /k ".\\tmp\\wdrev.bat"')
print "Finished!. The files are in the out folder. You can delete the tmp folder and txt filex if you want to now."
time.sleep(10)
