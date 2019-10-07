from flask import Flask, render_template, url_for, request, redirect
from werkzeug import secure_filename
import os
import img_operation

IMAGE_FOLDER = os.path.join('static', 'photos')
file_name = 1

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['imgfile']
		global imgname
		imgname = secure_filename(f.filename)
		extension = os.path.splitext(imgname)[1][1:]
		imgname = 'image.'+extension
		imgpath = 'static/photos/output_'+imgname
		f.save(imgpath)
		#img_operation.squarefit(imgpath)
		img_operation.greyscale(imgpath)
		imgname = 'img.'+extension
		return redirect('show')	

@app.route('/show')
def show():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output_'+imgname)
	masked_image = full_filename
	print masked_image
	return render_template('show.html', user_image = masked_image)

if __name__ == '__main__':
    app.run(debug = True)