# events/signals.py

from django.dispatch import Signal

# emitter_event_signal se debe disparar cuando se quiera colocar un mensaje en la cola de events
emitter_event_signal = Signal()
# handler_event_signal se dispara cuando se recibe un mensaje por la cola de events
handler_event_signal = Signal()
