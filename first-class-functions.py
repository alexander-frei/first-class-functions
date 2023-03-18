#------------------------------------------------------------
#  First class functions: functions = first class citizens
#  https://www.youtube.com/watch?v=kr0mpwqttM0
#------------------------------------------------------------

#----------------------------------------
#  Example: html environment > html command
#----------------------------------------
def html_command(tag):
    def wrap_text(some_text):
        print(f"<{tag}> {some_text} </{tag}>")
    return wrap_text

#--------------------
#  Applied > message command
#--------------------
message = html_command("message")
message("Hello fellows")
message("Some news")