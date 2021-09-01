import redis
from flask import Flask, request
from time import strftime

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6380, db=0)


@app.route('/')
def theanswer():
    day = strftime('%Y-%m-%d')
    user_ip = request.remote_addr
    result: str = ''
    r.sadd(f'page:index:counter:{day}', user_ip)
    counter_str = f'Unique visitors today ({day}) = ' + str(r.scard(f'page:index:counter:{day}')) + '\n'
    unique_users = r.smembers(f'page:index:counter:{day}')
    for user in unique_users:
        result = result + str(user) + '\n'
    return counter_str+' : '+result
