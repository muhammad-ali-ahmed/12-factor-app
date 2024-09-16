from flask import Flask
from redis import Redis

app = Flask(__name__)
redisDb = Redis(host='redis-db',port=6380)

@app.route('/')
def welcome():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'),'utf-8')
    return "Welcome to Stranger's World" + visitCount

if __name__ == "__main__":

    app.run(host="0.0.0.0",debug=True)