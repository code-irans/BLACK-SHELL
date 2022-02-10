# start function



def log_create(data):
    file = open("logs/create.log", 'a')

    formated = "[Create] Log Added : '{}'".format(data)

    file.write(formated + "\n")

def log_remove(data):
    file = open("logs/remove.log", 'a')

    formated = "[Remove] Log Added : '{}'".format(data)

    file.write(formated + "\n")


def log_check(data):
    file = open("logs/check.log", 'a')

    formated = "[Check] Log Added : '{}'".format(data)

    file.write(formated + "\n")

def log_quit(data):
    file = open("logs/quit.log", 'a')

    formated = "[Quit] Log Added : '{}'".format(data)

    file.write(formated + "\n")



# end function




def SaveLog(action, data_log):

    if action == "create":
        log_create(data_log)

    elif action == "remove":
        log_remove(data_log)
    
    elif action == "check":
        log_check(data_log)

    elif action == "quit":
        log_quit(data_log)

