
import RPIO

def gpio_callback(gpio_id, val):
    print("gpio %s: %s" % (gpio_id, val))

def socket_callback(socket, val):
#    byteval = ("echo"+val).encode()
    print("socket %s: '%s'" % (socket.fileno(), val))
#    socket.send("echo: %s\n" % val)
    socket.send(val+"\n".encode())

# GPIO interrupt callbacks
RPIO.add_interrupt_callback(7, gpio_callback, threaded_callback=True)
RPIO.add_interrupt_callback(9, gpio_callback, pull_up_down=RPIO.PUD_UP, threaded_callback=True)
# RPIO.add_interrupt_callback(7, gpio_callback, threaded_callback=False)
# RPIO.add_interrupt_callback(9, gpio_callback, pull_up_down=RPIO.PUD_UP, threaded_callback=False)

# TCP socket server callback on port 8080
# RPIO.add_tcp_callback(8080, socket_callback)
RPIO.add_tcp_callback(8080, socket_callback, threaded_callback=True)

# Blocking main epoll loop
RPIO.wait_for_interrupts()

