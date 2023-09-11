import gradio as gr
 
def greet(name):
    return "Hello " + name + "!"
 
demo = gr.Interface(fn=greet, inputs="image", outputs="text")
 
demo.launch()