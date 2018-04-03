import sys
import os, string
from pymongo import MongoClient
from gridfs import GridFS
import base64

from flask import Flask, request, render_template, session

@app.route('/')
def mainpage():
	return render_template('mongostart.html')

@app.route('/imageupload',methods=['GET','POST'])
def imageupload():
	image = request.files['image']	
	connection = MongoClient("ds040349.mlab.com", 40349)
	db = connection["mongologinexample"]
	# MongoLab has user authentication
	db.authenticate("dbusername", "dbpassword")
	fs = GridFS(db)
	# encode_content = base64.b64encode(image.stream.read())
	encode_content  = "hello"
	oid = fs.put(encode_content, content_type="image/jpeg", filename=image.filename)
	# posts = db.posts
	# post = {'firstname':'Romil','lastname':'Bheda'}
	# id_pythonmongo = posts.insert(post)
	print 'Create the id: %s'%oid
	return render_template('mongostart.html')

@app.route('/imageretrieve',methods=['GET','POST'])
def retrieve():
	connection = MongoClient("ds040349.mlab.com", 40349)
	db = connection["mongologinexample"]
	# MongoLab has user authentication
	db.authenticate("dbusername", "dbpassword")
	fs = GridFS(db)
	fslist = db.fs.chunks.find()
	list1 = ''
	for abc in fslist:
		data = abc["data"]
		list1 += "<br><br><img src= \""+"data:image/jpeg;base64,"+data+"\">"
	return '''<!DOCTYPE html><html><head><title>Python Flask Application</title><link rel="stylesheet" href="static/stylesheets/style.css"></head><body>''' + list1 + '''</body></html>'''
			
if __name__ == "__main__":
	app.debug=True
	app.run(host='mypage.southcentralus.cloudapp.azure.com', port=5000)
	