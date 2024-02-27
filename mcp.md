 Rogue Endpoint Detection

 About the Rogue Endpoint Control Policy
Rogue endpoints pose a significant threat to leaf switches by frequently injecting packets through various leaf switch ports and altering 802.1Q tags, mimicking endpoint movements. This can cause alterations in learned classes and EPG port configurations, often a result of misconfigurations leading to frequent IP and MAC address changes.

 Key Challenges:
- Causes network instability and high CPU usage.
- Can lead to crashes of endpoint mapper (EPM) and EPM client (EPMC) due to excessive messaging and transaction service (MTS) buffer usage.
- Rapid log turnover, complicating debugging efforts for unrelated endpoints.

 Rogue Endpoint Control Feature
This feature aims to mitigate the aforementioned issues by:
- Identifying rapidly moving MAC and IP endpoints.
- Quarantining the endpoint by temporarily making it static to halt its movement.
- Deleting the unauthorized MAC or IP address after the Rogue EP Detection Interval:
  - Before 3.2(6) Release: Traffic to and from the rogue endpoint is dropped during this interval.
  - 3.2(6) Release and Later: The feature no longer drops traffic but still deletes the unauthorized addresses post-interval.
- Generating a host tracking packet to re-learn affected MAC or IP addresses.
- Raising a fault for corrective action.

 Policy Configuration
- Configured globally, impacting individual endpoints (IP and MAC addresses) without distinguishing between local or remote moves. Any interface change is treated as a movement for the purpose of determining potential quarantine actions.
- By default, the rogue endpoint control feature is disabled, requiring manual activation to employ its protective measures.



 Loop Detection in Cisco ACI

Cisco Application Centric Infrastructure (ACI) implements several measures to detect and mitigate loop formations within the network fabric, primarily focusing on Layer 2 network segments connected to Cisco ACI access ports.

 Global Default Loop Detection Policies
- Default State: Disabled at the global level but enabled by default at the port level.
- Effect of Enabling Global Policies: Applies loop detection to all access ports, virtual ports, and virtual port channels (VPCs), unless disabled at a specific port level.

 Mis-Cabling Protocol (MCP)
- Role: Detects loops within the ACI fabric, functioning alongside the Spanning Tree Protocol (STP) operating on external Layer 2 networks.
- Operation: Does not rely on STP. Utilizes MCP for loop detection within the fabric.
- Configuration: Administrators can set MCP to identify loops and dictate the response, which can be logging (syslog) or disabling the affected port.

 Notes on MCP and External Connectivity
- External STP Interaction: Interfaces connecting to external switches running STP may enter a `loop_inc` status. Resolving this involves flapping the port-channel or adjusting BDPU filter and loop guard settings on the external switch.
- VLAN Mode: MCP operates in native VLAN mode by default, sending untagged BPDUs. However, starting from release 2.0(2), MCP has been enhanced to send BPDUs across all VLANs configured in EPGs, improving loop detection capabilities.

 Enhancements and Fault Management
- Enhanced Loop Detection: From release 3.2(1), ACI fabric offers faster loop detection, with frequencies ranging from 100 milliseconds to 300 seconds.
- Fault Generation: Releases 5.2(3) and later generate specific faults if the number of operational VLANs per interface exceeds 256 (fault F4268) or if more than 2000 logical ports are active per leaf switch (fault F4269).

 Limitations
- VLAN Limitation: MCP's per-VLAN operation is capped at 256 VLANs per interface, prioritizing the first numerical 256 VLANs for loop detection.
- FEX Support: MCP does not support operation on fabric extender (FEX) host interface (HIF) ports.

This structured approach delineates the mechanisms Cisco ACI employs for loop detection and the administrative configurations available to manage and mitigate network loops effectively.

