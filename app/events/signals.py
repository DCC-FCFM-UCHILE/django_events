from django.dispatch import Signal

# handler_event_signal se dispara cuando se recibe un mensaje por la cola de events
handler_event_signal = Signal()
