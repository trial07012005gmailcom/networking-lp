# Enterprise Network Design Requirements Documentation

## Executive Summary

This document outlines the comprehensive requirements for implementing a highly available enterprise network infrastructure featuring redundant routing, VLAN segmentation, server virtualization, and voice integration across GNS3 and eSNP platforms.

## Network Design Architecture

### Core Infrastructure

- **Primary Routers**: R1, R2 (HSRP-enabled for gateway redundancy)
- **Layer 3 Switches**: SW1, SW2 (Distribution layer with SVI interfaces)
- **Access Switches**: SW3, SW4, SW5 (Client VTP mode)
- **WAN Connectivity**: Full OSPF mesh with ISP router integration

### High Availability Design

- **Router Redundancy**: HSRP configuration on R1/R2 for all VLANs
- **Switch Redundancy**: SW1/SW2 as VTP servers with PVST load balancing
- **Server Redundancy**: Active-backup NIC teaming across datacenter switches
- **Link Redundancy**: 802.1Q trunks with static configuration

## Critical Implementation Requirements

### 1. VTP Configuration

**Domain**: cisco.com  
**Password**: cisco  
**VTP Servers**: SW1, SW2  
**VTP Clients**: SW3, SW4, SW5

### 2. VLAN Implementation

| VLAN ID | Network         | Purpose        | Root Bridge | Backup Bridge |
| ------- | --------------- | -------------- | ----------- | ------------- |
| 10      | 10.0.10.0/24    | Gerencia       | SW1         | SW2           |
| 11      | 192.168.10.0/24 | Administración | SW1         | SW2           |
| 12      | 172.16.10.0/24  | VoIP           | SW1         | SW2           |
| 13      | 10.1.10.0/24    | IT             | SW2         | SW1           |
| 15      | 172.1.10.0/24   | Admin_Equipos  | SW2         | SW1           |

### 3. SVI Configuration

**SW1 Interfaces**: Use 2nd IP of each subnet  
**SW2 Interfaces**: Use 3rd IP of each subnet  
**DHCP Relay**: Configure on all SVI interfaces

### 4. HSRP Implementation

- **Gateway Groups**: One per VLAN
- **Virtual IPs**: 1st usable IP of each subnet
- **Priority**: Configure based on PVST root bridge alignment
- **Router Configuration**: Dual IP addressing for redundancy

### 5. Security Implementation

**Access Control**:

- Extended ACL blocking all networks except VLAN 13 from accessing VLAN 15
- SSH configuration on VTY lines with username/password authentication

**Network Segmentation**:

- Static IP assignment for server and management VLANs (13, 15)
- DHCP pools for user VLANs (10, 11, 12)

### 6. Service Infrastructure

#### DHCP Services

**Platform**: MikroTik Router  
**Scope**: All user VLANs (exclude server/management VLANs)  
**Reservations**: MAC-to-IP binding per network scheme

#### DNS Services

**Platform**: Debian 12 with BIND  
**Configuration**: Authoritative local DNS with views and ACLs  
**Domain**: dominio.com  
**Records Required**:

- A records for DNS, web (www + FQDN), PBX servers
- Public and private DNS zones

#### Web Services

**Platform**: NGINX on Debian  
**Configuration**: Enterprise website hosting

#### Directory Services

**Platform**: Windows Server  
**Configuration**: Active Directory with Windows 7 client integration

#### Voice Services

**Platform**: Issabel PBX  
**Integration**: Softphone registration on Windows 7 clients  
**Connectivity**: IAX trunk between GNS3 and eSNP PBX systems

### 7. WAN and Internet Connectivity

#### NAT Configuration

**Static NAT**: Web server (port 80), DNS server (port 53)  
**PAT**: All VLAN networks on both R1 and R2  
**Redundancy**: Duplicate configuration across both routers

#### OSPF Implementation

**Scope**: All WAN routers  
**Public IPs**: Include 8.8.8.8, 8.8.4.4 simulation  
**Integration**: Cross-platform OSPF (Cisco-Huawei)

#### Default Routing

**Layer 3 Switches**: Default routes pointing to HSRP virtual IPs  
**Routers**: Default routes to ISP  
**Return Routes**: Static routes for VLAN networks

## Server Virtualization Requirements

### Network Interface Configuration

**All Servers**: Dual NIC active-backup configuration  
**Connection**: Primary to SW5, backup to SW6  
**Platforms**:

- Windows Server (Active Directory)
- Debian 12 (DNS/Web services)
- Issabel PBX (Voice services)
- MikroTik (DHCP services)

## Inter-Platform Integration

### VoIP Connectivity

**Requirement**: Point-to-point link between eSNP Router 1 and GNS3 R5  
**Protocol**: Static routing for VoIP traffic  
**Trunk**: IAX configuration for inter-PBX calling  
**Numbering**: eSNP PBX uses XXX format, GNS3 PBX uses XXX format

## Validation and Testing Requirements

### Connectivity Testing

- [ ] Inter-VLAN communication via HSRP gateways
- [ ] Public IP connectivity (GNS3 ↔ eSNP)
- [ ] DNS resolution from Windows 7 clients
- [ ] Web server access from user workstations
- [ ] OSPF route propagation (Cisco-Huawei)

### Redundancy Testing

- [ ] Router failover (HSRP functionality)
- [ ] Switch failover (maintain connectivity during outages)
- [ ] Server NIC failover (active-backup switching)
- [ ] Continuous internet connectivity during component failures

### Service Testing

- [ ] Intra-PBX calling (same system)
- [ ] Inter-PBX calling (GNS3 ↔ eSNP via IAX trunk)
- [ ] DHCP lease assignment and renewal
- [ ] Active Directory authentication and domain join

## Critical Success Factors

1. **High Availability**: Zero single points of failure in core infrastructure
2. **Security**: Proper VLAN isolation and access control implementation
3. **Scalability**: Modular design supporting future expansion
4. **Integration**: Seamless cross-platform communication (GNS3/eSNP)
5. **Service Continuity**: All services maintain operation during planned/unplanned outages

## Implementation Priorities

**Phase 1**: Core infrastructure (VTP, VLANs, trunking, PVST)  
**Phase 2**: Routing and gateway services (HSRP, SVIs, default routes)  
**Phase 3**: Server services (DHCP, DNS, Web, AD)  
**Phase 4**: Security implementation (ACLs, SSH, user authentication)  
**Phase 5**: Voice integration and cross-platform connectivity  
**Phase 6**: Comprehensive testing and validation
