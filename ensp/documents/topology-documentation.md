Network Topology Documentation - Huawei eNSP
Overview
This document details a Huawei enterprise network topology featuring multiple VLANs, routers, switches, and end devices. The network implements a hierarchical design with core routers, distribution switches, and access layer connectivity using Huawei networking equipment.
Network Architecture
Core Layer (Routers)
The network core consists of 6 routers providing inter-VLAN routing and WAN connectivity:
Router Interconnections:
• ISP Router: Central internet gateway
o Connected to AR3, AR4, Router1, Router2
• AR1
o Connected to: AR2, AR4, R4 Cisco (cloud)
• AR2
o Connected to: AR1, AR3, AR4
• AR3
o Connected to: ISP, AR2
• AR4
o Connected to: ISP, AR1, AR2
• Router1
o Connected to: ISP, LSW1
• Router2
o Connected to: ISP, LSW2
Distribution/Access Layer (Switches)
Four switches provide access layer connectivity and VLAN segmentation:
Switch Infrastructure:
• LSW1: Connected to Router1 and with LSW2, LSW3, LSW4, DHCP_Server, DNS_Server, PBX
• LSW2: Connected to Router2 and with LSW1, LSW3, LSW4, DHCP_Server, DNS_Server, PBX
• LSW3: Connected to LSW1, LSW2 and with PC1
• LSW4: Connected to LSW1, LSW2 and with Windows1
Network Segmentation Analysis
Point-to-Point Router Networks (/30 subnets)
Each /30 network connects exactly two router interfaces:
156.0.10.16/30 Network:
• AR2 (interface)
• AR3 (interface)
156.0.10.0/30 Network:
• AR3 (interface)
• ISP Router (interface)
156.0.10.4/30 Network:
• AR4 (interface)
• ISP Router (interface)
156.0.10.12/30 Network:
• AR2 (interface)
• AR4 (interface)
156.0.10.20/30 Network:
• AR2 (interface)
• AR1 (interface)
156.0.10.8/30 Network:
• AR1 (interface)
• AR4 (interface)
192.10.6.0/30 Network:
• AR1 (interface)
• R4 Cisco (cloud)
177.0.10.0/28 Network:
• ISP Router (interface)
• Router1 (interface)
144.0.10.0/28 Network:
• ISP Router (interface)
• Router2 (interface)
VLAN Networks (End Device Networks)
VLAN 10 Network (172.16.10.0/24):
• PC1: 172.16.10.10
• Name: VoIP
VLAN 11 Network (192.168.10.0/24):
• DHCP_Server: 192.168.10.10
• Name: Ventas
VLAN 12 Network (10.0.10.0/24):
• Windows1: 10.0.10.10
• Name: IT
VLAN 13 Network (10.1.10.0/24):
• Name: Admin_Equipos
VLAN 18 Network (192.168.11.0/28):
Notes
• LSW5 and LSW6 are connected to the same end devices, this means there is only one dhcp server and so on
