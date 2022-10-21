from pytube import YouTube

def get_infos(alink):
    url = YouTube(str(alink))
    v_title = url.title
    v_author = url.author
    v_published_date = url.publish_date.strftime("%Y-%m-%d")
    v_nb_views = url.views
    v_length = url.length

    return (v_title, v_author, v_published_date, v_nb_views, v_length)

def Downloader(alink):
    url = YouTube(str(alink))
    video = url.streams.first()
    video.download()




