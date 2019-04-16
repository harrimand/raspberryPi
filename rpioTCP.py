import RPIO

def socket_callback(socket, val):
    print("socket %s: '%s'" % (socket.fileno(), val))
    socket.send(val+"\n".encode())

# TCP socket server callback on port 8080
RPIO.add_tcp_callback(8080, socket_callback, threaded_callback=True)

# Blocking main epoll loop
try:
    RPIO.wait_for_interrupts()
except KeyboardInterrupt:
    RPIO.stop_waiting_for_interrupts()
    RPIO.cleanup()
    print("\nStopping Server\n")


