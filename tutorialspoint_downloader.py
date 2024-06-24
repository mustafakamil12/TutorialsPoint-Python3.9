import urllib.request

def download(tutorialName):
    #https://www.tutorialspoint.com/mysql/mysql_tutorial.pdf
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    print(url)
    downloadLocation = '/Users/mustafaalogaidi/Desktop/TutorialsPoint-Python3.9/'
    try:
        pdf = urllib.request.urlopen(url)
        saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')
        saveFile.write(pdf.read())
        saveFile.close()
        print(tutorialName + ' Tutorial is Downloaded Successfully !!!')
    except:
        print("Failed to download")

if __name__ == '__main__':
    tutorialName = input('Name of the tutorial pdf to be downloaded: ')
    download(tutorialName)
