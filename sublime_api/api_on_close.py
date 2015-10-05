import sublime
import sublime_plugin


class EventDump(sublime_plugin.EventListener):

    def on_close(self, view):
        sublime.message_dialog("file is closed.")
