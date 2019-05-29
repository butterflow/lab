def dijkastra(start):
	global n,graph
	Q=[[0,start]]
	d=[999 for i in range(n)]
	d[start]=0
	while Q:
		Q.sort()
		[l,u]=Q.pop(0)
		for v in range(n):
			if d[v]>d[u]+graph[u][v]:
				d[v]=d[u]+graph[u][v]
				Q.append([d[v],v])
	return d
n=int(input("Enter number of nodes in graph:"))
graph=[[]for i in range(n)]
for i in range(n):
	for j in range(n):
		print("Enter weight b/w nodes",i+1,"and",j+1)
		val=int(input())
		graph[i].append(val)
s=int(input("Enter source node:"))
d=dijkastra(s-1)
print("---MINIMUM COST PATH---")
print("EDGE     :COST")
for i in range(n):
	print(s,"--->",i+1,":",d[i])
