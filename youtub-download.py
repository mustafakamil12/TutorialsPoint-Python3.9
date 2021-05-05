import pytube

#url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'
url = 'https://www.youtube.com/watch?v=UN1QB5BIvps&list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK'

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download('/Users/mustafaalogaidi/Desktop/MyWork/LinuxTutorial/')
