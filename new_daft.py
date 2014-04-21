import sublime, sublime_plugin

class JekyllNewDraftCommand(sublime_plugin.WindowCommand):
    def run(self):
        new_draft = self.window.new_file()
        new_draft.set_syntax_file("Packages/Jekyll/Syntaxes/Markdown (Jekyll).tmLanguage")
        new_draft.run_command("insert_snippet", {"name": "Packages/Jekyll/Snippets/new_draft.sublime-snippet"})
