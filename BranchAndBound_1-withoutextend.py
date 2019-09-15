##取已走距离最小的在前端
##加上已经过距离限制

from Joint import *
import copy
import matplotlib.pyplot as plt

## 用于设置最大循环深度
# import sys   
# sys.setrecursionlimit(100000)

def quick_sort(targat_list, fellow_list, first, last):
	"""快速排序"""
	if first >= last:
		return
	mid_value = targat_list[first]
	mid_value_fellow_list = fellow_list[first]
	low = first
	high = last
	while low < high:
		while low < high and targat_list[high] >= mid_value:
			high -= 1
		targat_list[low] = targat_list[high]
		fellow_list[low] = fellow_list[high]
		while low < high and targat_list[low] < mid_value:
			low += 1
		targat_list[high] = targat_list[low]
		fellow_list[high] = fellow_list[low]
	targat_list[low] = mid_value
	fellow_list[low] = mid_value_fellow_list
	quick_sort(targat_list, fellow_list, first, low-1)
	quick_sort(targat_list, fellow_list, low+1, last)


def BAB(joint, start_point, end_point):
	"""
	功能：实现找到最短路径的算法
	循环：
	创建一个path_queue用于存放所有已经发现的路径
	创建一个distance-queue用于存放path-queue中对应的已经走过的距离
	每次选取distance-queue 中最小的那个，并取得其索引，作为path_queue中要扩展路径的对象
	删除path_queue中要扩展的元素，以及distance-queue中对应的距离
	依次循环，直到达到目标点。

	每次取最前端的元素，搞完后sort
	增加一个列表point_list用于存储已经经过的point
	当新的next_point已经存在于point_list中，比较这两者距离start_point的距离，如果大于原有的，不在队列中增加，否则更新
	"""
	## 初始化
	break_flag = 0
	loop_index = 0
	path_queue = [[start_point]]
	distance_queue = [0]
	point_list = [start_point]
	point_distance_list = [0]
	# shortest_path = [[(0,0),(1000,1000)]]
	# shortest_path_distance = [1000000000000000]

	fig, ax = plt.subplots()
	point_x = []  ## Scatter 用
	point_y = []
	for point in point_index:
		# 将point_index中的x, y区分开
		point_x.append(point[0])
		point_y.append(point[1])

	while True:
		## 对distance_queue 进行排序
		## 顺带path_queue
		# print(shortest_path[-1])
		if break_flag == 1:
			break
		# targat_list = copy.deepcopy(distance_queue)
		# fellow_list = copy.deepcopy(path_queue)
		# quick_sort(targat_list, fellow_list, 0, len(targat_list)-1)
		# # print(alist, n, x0)
		# distance_queue = targat_list 
		# path_queue = fellow_list
		# # if len(distance_queue)>0:
		# # 	for i in range(len(distance_queue)):
		# # 		if distance_queue[i] > shortest_path_distance[-1]:
		# # 			cut_number = len(distance_queue) -i
		# # 			for j in range(cut_number):
		# # 				distance_queue.pop()
		# # 				path_queue.pop()
		# # 			break


		if len(distance_queue) == 0:
			# plt.pause(1)
			break

		current_path = path_queue[0]
		current_point = current_path[-1]
		path_queue.pop(0)
		current_path_distance = distance_queue[0]
		distance_queue.pop(0)
		# if current_point == end_point:
		# 	if current_path_distance < shortest_path_distance[-1]:
		# 		shortest_path.append(current_path)
		# 		shortest_path_distance.append(current_path_distance)
		# 	continue
		#####  这个地方可以省略了，与下下句子重复
		# if len(joint[current_point]) > 0:
		for next_point in joint[current_point]:
			if ((next_point not in current_path) and len(joint[next_point])>1) or (next_point == end_point):
				########################################################################
				ax.cla()
				plt.xlim((-140*n_roads, 140*n_roads))
				plt.ylim((-110*n_roads, 110*n_roads))
				plt.grid()
				# loop_index += 1
				plt.title("BAB: "+ str(loop_index)+" steps")
				ax.scatter(point_x, point_y, color = "blue")
				ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
				ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
				#######################################################################
				new_path = []
				new_distance = 0
				for point in current_path:
					new_path.append(point)
				new_path.append(next_point)
				for i in range(len(new_path) - 1):
					vector1 = np.array(new_path[i])
					vector2 = np.array(new_path[i+1])
					distance = int(np.sqrt(np.sum(np.square(vector1-vector2))))
					new_distance += distance
				if next_point == end_point:
					break_flag = 1
					# shortest_path.append(new_path)
					# shortest_path_distance.append(new_distance)
					break
				if new_path not in path_queue:
					if next_point not in point_list:
						point_list.append(next_point)
						point_distance_list.append(new_distance)
						path_queue.insert(0, new_path)  ## DFS--
						# path_queue.append(new_path)  ## BFS--
						distance_queue.insert(0, new_distance)
						print(len(distance_queue), len(path_queue), new_distance)
						# print(len(distance_queue), len(path_queue), shortest_path_distance[-1], new_distance)
						# print("path_queue is: ", path_queue)
						for i in range(len(new_path)-1):
							ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], color = "red")
						plt.pause(0.001)
						loop_index += 1
					else:
						point_list_index = point_list.index(next_point)
						if point_distance_list[point_list_index] > new_distance:
							point_distance_list[point_list_index] = new_distance
							path_queue.insert(0, new_path)  ## DFS--
							distance_queue.insert(0, new_distance)
							print(len(distance_queue), len(path_queue), new_distance)
							for i in range(len(new_path)-1):
								ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], color = "red")
							plt.pause(0.001)
							loop_index += 1
						else:   ## new-distance <= already
							continue

				else:
					pass
					# print("new_path already founded!")
			else:
				pass
				# print("found an end_point!")
	# print(len(shortest_path_distance))
	ax.cla()
	plt.xlim((-140*n_roads, 140*n_roads))
	plt.ylim((-110*n_roads, 110*n_roads))
	plt.grid()
	plt.title("BAB: "+ str(loop_index)+" steps")
	ax.scatter(point_x, point_y, color = "blue")
	ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
	ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
	# new_path = shortest_path[-1]
	ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
	ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
	for i in range(len(new_path)-1):
		ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], color = "red")
	plt.pause(0.3)
	ax.scatter(start_point[0], start_point[1], color = "g", s = 50)
	ax.scatter(end_point[0], end_point[1], color = "g", s = 50)
	for i in range(len(new_path)-1):
		ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], linewidth = 4, color = "green")
	plt.pause(0.3)
	ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
	ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
	for i in range(len(new_path)-1):
		ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], linewidth = 4, color = "red")
	plt.pause(0.3)
	ax.scatter(start_point[0], start_point[1], color = "g", s = 100)
	ax.scatter(end_point[0], end_point[1], color = "g", s = 100)
	for i in range(len(new_path)-1):
		ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], linewidth = 4, color = "green")
	plt.pause(0.1)
	ax.text(x = end_point[0], y = end_point[1], s = str(new_distance), color = "red")
	plt.show()




if __name__ == "__main__":
	##joint = {point:{next_point:distance,---}}
	joint = ComputeDistance(GenerateRoads(points))
	point_index = GetPointIndex(points)  ## 用于获取所有的点
	start_point = point_index[27]
	end_point = point_index[-1]
	BAB(joint, start_point, end_point) 