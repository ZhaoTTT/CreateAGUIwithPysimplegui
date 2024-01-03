import PySimpleGUIQt as s
# import PySimpleGUIWeb as s

mylayout = [
    [s.Text("hello world")], 
    [s.Button("OK"), s.Button("Cancel")]
]
window = s.Window(
    title="hihihi", 
    size=(640,4800), 
    layout=mylayout
    )
window.read()

s.preview_all_look_and_feel_themes()