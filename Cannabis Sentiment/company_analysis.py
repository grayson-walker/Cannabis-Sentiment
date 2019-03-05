class CannCompany(object): 
	''' 
	Generic Cannabis Company class 
	'''
	def __init__(self,name,license_dict): 
		self.name = name
		self.license_dict = license_dict
	
	#Will use the sentiment rating of the states its operational in, state gdp, number licenses, to calculate value
	def calculate_value(self,states_sentiment):
		pass



class State(object): 
	''' 
	Generic Cannabis Company class 
	'''
	def __init__(self,name,license_dict): 
		self.name = name
		self.license_dict = license_dict
		self.gdp = gdp


	