from os import path, remove

filepath = str


## Module Exception
class LogError(Exception):
    ## when it's initializing
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


## Main object for logger
class Logger:
    """
    The main object type - Logger. Its constructor takes three arguments:
    1. Path to the file. Path can be either absolute or relative. File - is the place to store your messages,
    warnings and errors. 'log.txt' by default.

    2. Enter type. Shows the way opening the file using with Logger() as.... 'r' by default, should be 'a' if you need
     to write something in the file using with construction.

    3. Log types. List of types of messages. By default, consists of message, warning, critical warning, error and
     critical error.

    4. Duplicate to console bool.* Only for log(). If True, duplicates the log to console. False by default.
    """

    ## Initializing...
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

    ## bool(Logger())
    def __bool__(self):
        return path.exists(self.filename)

    ## Logger() == other
    def __eq__(self, other):
        return self.filename == other

    ## Logger() != other
    def __ne__(self, other):
        return self.filename != other

    ## Logger() >= other
    def __ge__(self, other):
        return len(self) >= other

    ## Logger() <= other
    def __le__(self, other):
        return len(self) <= other

    ## Logger() > other
    def __gt__(self, other):
        return len(self) > other

    ## Logger() < other
    def __lt__(self, other):
        return len(self) < other

    ## str(Logger())
    def __str__(self):
        return f'Logger object: {self.filename}'

    ## repr(Logger())
    def __repr__(self):
        return str(self)

    ## Length of file
    def __len__(self):
        file = open(self.filename, 'r')
        r = len(file.readlines())
        file.close()
        return r

    ## Log function
    def log(self, message: str = "*log message wasn't given*", log_type: int = None, split_char: str = ": ",
            duplicate_to_console: bool = False):
        if log_type is None:
            log_type = 0
        if log_type >= len(self.log_types):
            raise LogError("Type of the log doesn't exists.")
        else:
            file = open(self.filename, 'a')
            file.write(f'[{self.log_types[log_type]}]{split_char}{message}\n')
            file.close()
            if duplicate_to_console:
                self.console_log(message=message, log_type=log_type, split_char=split_char)

    ## reversed(Logger())
    def __reversed__(self):
        file = open(self.filename, 'r')
        rev = reversed(list(file))
        file.close()
        return rev

    ## IDK what is it, modified version of print(), or something, i'm going to delete this in the future
    def console_log(self, message: str = "*log message wasn't given*", log_type: int = None,
                    split_char: str = ": "):
        if log_type is None:
            log_type = 0
        if log_type >= len(self.log_types):
            raise LogError("Type of the log doesn't exists.")
        else:
            print(f'[{self.log_types[log_type]}]{split_char}{message}')

    ## clearing the logs when needed
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
        res = file.readlines()[-1]
        file.close()
        return res

    ## entering context manager (with Logger() as file: ...)
    def __enter__(self):
        self.file = open(self.filename, self.enter_method)
        return self.file

    ## exiting context manager
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.file.close()
        del self.file


class LoggerGroup:
    def __init__(self, logger_list: dict[str: Logger]):
        self.logger_list = logger_list

    def log(self, logger_name, message: str = "*log message wasn't given*", log_type: int = None,
            split_char: str = ": ",
            duplicate_to_console: bool = False):
        self.logger_list[logger_name].log(message=message, log_type=log_type, split_char=split_char,
                                          duplicate_to_console=duplicate_to_console)

    def console_log(self, logger_name, message: str = "*log message wasn't given*", log_type: int = None,
                    split_char: str = ": "):
        self.logger_list[logger_name].console_log(message=message, log_type=log_type, split_char=split_char)


if __name__ == "__main__":
    print("Module was started as main file.")
    raise SystemExit
