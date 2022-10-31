import pyads

# create some constants for connection
CLIENT_NETID = "192.168.11.5.1.1" # moj
CLIENT_IP = "192.168.11.5"
TARGET_IP = "192.168.11.21"
TARGET_NETID = '192.168.11.21.1.1'
TARGET_USERNAME = "Administrator"
TARGET_PASSWORD = "1"
ROUTE_NAME = "ABM-NARZ-1"
print(pyads.PORT_SPS1, type(pyads.PORT_SPS1))
print("-----------------")

#print("----add_route_to_plc start -------------")

#pyads.add_route_to_plc(
#    CLIENT_NETID, CLIENT_IP, TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD,
#    route_name=ROUTE_NAME
#)
#print("----add_route_to_plc end -------------")
# connect to plc and open connection
# route is added automatically to client on Linux, on Windows use the TwinCAT router
# plc = pyads.Connection(TARGET_NETID, 851)
pyads.open_port()
plc = pyads.Connection(TARGET_NETID, 851)
plc.open()

# check the connection state
plc.read_state()
# (0, 5)

# read int value by name
i = plc.read_by_name("GVL.bPracaAuto")

# write int value by name
# plc.write_by_name("GVL.real_val", 42.0)

# create a symbol that automatically updates to the plc value
real_val = plc.get_symbol("GVL.bPracaAuto", auto_update=True)
print(real_val.value)
#42.0
real_val.value = 5.0
print(plc.read_by_name("GVL.bPracaAuto"))
#5.0

# close connection
plc.close()