from Joint import *
import copy
import matplotlib.pyplot as plt

def DFS(joint, start_point, end_point):
	"""
	功能：采用深度优先算法，进行搜索
	创建一个队列，从左到右 path_queue
	创建一个生成路径列表path_list，用于存放搜索到的所有路径
	创建一个point_list 用于存放所有已经经过的节点
	创建一个passed_distanse_dict 用于存放所有路径的距离 
	取第一个path：
		删除该path
		如果current_point != end_point:
			如果current_point有根节点：
				在current_point下生成新的path，插入到队列前端
			当current_point 没有根节点时：
				break
		另如果current_point == end_point:
			将它存放到path_list中
	加上了剩余距离的判断，方向的判断
	"""
	global point_index

	queue0 = [start_point]
	path_queue = [queue0]  # 初始
	path_list = []  # 用于存放所有找到的path
	passed_distance_dict = {}
	point_list = [(start_point)]  # 用于存放所有经过的poing A01
	loop_index = 0

	fig, ax = plt.subplots()
	point_x = []  ## Scatter 用
	point_y = []
	for point in point_index:
		# 将point_index中的x, y区分开
		point_x.append(point[0])
		point_y.append(point[1])

	while True:
		"""
		循环取第一个path
		"""
		continue_flag = 0
		break_flag = 0
		# loop_index += 1
		# print("loop_index is: ", loop_index)
		current_path = path_queue[0]
		path_queue.remove(current_path)
		current_point = current_path[-1]
		lift_distance_dict = {}
		lift_distance_list = []
		lift_point_list = []
		# current_path_temp = copy.deepcopy(current_path)
		# print("path_queue is ",path_queue)
		# print("current_point is: ",current_point)
		# print("current_path is:", current_path)
		
		# if current_point != end_point:
		if len(joint[current_point]) > 0:
			for next_point in joint[current_point]:
				# if ((next_point not in current_path) and (next_point not in point_list)) and (len(joint[next_point]) > 1 or next_point == end_point ):
				vector1 = np.array(end_point)
				vector2 = np.array(next_point)
				distance = int(np.sqrt(np.sum(np.square(vector1-vector2))))
				lift_distance_dict[next_point] = distance
				lift_distance_list.append(distance)
			lift_distance_list.sort()
			for m in range(len(lift_distance_list)):
				for next_point in lift_distance_dict:   ## 当两者距离一样时，会出问题
					if lift_distance_list[m] == lift_distance_dict[next_point] :
						lift_point_list.append(next_point)
			print(lift_distance_dict, lift_distance_list, lift_point_list)
					# for next_point in lift_distance_dict:
						# if lift_distance_list[m] == lift_distance_dict[next_point]:
						# 	print(next_point)
						# # if (next_point not in current_path) and (next_point not in point_list):   ## A01
							# point_list.append(next_point)   ## A01
							########################################################################
			for next_point in lift_point_list:
				if ((next_point not in current_path) and (next_point not in point_list)) and (len(joint[next_point]) > 1 or next_point == end_point ):
					point_list.append(next_point) 
				# if next_point not in current_path:
					ax.cla()
					plt.xlim((-140*n_roads, 140*n_roads))
					plt.ylim((-110*n_roads, 110*n_roads))
					plt.grid()
					loop_index += 1
					plt.title("HillClimbing: "+ str(loop_index)+" steps")
					ax.scatter(point_x, point_y, color = "blue")
					ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
					ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
					#######################################################################
					# print("current_path is: ", current_path)
					# print("next_point is", next_point)
					# new_path = eval(current_path_temp.append(next_point))
					new_path = []
					for point in current_path:
						new_path.append(point)
					new_path.append(next_point)
					# if new_path in (path_queue or path_list):
					# 	continue_flag == 1
					# 	continue
					# print("new_path is ", new_path)
					if next_point != end_point:
						if (new_path not in path_queue) or (new_path not in path_list):
							path_queue.insert(0, new_path)
						# print("path_queue is: ", path_queue)
						for i in range(len(new_path)-1):
							ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], color = "red")
						plt.pause(0.1)
					else:
						break_flag = 1 ## 注释掉之后，就可以一直搜索，直到所有路径被发现，现在只要找到一个就停止
						if new_path not in path_list:
							path_list.append(new_path)
						######################################################################################
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
						distance = 0
						for i in range(len(new_path)-1):
							vector1 = np.array(new_path[i])
							vector2 = np.array(new_path[i+1])
							distance += int(np.sqrt(np.sum(np.square(vector1-vector2))))
							ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], linewidth = 4, color = "green")
						plt.pause(0.1)
						ax.text(x = end_point[0], y = end_point[1], s = str(distance), color = "red")
						# plt.pause(0.3)
						# ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
						# ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
						# for i in range(len(new_path)-1):
						# 	ax.plot([new_path[i][0], new_path[i+1][0]], [new_path[i][1], new_path[i+1][1]], linewidth = 4, color = "red")
						#################################################################################
					break
				else:
					print("next_point already passed")	
					# print("lift_distance_list[m] == lift_distance_dict[next_point]")
			# else:
				# print("next_point already passed")	
						
		else:
			print("in DFS: find an deadEnd")
		# if continue_flag == 1:
		# 	continue
		if len(path_queue) < 1:
			break
		if break_flag == 1:
			break
	# path_queue.remove(current_path)
	plt.show()	


if __name__ == "__main__":
	##joint = {point:{next_point:distance,---}}
	joint = ComputeDistance(GenerateRoads(points))
	point_index = GetPointIndex(points)
	start_point = point_index[27]
	end_point = point_index[-1]
	DFS(joint, start_point, end_point) 