from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'
@app.route('/dojo')
def dojo():
    return f"DOJO!"
@app.route('/<name>')
def dojo_name(name):
    return f"HI {name}"
@app.route('/<string:name>/<int:num>')
def display_name(name,num):
    #if num.isdigit():
       if num == int(num):
         return f"HI {name * num}"
       else:
         
          return f"Sorry! No response. Try again."

if __name__ == '__main__':
    app.run(debug=True)