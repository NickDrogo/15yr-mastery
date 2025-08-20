messages = ['Christ is king', 'He reigneth on the throne forever', 'For our lord is good', 'All the time']
completed_message = []


def send_messages(messages):
        while messages:
            current_message = messages.pop()
            print(current_message)
            completed_message.append(current_message)


send_messages(messages)
print(messages)
print(completed_message)


