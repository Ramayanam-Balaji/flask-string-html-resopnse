from flask import Flask,render_template
fai=Flask(__name__)

@fai.route('/string')
def string():
    return 'hi this is balaji'

@fai.route('/first')
def first():
    return render_template('first.html',name='balaji',age=20)

if __name__=='__main__':
    fai.run(debug=True)
