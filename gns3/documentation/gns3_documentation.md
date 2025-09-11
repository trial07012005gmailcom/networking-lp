Network Topology Documentation: pf-1
Overview
This document describes the network topology defined in the GNS3 project "pf-1". The topology consists of Cisco routers, multilayer switches, virtual PCs, and cloud nodes representing external servers, interconnected via Ethernet and UDP tunnel links.
Devices
The topology includes the following devices:

Routers (7):
R1, R2, R3, R4, R5, R6, ISP
Model: Cisco 7200 (Dynamips, c7200 platform, IOS image: c7200-advipservicesk9-mz.152-4.M6)
Configuration: 512 MB RAM, 512 MB NVRAM, NPE-400, C7200-IO-FE in slot0, PA-2FE-TX in slots 1-4

Switches (6):
SW-1, SW-2, SW-3, SW-4, SW-5, SW-6
Model: QEMU-based multilayer switch (vios_l2-adventerprisek9-m.SSA.high_iron_20180619.qcow2)
Configuration: 768 MB RAM, 16 adapters (e1000), virtio disk interface

Virtual PCs (2):
PC1, PC2
Model: VPCS

Cloud Nodes (6):
ARHuawei, DNS_Web, DHCP_Server, WindowsServer, PBX, Windows1, Windows2
Type: Cloud nodes with Ethernet and UDP tunnel interfaces

Connections
The topology includes the following connections:
Router-to-Router Connections

ISP (f0/0) <-> R3 (f0/0): Ethernet link
ISP (f1/0) <-> R4 (f0/0): Ethernet link
ISP (f2/0) <-> R6 (f0/0): Ethernet link
ISP (f3/0) <-> R5 (f0/0): Ethernet link
R1 (f0/0) <-> R2 (f0/0): Ethernet link
R1 (f1/0) <-> R3 (f1/0): Ethernet link
R2 (f1/0) <-> R3 (f2/0): Ethernet link
R2 (f2/0) <-> R4 (f1/0): Ethernet link
R2 (f3/0) <-> ARHuawei (UDP tunnel 1): UDP tunnel (local port: 35005, remote: 127.0.0.1:25005)

Router-to-Switch Connections

R5 (f1/0) <-> SW-1 (Gi0/0): Ethernet link
R6 (f1/0) <-> SW-2 (Gi0/0): Ethernet link

Switch-to-Switch Connections

SW-1 (Gi0/1) <-> SW-2 (Gi0/1): Ethernet link
SW-1 (Gi0/2) <-> SW-3 (Gi0/0): Ethernet link
SW-1 (Gi0/3) <-> SW-4 (Gi0/0): Ethernet link
SW-1 (Gi1/0) <-> SW-5 (Gi0/0): Ethernet link
SW-1 (Gi1/1) <-> SW-6 (Gi0/0): Ethernet link
SW-2 (Gi0/2) <-> SW-3 (Gi0/1): Ethernet link
SW-2 (Gi0/3) <-> SW-4 (Gi0/1): Ethernet link
SW-2 (Gi1/0) <-> SW-5 (Gi0/1): Ethernet link
SW-2 (Gi1/1) <-> SW-6 (Gi0/1): Ethernet link
SW-3 (Gi0/2) <-> Windows1 (UDP tunnel 1): UDP tunnel (local port: 33000, remote: 127.0.0.1:23000)
SW-4 (Gi0/2) <-> Windows2 (UDP tunnel 1): UDP tunnel (local port: 33010, remote: 127.0.0.1:23010)
SW-5 (Gi0/2) <-> DNS_Web (UDP tunnel 1): UDP tunnel (local port: 33020, remote: 127.0.0.1:23020)
SW-5 (Gi0/3) <-> DHCP_Server (UDP tunnel 1): UDP tunnel (local port: 33030, remote: 127.0.0.1:23030)
SW-5 (Gi1/0) <-> WindowsServer (UDP tunnel 1): UDP tunnel (local port: 33040, remote: 127.0.0.1:23040)
SW-5 (Gi1/1) <-> PBX (UDP tunnel 1): UDP tunnel (local port: 33050, remote: 127.0.0.1:23050)
SW-6 (Gi0/2) <-> DNS_Web (UDP tunnel 2): UDP tunnel (local port: 34020, remote: 127.0.0.1:34020)
SW-6 (Gi0/3) <-> DHCP_Server (UDP tunnel 2): UDP tunnel (local port: 34030, remote: 127.0.0.1:24030)
SW-6 (Gi1/0) <-> WindowsServer (UDP tunnel 2): UDP tunnel (local port: 34040, remote: 127.0.0.1:24040)
SW-6 (Gi1/1) <-> PBX (UDP tunnel 2): UDP tunnel (local port: 34050, remote: 127.0.0.1:24050)

Switch-to-PC Connections

SW-3 (Gi0/3) <-> PC1 (e0): Ethernet link
SW-4 (Gi0/2) <-> PC2 (e0): Ethernet link

Additional Notes

Compute Environment: Devices are hosted on a local compute node and a remote GNS3 server (192.168.70.102:80).
Console Access: Routers, switches, and VPCS devices use Telnet for console access (ports 60009-60017 for routers, 5031-5041 for switches, 60012-60014 for VPCS). Cloud nodes have no console configured.
Topology Settings: Grid size 75, drawing grid size 25, scene dimensions 2000x1000, zoom level 60%.
