from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.metrics import dp, sp
from kivy.uix.widget import Widget

Builder.load_file("./calculator.kv")


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "error" in prev_number:
            prev_number = ""

        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    def signs(self, sign):
        prev_number = self.ids.input_box.text
        last = prev_number[-1]

        if last in {"+", "-", "/", "*", "%"}:
            prev_number = prev_number[:-1]
            self.ids.input_box.text = f"{prev_number}{sign}"

        else:
            self.ids.input_box.text = f"{prev_number}{sign}"

    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def positive_negative(self):
        prev_number = self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"

    def dot(self):
        prev_number = self.ids.input_box.text
        if (
            any(op in prev_number for op in "+-/*%")
            and "." not in prev_number.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1].split("%")[-1]
        ):
            prev_number += "."
            self.ids.input_box.text = prev_number
        elif "." not in prev_number:
            prev_number += "."
            self.ids.input_box.text = prev_number

    def results(self):
        prev_number = self.ids.input_box.text
        last = prev_number[-1]
        if "." == prev_number[-1]:
            prev_number = f"{prev_number}0"
        elif "%" == prev_number[-1]:
            prev_number = f"{prev_number}1"

        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "error"


class CalculatorApp(App):
    def build(self):
        self.icon = "calculator.png"
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
