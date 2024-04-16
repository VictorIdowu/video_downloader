from tkinter import *
from tkinter import filedialog,messagebox
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
  video_path = url_entry.get()
  file_path = path_label.cget("text")
  print('Downloading...')
  mp4 = YouTube(video_path).streams.get_highest_resolution().download()
  video_clip = VideoFileClip(mp4)
  # For mp3
  audio_file = video_clip.audio
  audio_file.write_audiofile('audio.mp3')
  audio_file.close()
  shutil.move('audio.mp3', file_path)
  # For mp4
  video_clip.close()
  shutil.move(mp4, file_path)
  messagebox.showinfo('Info', 'Download complete👍🏿')

def get_path():
  path = filedialog.askdirectory()
  path_label.config(text=path)

root = Tk()
root.title('Video Downloader')
canvas =  Canvas(root, width=600, height=400)
canvas.pack()

# APP LABEL
app_label = Label(root, text='Video Downloader', fg='blue', font=('Arial', 20))
canvas.create_window(300,20,window=app_label)

# Input to accept video url
url_label = Label(root, text="Enter Video URL")
url_entry = Entry(root, width=50)
canvas.create_window(300,80,window=url_label)
canvas.create_window(300,100,window=url_entry)

# Path to download Video
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(300,150,window=path_label)
canvas.create_window(300,180,window=path_button)

# Download Button
download_button = Button(root, text="Download", command=download)
canvas.create_window(300,250,window=download_button)


root.mainloop()