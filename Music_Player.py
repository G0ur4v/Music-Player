   #Music Player
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import pygame
from pygame import *
import os
import datetime #3 
from mutagen.mp3 import MP3 #3
from mutagen import File
from tkinter import filedialog

def directory():
         window.destroy()
         
         file=filedialog.askdirectory(title="Select a directory/folder",)
         os.chdir(file)
         songtracks = os.listdir()
         for track in songtracks:
              playlist.insert(END,track)

def files():
           window.destroy()
           file=filedialog.askopenfilename(title="Select a music file",)#filetypes=(("Audio Files", ".wav .ogg"),   ("All Files", "*.*")))
           print(file)
           playlist.insert(END,file)
                     

def popup():
             global window
             window=Toplevel(root)
             window.title("Open folder/file ")
             window.geometry("180x80+300+300")
             window.minsize(180,80)
             window.maxsize(180,80)
             window.configure(bg="#F4C724")
             label=tk.Label(window,text="SELECT",bd=5,image=lfphoto,height=90,width=180)
             label.pack(fil="both",expand="yes")
             folder=tk.Button(label,text="Folder",width=10,
                  command=directory,bg="#F5BCBA")
             folder.pack(side=LEFT,padx=5,)
             file=tk.Button(label,text="File",width=10,
                  command=files,bg="#F5BCBA")
             file.pack(side=RIGHT,padx=5,)
             
        
##        
##        

def play():
     global songlength
        #song_image.configure(text="Playing")
     if  not playlist.get(0):
            #print('Null Found')
            popup()
     else:
      global song
      
      if(mixer.music.get_pos()>0 and song==MP3(playlist.get(ACTIVE))):
          pygame.mixer.music.unpause()
          play.grid_forget()
          pause.grid(row=0,column=1,padx=5)
      else:
         
        song=MP3(playlist.get(ACTIVE))
        songlength=int(song.info.length)
        #print(songlength)
        pgbar['maximum']=songlength
        endtime.configure(text="{}".format(str(datetime.timedelta(seconds=songlength))))
        
        pygame.mixer.music.load(playlist.get(ACTIVE))
        pygame.mixer.music.play()
           

        def progressbarposition():
                realtimeposition=mixer.music.get_pos()/1000
                #print('Realtimeposition :',realtimeposition*1000)
                pgbar['value']=realtimeposition
                pgbar.after(1,progressbarposition)
                starttime.configure(text="{}".format(str(datetime.timedelta(seconds=realtimeposition))))
        progressbarposition()
        play.grid_forget()
        pause.grid(row=0,column=1,padx=5)

       
      

               

def pause():
    pygame.mixer.music.pause()
    pause.grid_forget()
    play.grid(row=0,column=1,padx=5)
    

def stop():
    pygame.mixer.music.stop()

    pause.grid_forget()
    play.grid(row=0,column=1,padx=5)


#def resume():
#    pygame.mixer.music.unpause()

def volume(value):
       #print(value)
       #vol=mixer.music.get_volume()
       mixer.music.set_volume(int(value)/100)
def mute():
    mixer.music.set_volume(0)
    mute.grid_forget()
    unmute.grid(row=0,column=7,padx=5)
    

    
def unmute():
    value=scale.get()
    print(value)
    mixer.music.set_volume(int(value)/100)
    mute.grid(row=0,column=7,padx=5)
    unmute.grid_forget()


def backward():
    pass
       
    
    
def forward():
    pass

def previous():
    
    selection =(playlist.curselection())
    active=selection[0]-1
    if active>=0:
      playlist.activate(active)
      #playlist.select_anchor(active)
      play.invoke()
def nexxt():
    #print(playlist.get(ACTIVE))
    selection =(playlist.curselection())
    active=selection[0]+1
    playlist.activate(active)
    #playlist.selection_clear(active)
    #playlist.select_anchor(active)
    play.invoke()
    

pygame.init()
pygame.mixer.init()


root=tk.Tk()
root.geometry("630x600")
root.maxsize(630,600) #1
root.minsize(400,400) #2
root.title("Musicana")
root.iconbitmap(".\\resources\\app_icon.ico")
lfphoto=tk.PhotoImage(file=".\\resources\\jpeg.png")
laf=tk.LabelFrame(root,#text="Enter Nirvana",font=("forte",15,"bold"),
                  bg="#616C6F",)
laf.pack(fill='both',expand='yes')

lf1=Label(laf,image=lfphoto)
lf1.pack(fill='both',expand='yes')

v=DoubleVar()
scale=tk.Scale(lf1,variable=v,from_ = 100, to =0,
            orient=VERTICAL,
            troughcolor="black",
            #state=DISABLED
            #sliderlength=10
            length=250,
            # label="Volume",
               width=10,
               showvalue=0,
               command=volume,
               tickinterval=10,
               fg='black',
               bg='white'
            )
scale.set(10)
scale.pack(side=RIGHT,padx=10)

photo=tk.PhotoImage(file=".\\resources\\eye.png").subsample(3,3)
song_image=tk.Label(lf1,height=130,width=150,image=photo,padx=10,pady=10,
                    bg="black"
                    )
song_image.pack()
################################################################################
pglabel=tk.Label(lf1,bg="#616C6F",image=lfphoto)#1
pglabel.pack(pady=10)#1
starttime=tk.Label(pglabel,width=5,text="000")#1
starttime.grid(row=0,column=0,ipadx=3)#1
#style=Style()
#style.configure('TProgressbar',foreground='red',
 #               background='red',
  #              thickness=10)
                
pgbar=ttk.Progressbar(pglabel,#style='TProgressbar',
                  length=400,
                  orient="horizontal",
                  mode="determinate",value=0
                         )#1
pgbar.grid(row=0,column=2,padx=1,pady=1)#1

endtime=tk.Label(pglabel,text="000",width=5,)#1
endtime.grid(row=0,column=3,ipadx=3)#1


################################################################################
show_info=tk.Label(lf1,text='',bg='#ffa801',fg='white')
show_info.pack(pady=10)

string='Hey there, Much more to come'
count=0
text=''


def flow():
              global count,text
              if(count>=len(string)):
                  count=0
                  text=''
                  show_info.config(text=text)
              else:
                  text=text+string[count]
                  show_info.config(text=text)
                  count=count+1
              show_info.after(200,flow)    
 

flow()

#####################################################################################

button_flabel=tk.Label(lf1,height=50,width=500,image=photo,bg="black")
button_flabel.pack(pady=20)
resume_image=PhotoImage(file=".\\resources\\icons\\resume.png").subsample(2,2)
play_image=PhotoImage(file=".\\resources\\icons\\play.png").subsample(2,2)
pause_image=PhotoImage(file=".\\resources\\icons\\pause.png").subsample(2,2)
stop_image=PhotoImage(file=".\\resources\\icons\\stop.png").subsample(2,2)
file_image=PhotoImage(file=".\\resources\\icons\\file.png").subsample(2,2)
mute_image=PhotoImage(file=".\\resources\\icons\\mute.png").subsample(2,2)
unmute_image=PhotoImage(file=".\\resources\\icons\\unmute.png").subsample(2,2)
backward_image=PhotoImage(file=".\\resources\\icons\\backward.png").subsample(2,2)
forward_image=PhotoImage(file=".\\resources\\icons\\forward.png").subsample(2,2)
previous_image=PhotoImage(file=".\\resources\\icons\\previous.png").subsample(2,2)
nexxt_image=PhotoImage(file=".\\resources\\icons\\next.png").subsample(2,2)

#resume=tk.Button(button_flabel,image=resume_image,)
#resume.grid(row=0,column=0,padx=5)
backward=tk.Button(button_flabel,image=backward_image,command=backward)
backward.grid(row=0,column=0,padx=5)

play=tk.Button(button_flabel,image=play_image,command=play)
play.grid(row=0,column=1,padx=5)

forward=tk.Button(button_flabel,image=forward_image,command=forward)
forward.grid(row=0,column=2,padx=5)

pause=tk.Button(button_flabel,image=pause_image,command=pause)
#pause.grid(row=0,column=2,padx=5)

previous=tk.Button(button_flabel,image=previous_image,command=previous)
previous.grid(row=0,column=3,padx=5)

stop=tk.Button(button_flabel,image=stop_image,command=stop)
stop.grid(row=0,column=4,padx=5)

nexxt=tk.Button(button_flabel,image=nexxt_image,command=nexxt)
nexxt.grid(row=0,column=5,padx=5)

file=tk.Button(button_flabel,image=file_image,command=popup)
file.grid(row=0,column=6,padx=5)

mute=tk.Button(button_flabel,image=unmute_image,command=mute)
mute.grid(row=0,column=7,padx=5)

unmute=tk.Button(button_flabel,image=mute_image,command=unmute)
#unmute.grid(row=0,column=5,padx=5)

####################################################################




    
songsframe =tk.LabelFrame(root,text="Song Playlist",
                        font=("forte",12),
                         bg="black",fg="white",
                        relief=GROOVE)
#songsframe.place(x=600,y=0,width=400,height=200)
songsframe.pack(fill='both',expand='yes')
scrol_y = tk.Scrollbar(songsframe,
                    orient=VERTICAL)

playlist = tk.Listbox(songsframe,
                   yscrollcommand=scrol_y.set,
                   selectbackground="green",
                   selectmode=SINGLE,
                   font=("forte",12),
                   bg="black",fg="white",
                   relief=RIDGE,
                   height=15
                      )

scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
    
##play=tk.Button(root,text='PLAY',command=play)
##play.pack(side=LEFT)
##
##stop=tk.Button(root,text='stop',command=stop)
##stop.pack(side=LEFT)
##
##pause=tk.Button(root,text='pause',command=pause)
##pause.pack(side=LEFT)
##
##resume=tk.Button(root,text='resume',command=resume)
##resume.pack(side=LEFT)
    

root.mainloop()
