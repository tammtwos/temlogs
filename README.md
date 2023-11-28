# TemLogs 1.1 - Simplest logging lib.

Module is written using OOP, so...

The main object type - Logger. Its constructor takes three arguments:
1. **Path to the file.**  Path can be either absolute or relative. File - is the place to store your messages, warnings and errors. 'log.txt' by default.
2. **Enter type**  Shows the way opening the file using `with Logger() as...`. 'r' by default, should be 'a' if you need to write something in the file using `with` construction.
3. **Log types** List of types of messages. By default, consists of message, warning, critical warning, error and critical error.

Logger is basic represent of log file. Its main methods - `log()` and `console_log()`.
Second method is specific, because, maybe, it's just printing message to the console.
All of the methods take three arguments - message, log type and split char. 
1. **Message** String, that contains your message.
2. **Log type** Integer, that represents the index of needed log type from `Logger.log_types`. Indexing starting from 0.
3. **Split character** String, that stands between log type and message.

Log messages looks like
`[Error]: User's age can't be less than 13.`
Logger's log_types is default, 
message is "User's age can't be less than 13.", 
log type is 3, 
split char is ': '.
