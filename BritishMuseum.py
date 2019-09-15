from Joint import *
import copy
import matplotlib.pyplot as plt


def Forward(joint, current_path, end_point):
	"""
	功能：对每一个current_path,返回 n 个new_path(next_path_list,用一个列表返回)（存放在path_list开头）
	并且对新节点负责，要求next_point不能存在于current_path中，
	# 完毕，删除current_path。
	"""
	next_path_list = []
	current_point = current_path[-1]  ## 获取当前位置,固定
	# print("current_point is ", current_point)
	next_points = joint[current_point]  ## next_point 列表
	# print(next_points)
	if len(next_points) != 0:
		for next_point in next_points:
			print(joint[next_point])
			# len_next_point = len(joint[next_point])
			if len(joint[next_point]) > 1 or next_point == end_point:
				# print("in Forward(), next_point is ", next_point)
				current_path_temp = copy.deepcopy(current_path)
				# print("in Forward(), current_path_temp is: ", current_path_temp)
				if next_point not in current_path_temp:
					current_path_temp.append(next_point)
					next_path_list.append(current_path_temp)
					# print("in Forward(), next_path_list is: ", next_path_list)
				else:
					print("in Forward(), next_point in current_path_temp")
			else:
				print("found an endpoint: ", next_point)
	else:
		next_path_list.append(current_path)
	return next_path_list


def BritishMuseum(joint, start_point, end_point):
	"""
	功能：输入node节点，输出能够找到从起点到终点的所有可能方式
	要求：不能往回走
	首先有一个path_list，用于存放所有的path
	path_list中的单个元素为经过的所有节点的集合，path_list[0]为start_point
	path_list[-1]为current_point,当current_point = end_point时，该元素为一个完整的元素。
	对于每一个当前节点，搜索其next_point，并扩充至它的路径中，扩充完毕后，删除之前的节点
	对于每一条路径，都要保证，不能走重复的节点，即新增节点不能已经存在。
	创建一个递归函数，每一次更新当前current_point,当current_point == end_point, return
	"""
	## 画图
	global point_index

	path_list = [[start_point]]  ## 初始


	fig, ax = plt.subplots()
	point_x = []  ## Scatter 用
	point_y = []
	for point in point_index:
		# 将point_index中的x, y区分开
		point_x.append(point[0])
		point_y.append(point[1])
	loop_index = 0
	while True:
		continue_flag = 0
		"""
		循环，当path_list中的所有path的current_point == end_point，退出
		"""
		path_list_temp  = copy.deepcopy(path_list)
		# print(path_list)
		# plt.title(loop_index)
		
		for current_path in path_list:
			"""
			将Forward()函数返回的next_path_list中的元素添加到new_path_list中(append)
			"""
			try:
				q = len(joint[current_path[-1]])
				print("go on")
			except:
				continue_flag =1
				break
			next_path_list = Forward(joint, current_path, end_point)
			for new_path in next_path_list:
				path_list_temp.append(new_path)
			path_list_temp.remove(current_path)
		if continue_flag == 1:
			continue
		path_list = copy.deepcopy(path_list_temp)
		## plot
		print(len(path_list))
		for path in path_list:
			loop_index += 1
			## 画图 当寻找到路径后停止寻找
			break_flag = 0
			ax.cla()
			plt.xlim((-140*n_roads, 140*n_roads))
			plt.ylim((-110*n_roads, 110*n_roads))
			plt.grid()
			plt.title("BritishMuseum:"+str(loop_index)+" steps")
			ax.scatter(point_x, point_y, color = "blue")
			ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
			ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
			if path[-1] != end_point:
				##  没有找到的时候
				break_flag = 0
				# print("in  BritishMuseum: break_flag is: ", break_flag)
				# ax.cla()
				# plt.title(loop_index)
				# ax.scatter(point_x, point_y, color = "blue")
				# ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
				# ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
				for i in range(len(path)-1):
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color = "red")
				if path[-1] == end_point:
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color = "red")	
				plt.pause(0.0001)
			else:
				##  当找到路径后
				break_flag = 1
				# print("in  BritishMuseum: break_flag is: ", break_flag)
				# ax.cla()
				# ax.scatter(point_x, point_y, color = "blue")
				# ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
				# ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
				for i in range(len(path)-1):
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color = "red")
				plt.pause(0.2)
				ax.scatter(start_point[0], start_point[1], color = "green", s = 50)
				ax.scatter(end_point[0], end_point[1], color = "green", s = 50)
				for i in range(len(path)-1):
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], linewidth=4, color = "green")
				plt.pause(0.2)
				ax.scatter(start_point[0], start_point[1], color = "red", s = 50)
				ax.scatter(end_point[0], end_point[1], color = "red", s = 50)
				for i in range(len(path)-1):
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], linewidth=4, color = "red")
				plt.pause(0.2)
				ax.scatter(start_point[0], start_point[1], color = "green", s = 100)
				ax.scatter(end_point[0], end_point[1], color = "green", s = 100)
				for i in range(len(path)-1):
					ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], linewidth=4, color = "green")
				plt.pause(0.2)
				# if path[-1] == end_point:
				# 	ax.plot([path[i][0], path[i+1][0]], [path[i][1], path[i+1][1]], color = "green")	
				
				break

		###############################################################
		### A 方案， 当所有的路径都找到了， 不可取
		# for path in path_list:
		# 	# 循环判断是否结束
		# 	break_flag = 1
		# 	if path[-1] = end_point:
		# 		break_flag = 0
		# 		print("in  BritishMuseum: break_flag is: ", break_flag)
		# 		break
		# if break_flag == 1:
		# 	break
		###############################################################

		###############################################################
		###　B 方案， 找到一个即停止
		# for path in path_list:
		# 	# 循环判断是否结束
		# 	break_flag = 0
		# 	if path[-1] == end_point:
		# 		break_flag = 1
		# 		print("in  BritishMuseum: break_flag is: ", break_flag)
		# 		break
		if break_flag == 1:
			break
		print("in BritishMuseum: break_flag is: ", break_flag)
		###############################################################
	plt.show()
	return path_list

if __name__ == "__main__":
	##joint = {point:{next_point:distance,---}}
	joint = ComputeDistance(GenerateRoads(points))
	point_index = GetPointIndex(points)
	# print("=====", len(joint), len(point_index))
	start_point = point_index[27]
	end_point = point_index[-1]
	BritishMuseum(joint, start_point, end_point)