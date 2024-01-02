import PySimpleGUI as sg
from pytube import YouTube
import os


output_folder = "videos"

sg.theme('DarkAmber')

layout = [
    [sg.Text('BRN - YOUTUBE VIDEO DOWNLOADER')],
    [sg.Text('Insira o link do vídeo do YouTube:')],
    [sg.Input(key='link_video', size=(50, 10), background_color='white', text_color='black')],
    [sg.Button('Baixar', size=(50, 3), button_color=("black", "green"))],
        [sg.Text('Download Status')],
    [sg.Text('', key="status_message")]
]


window = sg.Window('YouTube Video Downloader 1.0', layout=layout, font='arial')


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        link_do_video = values['link_video']

        try:
            video = YouTube(link_do_video)
            stream = video.streams.get_highest_resolution()


            output_path = os.path.join(output_folder, f"{video.title}.mp4")


            stream.download(output_path)
            
            window["status_message"].update("Download completo", text_color="green")

            window["link_video"].update("")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break