# GNS3 Network Topology Project

This project contains the configuration files and helper scripts for a comprehensive network topology built in GNS3. It was developed for the "Aplicaciones con Redes" course.

The network simulates a corporate environment with multiple departments, implementing redundancy, dynamic routing, and secure access to the internet.

## Network Topology Overview

The topology is designed with a hierarchical approach, featuring core, distribution/access, and edge layers.

- **Core/Distribution Layer:** Comprised of two multilayer switches, `ESW1` and `EWS2`. They handle inter-VLAN routing and provide high availability for default gateways using the Hot Standby Router Protocol (HSRP). They also act as VTP servers for the network.

- **Access Layer:** Includes four switches (`ESW3`, `ESW4`, `ESW5`, `ESW6`) that provide network access to end-user devices across different VLANs. These are configured as VTP clients.

- **Edge/WAN Layer:** A redundant setup involving routers `R1` and `R2` which perform Network Address Translation (NAT) and connect to a simulated internet backbone.

- **Backbone:** Routers `R3`, `R4`, `R5`, `R6`, and `ISP` form a backbone running OSPF to simulate connections to and within the Internet Service Provider's network.

## Key Features Implemented

- **VLANs & VTP:** The network is segmented into several VLANs for different departments:

  - `VLAN 10`: Gerencia (`10.0.10.0/24`)
  - `VLAN 11`: Administración (`192.168.10.0/24`)
  - `VLAN 12`: VoIP (`172.16.10.0/24`)
  - `VLAN 13`: IT (`10.1.10.0/24`)
  - `VLAN 15`: Admin_Equipos (`172.1.10.0/24`)
  - VLAN Trunking Protocol (VTP) is used to manage VLANs centrally from `ESW1` and `ESW2`.

- **Spanning Tree Protocol (STP):** Per-VLAN Spanning Tree (PVST) is configured. STP priorities are adjusted on the core switches to load-balance traffic, making `ESW1` the root bridge for some VLANs and `ESW2` the root for others.

- **Inter-VLAN Routing:** Handled by the core multilayer switches (`ESW1`, `ESW2`).

- **First-Hop Redundancy (FHRP):** HSRP is configured on the core switches for all major VLANs, providing a resilient default gateway for end devices.

- **Dynamic Routing:** OSPF (single-area) is the primary IGP, enabling dynamic route discovery between all routers in the topology.

- **Network Address Translation (NAT):** Routers `R1` and `R2` use PAT (overload) to translate private internal IP addresses to a public IP address for internet access. Static NAT is also configured for specific internal services.

- **Access Control Lists (ACLs):** Standard and extended ACLs are used to filter traffic, notably to restrict access to the `Admin_Equipos` VLAN (VLAN 15) to only allow traffic from the IT department.

- **Device Security:** Basic security measures are in place, including `enable secret`, local user accounts, and SSH access for VTY lines on the switches.

## Project File Structure

```
pf/
├── gns3/
│   └── confs/
│       ├── ESW1.cfg
│       ├── R1.cfg
│       └── ... (all other individual device configs)
│
├── all_gns3_configs.txt    # All config files concatenated into one file.
├── textification.py        # Python script to generate all_gns3_configs.txt.
├── prompts.md              # Example prompts for AI-assisted network tasks.
└── README.md               # This file.
```

- `gns3/confs/`: This directory contains the individual configuration files for each device in the GNS3 topology.
- `all_gns3_configs.txt`: An aggregated text file containing all device configurations, separated by headers. This is useful for a quick overview or for providing context to language models.
- `textification.py`: A Python script that recursively finds all `.cfg`, `.txt`, and `.conf` files in the `gns3/confs` directory and combines them into `all_gns3_configs.txt`.
- `prompts.md`: A markdown file containing sample prompts that can be used with an AI assistant (like Gemini or Claude) to perform tasks like generating documentation from the configurations or creating new command sets.

## How to Use

### Prerequisites

- GNS3
- Cisco IOS images for routers (e.g., c7200) and switches (e.g., L2/L3 IOU or vIOS). The configurations use `version 12.4` for switches and `version 15.2` for routers.
- Python 3.x to run the helper script.

### Loading Configurations

1.  Build the network topology in GNS3 according to the connections implied by the configuration files.
2.  For each device in GNS3, you can copy and paste the corresponding configuration from the `gns3/confs/` directory into its console.

### Aggregating Configurations

If you make changes to the individual `.cfg` files, you can update the `all_gns3_configs.txt` file by running the `textification.py` script.

1.  **Modify the script (if needed):** Open `textification.py` and ensure the `SOURCE_DIR` and `OUTPUT_DIR` variables point to the correct locations.

    ```python
    # 🔧 Change these variables as needed
    SOURCE_DIR = r"D:\Education\UPB\Courses\APLICACIONES CON REDES\TP\pf\gns3\confs"
    OUTPUT_DIR = r"D:\Education\UPB\Courses\APLICACIONES CON REDES\TP\pf"
    OUTPUT_FILE = "all_gns3_configs.txt"
    EXTENSIONS = [".cfg", ".txt", ".conf"]
    ```

2.  **Run the script:**

    ```bash
    python textification.py
    ```

    This will generate or overwrite the `all_gns3_configs.txt` file in the project's root directory.
