from flask import Flask , render_template

 app=Flask(__name__)

 @app.route('/')
 def home():
    return render_template("home.html")
 
 
 @app.route('/api/v1/word')
 def api(word):
     uppercase=word.Title()
     result_dictionary={"word":word,"Uppercase":uppercase}
     return result_dictionary
 

