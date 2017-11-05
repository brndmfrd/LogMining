'''
This program is intended to be ran stand-alone
The program will run with an increasing K value that stands for the number of classifiers (cluster 
    heads) we are using on our static data set of 100.  
The maximum size of our two dimentional graph, for which we place all of our datapoints, will 
    stay size 25x25

For each run (each with a differnet amount of cluster heads) the program will calculate an appropriate 
    median value for which the datapoints will be classified, as per the kmeans algorithm.  
    The output of this program will be the following:
    1) list of data points and their respective cluster (colred) (list and graph)
    2) cluster head points (list) and what points they connect to for the 'backbone network'
    3) the workload of each cluster head/center calulated by the sum of:
        - intercluster comm: each cluster node with each other node of the same cluster
        - intracluster comm: each cluster node with each other node of all other cluster nodes
        - door-man comm: each outside cluster node using another node as a stepping stone. 

Our table is the adjacency matrix for all connected cluster heads' distance between each other.

The frequency of communication among pair of points (i,j) is f(i,j) = floor (abs(i-j))/2 for 0<i,j<M+1.

The transmission distance of a center point is D = sqr (2)N/2, therefore any two center points that  are In distance  
less than or equal to D should be connected and form a 'backbone network'.

We use Dijkstra's algo for shortest path between all cluster heads
'''
import matplotlib.pyplot as plt
from scipy.cluster.vq import *
import numpy
import pylab as pl
import numpy as np
import math
import networkx as nx


def setup(datapoints, nClusterHeads, maxGridsize):
	'''
	This method runs the kmeans algorithm and establishes
	the location of the cluster heads and outputs the 
	graph of the cluster distrobution.
	'''
	res, idx = kmeans2(datapoints, nClusterHeads)
	
	# create the backbone network from the cHeads
	# am is our adjacency matrix of distances of each cHead
	am = buildBackbone(res, maxGridsize)	

	# calculate the work of the cluster heads
	workDone = calcAllConnections(am, datapoints, idx, nClusterHeads)
	
	color_array = np.random.random((nClusterHeads,3))
	colors = ([color_array[i] for i in idx])
	pl.scatter(datapoints[:,0],datapoints[:,1],c=colors)
	pl.scatter(res[:,0],res[:,1], marker='o', s = 100, linewidths=2, c='none')
	pl.scatter(res[:,0],res[:,1], marker='x', s = 100, linewidths=2)

	savename = str(nClusterHeads) + 'Graph.png'
	pl.savefig(savename)
	#pl.show()	
	pl.close()
	
	return workDone, am

def buildBackbone(R, N):
	'''
	R := list of cluster (x,y) pos
	N := max size of our grid (ie 25)
	Determine what cluster heads are connected 
	to each other and return a matrix of the 
	distances	
	
	connected => R[i] - R[j] <= N/sqrt(2) 
	am := adjacency matrix; pos=0 if no connection.
	'''
	am = np.zeros((len(R),len(R)))		# empty RxR maxrix
	limit = float(N) / math.sqrt(2)		# cast as float, ensure no rounding
	
	for i in xrange(len(R)):
		for j in xrange(len(R)):
			# sqrt( (x1-x2)^2 + (y1-y2)^2 ) 
			dist = math.pow((R[i,0] - R[j,0]),2) + math.pow((R[i,1] - R[j,1]),2) 
			dist = math.sqrt(dist)
			if dist <= limit:
				am[i,j] = dist
	
	return am


def calcAllConnections(am, datapoints, idx, nClusterHeads):
	'''
	This method takes into account each node communicating with each 
	other node wether it be inter-cluster, intra-cluster, or 
	work the cHead needs to do to pass a message between two other 
	cluster nodes.  
	
	We calculate the shortest path traversal for each node with dijkstra's 
	single shortest path algorithm for each node to each node and tally up 
	the amount of times each cHead is effected multiplied by the freq of 
	communication between the two nodes that are communicating.  
	'''
	
	# index of each cHead, we tally the use of each in here
	comCost = np.zeros(nClusterHeads)
	G = nx.from_numpy_matrix(am)	

	for i in xrange(len(datapoints)-1):
		for j in xrange(i+1, len(datapoints)):
			if idx[i] == idx[j]:
				comCost[idx[i]] += 1*(abs(float(i) - float(j)))/2.0
			else:
				targets = (nx.dijkstra_path(G,idx[i],idx[j]))
				for t in targets:
					comCost[t] += 1*(abs(float(i) - float(j)))/2.0
	return comCost


if __name__ == '__main__':    
	#K = [3] # small for testing purposes
	K = [3,4,6,8,10,12,13,16,18,20,22,24,25,30]
	N = 25      # length of square plane for our datapoints
	M = 100     # num of datapoints we will be classifying
	allTheWorkDone = []

	np.set_printoptions(precision=1,linewidth=184)

	datapoints = np.random.randint(N, size=(M,2))       # M datapoints (x,y) < (N,N)
	print '---------Our datapoints----------'
	print datapoints

	for k in K:
		work, distMatrix = setup(datapoints, k, N)
		allTheWorkDone.append(sum(work))

		print '---------- For ' + str(k) + ' clusters ----------'
		print 'Work done for each cluster heads:  '
		print work
		
		print 'Sum of work done for all cluster heads: '
		print sum(work)
		
		print 'Distance matrix:'
		
		for d in distMatrix:
			print d
		'''
		for i in xrange(len(distMatrix)):
			print(distMatrix[i])
		'''
		print ''


	plt.plot(K,allTheWorkDone)
	savename = 'Workload ' + 'Graph.png'
	plt.savefig(savename)
	#plt.show()
	plt.close()
