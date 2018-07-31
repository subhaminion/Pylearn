import threading


def hello_world():
    threading.Timer(5.0, hello_world).start()
    print("Hello, World!")


hello_world()
