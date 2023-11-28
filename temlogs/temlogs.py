from os import path, remove

filepath = str
##Module Exception
class LogError(Exception):
    ##when it's initializing
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    ## when it's raising
    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'Unexpected Error'


##Main object for logger
class Logger(object):
    ##Initializing...
    def __init__(self, filename: filepath = "log.txt", enter_method: str = 'r', log_types=None):
        if log_types is None:
            log_types = ["Message", "Warning",
                         "Critical Warning", "Error",
                         "Critical Error"]
        self.filename: filepath = filename
        if not path.exists(filename):
            a = open(filename, "w")
            a.close()
        self.log_types = log_types
        self.enter_method = enter_method

    ##Logger() == other
    def __eq__(self, other):
        file = open(self.filename, "r")
        r = list(file) == other
        file.close()
        return r

    ##Logger() != other
    def __ne__(self, other):
        file = open(self.filename, "r")
        r = list(file) != other
        file.close()
        return r

    ##Logger() >= other
    def __ge__(self, other):
        file = open(self.filename, "r")
        r = list(file) >= other
        file.close()
        return r

    ##Logger() <= other
    def __le__(self, other):
        file = open(self.filename, "r")
        r = list(file) <= other
        file.close()
        return r

    ##Logger() > other
    def __gt__(self, other):
        file = open(self.filename, "r")
        r = list(file) > other
        file.close()
        return r

    ##Logger() < other
    def __lt__(self, other):
        file = open(self.filename, "r")
        r = list(file) < other
        file.close()
        return r

    ##str(Logger())
    def __str__(self):
        file = open(self.filename, "r")
        r = ' '.join(list(file))
        file.close()
        return r

    ## abs(Logger())
    def __abs__(self):
        raise LogError("Can't use abs() - logger isn't a number.")

    ##round(Logger())
    def __round__(self, n=None):
        raise LogError("Can't use round() - logger isn't a number.")

    ##bool(Logger())
    def __bool__(self):
        file = open(self.filename, 'r')
        if file:
            file.close()
            return True
        else:
            file.close()
            return False

    ##Length of file
    def __len__(self):
        file = open(self.filename, 'r')
        r = len(list(file))
        file.close()
        return r

    ##Log function
    def log(self, message: str = "*log message wasn't given*", log_type: int = None, split_char: str = ": "):
        if log_type is None:
            log_type = 0
        if log_type >= len(self.log_types):
            raise LogError("Type of the log doesn't exists.")
        else:
            file = open(self.filename, 'a')
            file.write(f'[{self.log_types[log_type]}]{split_char}{message}\n')
            file.close()

    ##reversed(Logger())
    def __reversed__(self):
        file = open(self.filename, 'r')
        rev = reversed(list(file))
        file.close()
        return rev

    ##IDK what is it, modified version of print(), or something, i'm gonna delete this in the future
    def console_log(self, message: str = "*log message wasn't given*", log_type: int = None,
                    split_char: str = ": "):
        if log_type is None:
            log_type = 0
        if log_type >= len(self.log_types):
            raise LogError("Type of the log doesn't exists.")
        else:
            print(self.log_types[log_type] + split_char + message)

    ##clearing the logs when needed
    def clear_file(self):
        file = open(self.filename, 'w')
        file.write('')
        file.close()

    ## deleting log file
    def delete_file(self):
        remove(self.filename)

    ## getting the last log
    def last_log(self):
        file = open(self.filename, 'r')
        res = list(file)[-1]
        file.close()
        return res

    ## entering context manager (with Logger() as file: ...)
    def __enter__(self):
        self.file = open(self.filename, self.enter_method)
        return self.file

    ## exiting context manager
    def __exit__(self):
        self.file.close()
        del self.file


if __name__ == "__main__":
    print("Module was started as main file.")
    raise SystemExit
