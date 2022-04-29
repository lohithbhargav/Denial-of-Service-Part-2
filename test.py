"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):

	def build( self ):

		with open('routers_data_undirected.txt') as f:
			lines = f.readlines()
		# connection = []
		routers = {}
		servers = {}
		clients = {}
		nodeIdSet = set()
		for line in lines:
			sourceNodeID = int(line.split("\t")[0])
			targetNodeID = int(line.split("\t")[1])
			if sourceNodeID >=800  and sourceNodeID <= 850:
				
				if sourceNodeID not in nodeIdSet:
						nodeIdSet.add(sourceNodeID)
						servers[sourceNodeID] = self.addHost('s'+str(sourceNodeID))
						clients[sourceNodeID] = self.addHost('c'+str(sourceNodeID))
						routers[sourceNodeID] = self.addSwitch('r'+str(sourceNodeID))
						nodeIdSet.add(sourceNodeID)

						self.addLink(clients[sourceNodeID], routers[sourceNodeID])
						self.addLink(routers[sourceNodeID], servers[sourceNodeID])
		
				if targetNodeID >= 800 and targetNodeID <= 850:
					# connection.append((sourceNodeID, targetNodeID))
					
					servers[targetNodeID] = self.addHost('s'+str(targetNodeID))
					clients[targetNodeID] = self.addHost('c'+str(targetNodeID))
					routers[targetNodeID] = self.addSwitch('r'+str(targetNodeID))
					nodeIdSet.add(targetNodeID)
					
					self.addLink(clients[targetNodeID], routers[targetNodeID])
					self.addLink(routers[targetNodeID], servers[targetNodeID])
					self.addLink(routers[sourceNodeID], routers[targetNodeID])
					

			if sourceNodeID > 851:
				break

        

topos = { 'mytopo': ( lambda: MyTopo() ) }

