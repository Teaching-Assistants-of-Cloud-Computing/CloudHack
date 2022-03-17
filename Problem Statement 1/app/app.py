from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

user = ''           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = ''       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = ''    # service name of the mongodb admin server as set in the service for mongodb server
port = ''              # port number of the mongodb admin server as set in the service for mongodb server
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog

@app.route('/')
def home():
    posts = list(db.posts.find({}))
    return render_template("home.html", homeIsActive=True, createPostIsActive=False, posts=posts)

@app.route('/create-post', methods=["GET", "POST"])
def createPost():
    if(request.method=="GET"):
        return render_template("create-post.html", homeIsActive=False, createPostIsActive=True)

    elif(request.method == "POST"):
        title = request.form['title']
        author = request.form['author']
        createdAt = datetime.now()

        # save the record to the database
        db.posts.insert_one({"title": title, "author": author, "createdAt": createdAt})

        # redirect to home page
        return redirect("/")

@app.route('/edit-post', methods=['GET', 'POST'])
def editPost():
    if request.method == "GET":
        # get the id of the post to edit
        postId = request.args.get('form')

        # get the post details from the db
        post = dict(db.posts.find_one({"_id":ObjectId(postId)}))

        # direct to edit post page
        return render_template('edit-post.html', post=post)

    elif request.method == "POST":
        #get the data of the post
        postId = request.form['_id']
        title = request.form['title']
        author = request.form['author']

        # update the data in the db
        db.posts.update_one({"_id":ObjectId(postId)},{"$set":{"title":title,"author":author}})

        # redirect to home page
        return redirect("/")

@app.route('/delete-post', methods=['POST'])
def deletePost():
    # get the id of the post to delete
    postId = request.form['_id']

    # delete from the database
    db.posts.delete_one({ "_id": ObjectId(postId)})

    # redirect to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
