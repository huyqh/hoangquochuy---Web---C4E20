import mlab
from mongoengine import*
from flask import*
from youtube_dl import YoutubeDL
from models.video import Video
app = Flask(__name__)

mlab.connect()
app.secret_key = ' a super super secret key'

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'loggedin' in session:
        if session['loggedin'] == True:
            if request.method == 'GET':
                videos = Video.objects()
                return render_template('admin.html', videos = videos)
            
            elif request.method == "POST":
                form = request.form
                
                link = form['link']

                
                ydl = YoutubeDL()
                
                data = ydl.extract_info(link, download=False)

                title = data['title']
                views = data['view_count']
                thumbnail = data['thumbnail']
                youtube_id = data['id']

                video = Video(
                    title = title,
                    views = views,
                    thumbnail = thumbnail,
                    youtube_id = youtube_id,
                    link = link
                )
                video.save()
                return redirect(url_for('admin'))
        else: 
            return 'yêu cầu đăng nhập'
    else:
        return 'yêu cầu đăng nhập'

@app.route('/logout')
def logout():
    session['loggedin'] = False
    return redirect(url_for('index'))

       

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id = youtube_id)



@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method =='POST':
        form = request.form
        username = form['username']
        password = form['password']

        if username == 'admin' and password == 'adminc4e20':
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return 'Sai tên tài khoản'
  



if __name__ == '__main__':
  app.run(debug=True)
 

