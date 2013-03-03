import sublime, sublime_plugin
import os.path

class OpenDirectoryInFinderCommand(sublime_plugin.WindowCommand):
  def run(self):
    directory = os.path.dirname(self.window.active_view().file_name())
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.set("show_panel_on_build", False)
    self.window.run_command("exec", {"cmd": ["open", directory ] })
    settings.set("show_panel_on_build", True)

