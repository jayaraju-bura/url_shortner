from flask import Flask, request
import url_shortner
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def hello():
    long_url = request.args.get('url')
    if long_url:
        url_inst = url_shortner.UrlShortner()
        url_inst.runtests()
        url_inst.long_url = long_url
        print("tiny url for the requested URL is "+url_inst.run())
        return url_inst.run()
    else:
        return "Not Found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
