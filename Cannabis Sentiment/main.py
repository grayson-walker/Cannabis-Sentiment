import operator
from twitter_analysis import get_analysis
from get_state_gdps import get_state_gdps


def main():
	#States we will check
	illegal_states = ['New York','Virginia','North Carolina','Arizona','Arkansas','Connecticut','Delaware',
	'Florida','Hawaii','Illinois','Louisiana','Maryland','Minnesota','Missouri','Montana','New Hampshire','New Jersey',
	'New Mexico','New York','North Dakota','Ohio','Oklahoma','Pennsylvania','Rhode Island','Utah','Virginia','West Virginia']
	
	#dict of state,gdps
	states_gdp = get_state_gdps()
	states_sentiment = {}
	for state in illegal_states:
		#Only analyze states with at least $200,000,000,000 GDP
		if states_gdp[state] > 200000:
			states_sentiment[state] = get_analysis(state)

	#create a sorted list of states, by sentiment ration
	print(states_sentiment)

	#Find companies with holdings by state
	




if __name__ == "__main__": 
	# calling main function 
	main() 
