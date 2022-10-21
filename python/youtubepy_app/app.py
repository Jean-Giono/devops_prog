from flask import Flask, render_template, request
import youtubepy

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/downloader',methods=["GET","POST"])
def download():
    if request.method == 'POST':
        video_link = request.form['videolink']
        v_title,v_author,v_published_date,v_nb_views,v_length = youtubepy.get_infos(video_link)
        youtubepy.Downloader(video_link)
    return render_template('result.html', vlink=video_link, vtitle=v_title, vauthor=v_author,vpublidate=v_published_date, vnbviews=v_nb_views, vlength=v_length)
    #return render_template('result.html', **locals())

if __name__ == '__main__':
	app.run(debug=True, use_reloader=False)
	#app.run(host='0.0.0.0', port=8000, debug=True)
