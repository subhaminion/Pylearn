# "C:\Users\subha\Downloads\17807246_1411210925607286_7765544507034600342_o.jpg"
import notify2

def notify():
	icon_path = "C:\Users\subha\Downloads\17807246_1411210925607286_7765544507034600342_o.jpg"
	n = notify2.Notification("Meow!!!", icon = icon_path)
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.set_timeout(1000)

notify()