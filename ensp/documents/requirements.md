# Enterprise Network Design Requirements Documentation

## DESIGN OVERVIEW

### Network Architecture

- **Topology**: Hierarchical three-layer design (Core/Distribution/Access)
- **Platform**: Huawei eNSP with Cisco GNS3 integration
- **Scope**: Multi-VLAN enterprise network with WAN connectivity and high availability

### Physical Infrastructure

- **Core Layer**: 6 routers (ISP, AR1-4, Router1-2)
- **Distribution/Access Layer**: 4 switches (LSW1-4)
- **End Devices**: Servers (DHCP, DNS, PBX), workstations (PC1, Windows1)
- **External**: Cisco R4 cloud connection

## NETWORK SEGMENTATION DESIGN

### VLAN Structure

| VLAN ID | Network         | Purpose        | SVI LSW1     | SVI LSW2     | VRRP VIP (Gateway) |
| ------- | --------------- | -------------- | ------------ | ------------ | ------------------ |
| 10      | 172.16.10.0/24  | VoIP           | 172.16.10.2  | 172.16.10.3  | 172.16.10.1        |
| 11      | 192.168.10.0/24 | Ventas (Sales) | 192.168.10.2 | 192.168.10.3 | 192.168.10.1       |
| 12      | 10.0.10.0/24    | IT             | 10.0.10.2    | 10.0.10.3    | 10.0.10.1          |
| 13      | 10.1.10.0/24    | Admin_Equipos  | 10.1.10.2    | 10.1.10.3    | 10.1.10.1          |
| 18      | 192.168.11.0/28 | Unspecified    | 192.168.11.2 | 192.168.11.3 | 192.168.11.1       |

### WAN Interconnections (/30 Point-to-Point Networks)

- **156.0.10.0/30**: AR3 ↔ ISP
- **156.0.10.4/30**: AR4 ↔ ISP
- **156.0.10.8/30**: AR1 ↔ AR4
- **156.0.10.12/30**: AR2 ↔ AR4
- **156.0.10.16/30**: AR2 ↔ AR3
- **156.0.10.20/30**: AR1 ↔ AR2
- **192.10.6.0/30**: AR1 ↔ R4 Cisco
- **177.0.10.0/28**: ISP ↔ Router1
- **144.0.10.0/28**: ISP ↔ Router2

## CONFIGURATION REQUIREMENTS

### 1. SWITCHING CONFIGURATION

#### Trunk Configuration

- **Requirement**: All inter-switch links as static trunks
- **Standard**: 802.1Q encapsulation
- **VLAN Allowed**: All VLANs on all trunks
- **Switches**: LSW1, LSW2, LSW3, LSW4

#### VLAN Assignment

- **Access Ports**: Assign per topology specifications
- **VLAN Creation**: Create VLANs 10, 11, 12, 13, 18 on all switches

### 2. SPANNING TREE PROTOCOL (MSTP)

#### Instance Configuration

- **Protocol**: Change from PVSTP to MSTP
- **Instance 1**: VLANs 10, 11
  - Root Bridge: LSW1 (SW1)
  - Backup Bridge: LSW2 (SW2)
- **Instance 2**: VLANs 12, 13
  - Root Bridge: LSW2 (SW2)
  - Backup Bridge: LSW1 (SW1)

### 3. LAYER 3 SWITCHING (SVI)

#### SVI Implementation

- **Switches**: LSW1 (SW1), LSW2 (SW2) as Layer 3 switches
- **IP Addressing**: Use 2nd and 3rd IP from each subnet
- **VLANs**: Create SVI for all active VLANs (10, 11, 12, 13, 18)

### 4. HIGH AVAILABILITY (VRRP)

#### VRRP Groups

- **Requirement**: One VRRP group per VLAN
- **Purpose**: Default gateway redundancy
- **Implementation**:
  - Configure on both SW1 and SW2 SVI interfaces
  - Router1 and Router2: Dual IP configuration for VRRP
- **Objective**: Maintain internet access during single device failure

### 5. SERVER REDUNDANCY

#### Mikrotik Virtual Machine

- **Platform**: Mikrotik RouterOS VM
- **NIC Configuration**: Active-backup bond (2 interfaces)
- **Connections**: Dual links to datacenter switches (LSW1, LSW2)

### 6. DHCP SERVICES

#### DHCP Server Configuration

- **Platform**: Mikrotik router
- **Pools**: Create for all VLANs (10, 11, 12, 13, 18)
- **DHCP Relay**: Configure on all SVI interfaces

### 7. ROUTING CONFIGURATION

#### Default Routes

- **Layer 3 Switches**: SW1, SW2 default routes to Router1, Router2
- **Edge Routers**: Router1, Router2 default routes to ISP

#### Static Routes

- **Return Traffic**: Router1, Router2 static routes to VLAN networks
- **Destination**: All VLAN subnets via SW1/SW2

### 8. NETWORK ADDRESS TRANSLATION

#### PAT Configuration

- **Routers**: Router1, Router2
- **Scope**: All VLAN traffic
- **Method**: Port Address Translation (PAT)

### 9. WAN ROUTING PROTOCOL

#### OSPF Implementation

- **Protocol**: Open Shortest Path First (OSPF)
- **Scope**: All WAN routers (AR1-4, ISP, Router1-2)
- **Purpose**: Dynamic learning of public networks
- **Integration**: Huawei-Cisco OSPF interoperability

### 10. DNS SERVICES

#### BIND DNS Server

- **Platform**: Linux with BIND9
- **Domain Structure**: domain.subdomain.com
- **Records**: DNS server A record, PBX A record
- **Resolution**: Local domain resolution

### 11. PBX SYSTEM

#### Issabel PBX Configuration

- **Platform**: Issabel PBX
- **Extensions**: XX format for eNSP, XX format for GNS3
- **Softphones**: Windows 7 clients registration
- **Inter-PBX**: IAX trunk between eNSP and GNS3 PBX systems

#### VoIP Network Integration

- **VPN Connection**: Point-to-point between Router1 (eNSP) and R5 (GNS3)
- **Traffic**: VoIP VLAN 10 routing through VPN tunnel
- **Static Routes**: Configure for PBX-to-PBX communication

## VALIDATION REQUIREMENTS

### Connectivity Tests

1. **Inter-VLAN Communication**: Ping between different VLAN hosts
2. **WAN Connectivity**: Ping public addresses (GNS3 ↔ eNSP)
3. **Web Access**: Access GNS3 web server from eNSP Windows 7
4. **OSPF Convergence**: Public network advertisement between Cisco/Huawei domains

### High Availability Tests

1. **Failover Testing**: Maintain internet access during router/switch failure
2. **Continuous Connectivity**: Sustained ping to Cisco public addresses during failover

### Application Services Tests

1. **VoIP Registration**: Windows 7 softphone registration with PBX
2. **Inter-PBX Calling**: Call routing through IAX trunk
3. **DNS Resolution**: Verify configured DNS records resolution

## CRITICAL IMPLEMENTATION NOTES

### IP Addressing Scheme

- **SVI Gateways**: Use .2 and .3 addresses from each VLAN subnet
- **VRRP VIPs**: Use .1 address as virtual gateway
- **WAN Addressing**: Follow /30 and /28 subnet specifications

### Redundancy Design

- **No Single Point of Failure**: Dual paths for all critical services
- **Load Distribution**: MSTP load balancing across switch instances
- **Service Availability**: VRRP, dual WAN connections, server bonding

### Integration Requirements

- **Platform Interoperability**: Huawei eNSP ↔ Cisco GNS3
- **Protocol Compatibility**: OSPF, STP, VRRP standard compliance
- **Service Integration**: PBX trunk, DNS resolution, web services

## DELIVERABLES CHECKLIST

### Configuration Files

- [ ] Switch configurations (VLAN, trunk, MSTP, SVI)
- [ ] Router configurations (OSPF, NAT, static routes)
- [ ] VRRP configurations
- [ ] DHCP server pools and relay configurations

### Service Configurations

- [ ] Mikrotik server setup and bonding
- [ ] BIND DNS with domain records
- [ ] Issabel PBX with extensions and IAX trunk
- [ ] VPN tunnel configuration

### Validation Results

- [ ] Connectivity test results matrix
- [ ] Failover test documentation
- [ ] Service functionality verification
- [ ] Performance baseline measurements
