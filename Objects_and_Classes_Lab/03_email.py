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

info = input()
while info != "Stop":
    info_args = info.split()
    sender = info_args[0]
    receiver = info_args[1]
    content = info_args[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    info = input()

sent_emails = list(map(lambda x: int(x), input().split(", ")))

for i in sent_emails:
    emails[i].send()

for email in emails:
    print(email.get_info())
