import json
import socket
import ssl

host_addr = 'api.vk.com'
port = 443


def request(socket, request):
    socket.send((request + '\n' * 2).encode())
    recv_data = socket.recv(65535).decode()
    return recv_data


def get_or_close(category):
    try:
        result = str(r["response"][0]["counters"][category])
        if result == "0":
            return "closed"
    except KeyError:
        result = "closed"
    return result


id = "your id :)"
token = "your token :)"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host_addr, port))
    client = ssl.wrap_socket(client)
    answ = request(client, f'GET /method/users.get?user_ids={id}&'
                           f'fields=city,'
                           f'bdate,'
                           f'counters&access_token={token}&'
                           f'v=5.130 HTTP/1.1\nHost: {host_addr}')
r = json.loads(answ.split("\n")[-1])
user_id = "id---------" + str(r["response"][0]["id"])
name = "name---------" + str(r["response"][0]["first_name"])
surname = "surname---------" + str(r["response"][0]["last_name"])
city = "city---------" + r["response"][0]["city"]["title"]
friends_count = "friends---------" + get_or_close("friends")
online = "online---------" + get_or_close("online_friends")
followers = "followers---------" + get_or_close("followers")
"\n"

result = user_id + "\n" + name + "\n" + surname + \
         "\n" + city + "\n" + friends_count + "\n" + online + "\n" + followers
print(result)
