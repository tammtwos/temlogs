# TemLogs 1.1 - Simplest logging lib.

## Basics of TemLogs.
Module is written using Object-Oriented Programming, so...

The main object type - Logger. Its constructor takes three arguments:
1. **Path to the file.** Path can be either absolute or relative. File - is the place to store your messages, warnings and errors. 'log.txt' by default.
2. **Enter type.** Shows the way opening the file using `with Logger() as...`. 'r' by default, should be 'a' if you need to write something in the file using `with` construction.
3. **Log types.** List of types of messages. By default, consists of message, warning, critical warning, error and critical error.
4. **Duplicate to console bool.** Only for `log()`. If True, duplicates the log to console. False by default. 

Logger is basic represent of log file. Its main methods - `log()` and `console_log()`.
Second method is specific, because, maybe, it's just printing message to the console.
All the methods take three arguments - message, log type and split char. 
1. **Message.** String, that contains your message.
2. **Log type.** Integer, that represents the index of needed log type from `Logger.log_types`. Indexing starting from 0. 0 by default.
3. **Split character.** String, that stands between log type and message. `': '` by default.

Log messages looks like `[Error]: User's age can't be less than 13.`, where
* Logger's log_types is default,
* message is `"User's age can't be less than 13."`, 
* log type is 3 (Error), 
* split char is `': '`.

Examples:

```
import temlogs 

loggr = temlogs.Logger("C:\test.txt", log_types=['a', 'b'])

loggr.log()
```
Following code will create a test.txt file in C:\ directory and put this message in:
```
[a]: *log message wasn't given*
```

## File operating methods.
### `last_log()`
`last_log()` is pretty simple function that returns... the last log in the logger.
If your message contained `\n` or `\r` symbols, it may break this function, because technically, it returns the last line in the file. 

Example:
```
loggr = Logger()
loggr.log()

print(loggr.last_log())
```
Following code will output this:
```
[Message]: *log message wasn't given*
```
### `clear_file()`
`clear_file()` is... makes file clear. 

Example:
```
loggr = Logger()
loggr.log()

loggr.clear_file()
```
Following code will log the default message and then delete it.

### `delete_file()`
`delete_file()` deletes the logger file, can be useful when the file is broken.

**WARNING!** You should use `log()` right after that, because reading file that don't exist may cause errors.

Example:
```
loggr = Logger()
loggr.log()

loggr.delete_file()
loggr.log()
```
Following code will log the default message, delete file with this message and then log the message one more time.

## Context Manager.
You can use `Logger()` as `open()` with `with` construct.

`Logger().enter_method` can be `'r'`, `'a'` and `'w'`.

* `'r'` - reading. Default value of this parameter. `file.read()` and `file.readlines()` functions is available.
* `'w'` - writing. Every time you write something via `with`, file is clearing. `file.write()` function is available.
* `'a'` - appending. Similar to 'w', but data isn't clearing after every log.

Examples: 
```
loggr = Logger()
loggr.log()

with loggr as file:
    a = file.readlines()
```

## Logger Group
Sometimes, for big apps it is difficult to have all logs in the same file.

You can create LoggerGroup object. Its constructor takes one argument - dictionary,
that looks like
```
LoggerGroup({
        'loggr1': Logger(),
        'loggr2': Logger(), 
        'loggr3': Logger()  
    })
```
Then you can use methods `log()` and `console_log()` as you usually do it with single Logger objects.
Syntax looks like
```
loggrg = LoggerGroup({
        'loggr1': Logger(),
        'loggr2': Logger(), 
        'loggr3': Logger()  
    })
    
loggrg.log('loggr', message='first message', log_type=1, split_char=' - ')
```

**Good luck with using this lib! Hope you enjoy it.**