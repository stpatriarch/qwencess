#!/usr/bin/env python3

import requests

from textual.app import App, ComposeResult
from textual.containers import Center, VerticalScroll
from textual.widgets import Input, Markdown
from textual.color import Color

class InputDecroation(Input):
    """input decor"""
        
    def on_mount(self):
        # self.styles.padding = (0, 0)
        # self.styles.margin = (1, 50) 
        self.styles.background = '#adbac0'

class MarkAiResponse(Markdown):
    """"""

    def on_mount(self):
        self.styles.width = '80%'
        self.styles.padding = (0, 0)
        # self.styles.margin = (1, 80)
        self.styles.background = Color(93, 94, 97, a=0.4)

class AiInterface(App):

    CSS_PATH = "style/aiinterface.tcss"

    def compose(self) -> ComposeResult:
        self.theme = 'gruvbox'
        with Center():
            yield VerticalScroll(id='ai_response')
        # with Center():
            yield InputDecroation(placeholder='enter for response', id='prompt')


    def on_mount(self) -> None:
        self.query_one("#prompt").focus()

        # self.screen.styles.background = 'black'

    def on_input_submitted(self, event: Input.Submitted):

        if event.input.id == 'prompt':

            text = event.value

            # self.query_one("#ai_response").mount(MarkAiResponse(text))
            response = requests.post('http://127.0.0.1:5000/ask', json={'prompt': text})
            data = response.json()
            self.query_one("#ai_response").mount(MarkAiResponse(data['content']))

            event.input.value = ''


if __name__ == "__main__":
    app = AiInterface()
    app.run()

#     def on_button_pressed(self) -> None:
#         """Clear the text input."""
#         input = self.query_one(Input)
#         with input.prevent(Input.Changed):  
#             input.value = ""
