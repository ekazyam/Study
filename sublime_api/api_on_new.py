import sublime
import sublime_plugin


class EventDump(sublime_plugin.EventListener):

    def on_new(self, view):
        sublime.message_dialog("new file is opned.")
