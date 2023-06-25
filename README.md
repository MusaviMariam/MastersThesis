# MastersThesis
A proof-of-concept implementation of Route Selection on Clustered Cognitive Radio Networks (CRNs) on USRP N200/ GNU Radio. 
In CRNs, secondary users (SU) explore and exploit the spectrum in the absence of primary users (PUs). 
The SU nodes in the topology are static and divided into three main classes source node, intermediate node, and destination node. 

Thesis title: Route Selection over Clustered Cognitive Radio Networks: An Experimental Evaluation

Author: Mariam Musavi 

Abstract: Cognitive radio (CR) is the next-generation wireless communication system that allows unlicensed users (or secondary users, SUs) to explore and exploit the
underutilized licensed spectrum (or white spaces) owned by licensed users (or primary users, PUs) in an opportunistic manner. This paper proposes a route
selection scheme over a clustered cognitive radio network (CRN) that enables SUs to form clusters, and a SU source node to search for a route to its destination
node. An intrinsic characteristic of CRN is the dynamicity of operating the environment in which network conditions (i.e., PUs' activities) change as time
goes by. Based on the network conditions, SUs form clusters whose cluster sizes are based on the number of available common channels in a cluster, select
a common operating channel for each cluster, and search for a route over a clustered CRN using an artificial intelligence approach called reinforcement
learning. The majority of the research related to CRNs has been limited to theoretical and simulation studies, and testbed investigation focusing on physical and
data link layers. This investigation is a proof of concept focusing on the network the layer of a route selection scheme over a clustered CRN in a universal software radio peripheral (USRP)/ GNU radio platform. 
Experimental results show that the proposed route selection scheme improves cluster stability by reducing the number of route breakages caused by route switches, and network scalability by
reducing the number of clusters in the network without significant deterioration of quality of service, including throughput, packet delivery rate, and end-to-end
delay.

