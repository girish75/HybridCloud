from flask import Flask, render_template

app = Flask(__name__)
#Now define the basic route / and its corresponding request handler:
@app.route("/")
def main():
    return render_template('index.html')
    #return "Welcome to the world of Azure learning - By Girish Pareek!"
#Next, check if the executed file is the main program and run the app: 
if __name__ == "__main__":
    app.run()
