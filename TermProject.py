from scipy.stats import norm
import numpy as np
import random

#ignore this for now
data_normal = norm.rvs(size = 10000, loc=0,scale=1)


class Voter:
	def __init__(self, opinion, educ, wtl, social, influence):
		self.opinion = opinion #0-1 value range indicating political beliefs
		self.educ = educ #education level, in years
		self.wtl = wtl #willingness to listen - how stubborn preferences are
		self.social = social #how many interactions this person will have
		self.influence = influence #how influential this person is

	#returns a numerical value for the likelihood of being influenced
	#could potentially incorporate some machine learning concepts to formulate an optimal equation
	def influence_equation(self):
		#returns a fractional (%) value that is associated with the influentiability of a particular person
		#possibly incorporate machine learning here to determine values of the weights of each value, for now they are arbitrary values
		return 0.05*self.educ + 0.1*self.wtl + 0.5*self.influence

	def interaction(self, otherPerson):
		#calculate difference between people interacting, and change opinions based on who is more influential (based on influence eq)
		influence_diff = self.influence_equation() - otherPerson.influence_equation()
		if(influence_diff > 0):
			otherPerson.opinion = otherPerson.opinion - influence_diff
		else if(influence_diff < 0):
			self.opinion = self.opinion - influence_diff
		else:
			return
		#value based on influence_equation of person and otherPerson,
		#add up both people's influence eq's, then add the subsequent remainder to 
		#as well as influence, value will determine who was influenced and by how much
		#interaction should be based on sir model from previous project - during each interaction, calculate each person's new values based on the weights of their current values
		#consider introducing "Misinformation" as well (ie some numerical value that affects voter's overall equation values)

def society_generator(population):
	people = []
	for i in range(population):
		people.append(Voter(np.random.normal(0.5, scale=0.18, size=1)), 
							np.random.gamma(2, scale=2, size=1),
							np.random.normal(0.5, scale=0.18, size=1), #should be based on political stance, ie how radical their beliefs are - more rad = less wtl
							np.random.randint(0, high=10, size=1),
							np.random.gamma(2, scale=2, size=1)) #go over these to make sure they give the correct values that you want for your population

#next, test that the above np methods give you the things that you want
print(np.random.normal(0.5, scale=0.18, size=10))
print(np.random.normal(2, scale=2, size=10))
print(np.random.randint(0, high=10, size=10))

def experiment(society, num_periods):
	#generate x number of voters, and thieir corresponding
	#preferences using a normal distribution

	#generate opinion probabilities based on normal dist.
	#more extreme values associated with smaller prob. of changing opinion

	#run the information model (many iterations)
	period = 1

	while period <= num_periods:
		#do stuff
		#for each iteration, run an interaction among the population, wherein the interaction function changes the values for each voter's values
		period += 1
	return
