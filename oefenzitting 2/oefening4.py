from graphics import GraphicsWindow
window = GraphicsWindow(400,400)
canvas = window.canvas()
canvas.drawOval(200, 200, 100, 100)
window.wait()