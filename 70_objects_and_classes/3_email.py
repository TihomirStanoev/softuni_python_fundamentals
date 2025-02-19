class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    line = input().split()
    if line[0] == "Stop":
        break

    sender, receiver, content = line

    email = Email(sender, receiver, content)
    emails.append(email)

inds = list(map(int,input().split(', ')))

[emails[i].send() for i in inds]


for email in emails:
    print(email.get_info())