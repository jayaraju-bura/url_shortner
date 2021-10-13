# url_shortner

bash:url_shortner bura$ python3 main.py 
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.1.8:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 108-951-237
tiny url for the requested URL is https://shorturl.com/JEE7XUE77A786
192.168.1.8 - - [13/Oct/2021 23:20:33] "GET /?url=https://www.geeksforgeeks.org/topological-sorting/?ref=leftbar-rightbar HTTP/1.1" 200 -
INFO:werkzeug:192.168.1.8 - - [13/Oct/2021 23:20:33] "GET /?url=https://www.geeksforgeeks.org/topological-sorting/?ref=leftbar-rightbar HTTP/1.1" 200 -

Response:- https://shorturl.com/JEE7XUE77A786



docker run -p 5000:5000 -it --name shorturl -v urls:/app/database  <image-name>
  
link to docker image:- https://hub.docker.com/layers/171913822/jayaraju2908/url_shortner/latest/images/sha256-e442d693cb20e5850049f222a1eaf37fca499d09ccdbe72e5355931f441aab58?context=repo 
