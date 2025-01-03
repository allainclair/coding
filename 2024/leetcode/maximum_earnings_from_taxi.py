# https://leetcode.com/problems/maximum-earnings-from-taxi/

def max_taxi_earnings_(n: int, rides: list[list[int]]) -> int:
	max_earning = 0
	for i, start_ride in enumerate(rides[:-1]):
		start, current_end, tip = start_ride
		current_max_earning = current_end - start + tip
		print("*** start_ride", start_ride)

		earnings = [0]*len(rides[i + 1:])
		prev_earning = current_end - start + tip
		earnings[0] = prev_earning
		print("start earnings", earnings)
		for j, ride in enumerate(rides[i+1:]):
			earnings[j] = prev_earning

			current_earning = current_max_earning
			print("current_start", ride[0])
			print("current_end", current_end)
			print(ride[0] >= current_end)

			# if ride[0] >= current_end:
			# 	print("current_ride", ride)
			# 	current_earning += ride[1] - ride[0] + ride[2]
			# 	current_end = ride[1]
			# 	print("current_earning", current_earning)
			# 	if current_earning > current_max_earning:
			# 		current_max_earning = current_earning

			if ride[0] >= current_end:
				earnings[j] += prev_earning + (ride[1] - ride[0] + ride[2])
				# prev_earning = earnings[j]
				current_end = ride[1]
			else:
				prev_earning = earnings[j]

			print("earnings", earnings)
			print()

		print("Final earnings", earnings)
		if current_max_earning > max_earning:
			max_earning = current_max_earning
			print("- current max_earning", max_earning)

	return max_earning


class Stop:
	def __init__(self, start, end, tip):
		self.start = start
		self.end = end
		self.tip = tip

	def __repr__(self):
		return f"({self.start}, {self.end}, {self.tip})"

	def cost(self):
		return self.end - self.start + self.tip


def max_taxi_earnings__(n: int, rides: list[list[int]]) -> int:
	costs = []
	current_start, current_end, tip = rides[0]
	stop = Stop(current_start, current_end, tip)
	max_cost = stop.cost()
	for i, start_ride in enumerate(rides[:-1]):
		current_start, current_end, tip = start_ride
		current_stop = Stop(current_start, current_end, tip)
		# max_cost = max_cost or current_stop.cost()

		path = [current_stop]
		paths = [path]
		for j, ride in enumerate(rides[i + 1:]):
			start, end, tip = ride
			stop = Stop(start, end, tip)

			# if ride[0] >= current_end:
			new_paths = []
			for p in paths:
				last_stop = p[-1]

				new_p = []
				for s in p:
					new_p.append(s)
					if stop.start >= s.end:
						new_path = new_p + [stop]
						print(new_path)
						new_paths.append(new_path)
						cost = sum(stop.cost() for stop in new_path)
						if max_cost < cost:
							print("new_path max", new_path)
							max_cost = cost
							costs.append(cost)
			paths += new_paths

				# if stop.start >= last_stop.end:
				# 	new_path = p + [stop]
				# 	paths.append(new_path)
				#
				# 	cost = sum(stop.cost() for stop in new_path)
				# 	if max_cost < cost:
				# 		print("new_path max", new_path)
				# 		max_cost = cost

						# costs.append(cost)

		print("Final paths")
		for p in paths:
			print(p)

	print("costs", costs)
	return max_cost


def max_taxi_earnings(n: int, rides: list[list[int]]) -> int:
	def max_taxi_earnings_rec(i: int, rides: list[list[int]], prev_end, prev_cost):
		print(rides)
		if rides:
			ride = rides[0]
			start, end, tip = ride

			max_ = prev_cost
			if start >= prev_end and i <= n:
				current_cost = prev_cost + (end - start + tip)
				max_ = current_cost
				for j, _ in enumerate(rides):
					m = max_taxi_earnings_rec(i+1, rides[j+1:], end, current_cost)
					if m > max_:
						max_ = m

			max_2 = prev_cost
			for j, _ in enumerate(rides):
				m = max_taxi_earnings_rec(i, rides[j+1:], prev_end, prev_cost)
				if m > max_2:
					max_2 = m
			return max(max_, max_2)

		else:
			return prev_cost

	return max_taxi_earnings_rec(0, rides, 0, 0)


def main():
	rides = [
		[1, 6, 1],
		[3, 10, 2],   # 9


		[10, 12, 3],  # +5 = 14
		[11, 12, 2],


		[12, 15, 2],  # +5 = 19
		[13, 18, 1],  # +6 = 20
	]
	# max_ = max_taxi_earnings(20, rides)
	# print(max_)
	# assert max_ == 20
	#
	# rides = [[2, 5, 4], [1, 5, 1]]
	# max_ = max_taxi_earnings(5, rides)
	# print(max_)
	# assert max_ == 7

	rides = [[2,3,6],[8,9,8],[5,9,7],[8,9,1],[2,9,2],[9,10,6],[7,10,10],[6,7,9],[4,9,7],[2,3,1]]
	max_ = max_taxi_earnings(5, rides)
	print(max_)
	assert max_ == 33


if __name__ == "__main__":
	main()
