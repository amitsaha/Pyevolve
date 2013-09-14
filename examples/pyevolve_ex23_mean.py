from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Mutators
from pyevolve import Initializators
from pyevolve import Consts

# This function is the evaluation function
# As close to the target mean as possible
def eval_func(genome):

   score =  (386.0 - sum(genome)/len(genome)*1.0)**2
   return score

def run_main():
   # Genome instance, 1D List of 12 elements
   genome = G1DList.G1DList(12)

   # Sets the range max and min of the 1D List
   genome.setParams(rangemin=350, rangemax=400, bestrawscore=0.00, rounddecimal=2)
   genome.initializator.set(Initializators.G1DListInitializatorReal)
   genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
   # The evaluator function (evaluation function)
   genome.evaluator.set(eval_func)

   # Genetic Algorithm Instance
   ga = GSimpleGA.GSimpleGA(genome)

   # Set the GA parameters
   # the termination criteria
   ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
   ga.setGenerations(100)
   ga.setCrossoverRate(0.8)
   ga.setPopulationSize(100)
   ga.setMutationRate(0.06)
   ga.setMinimax(Consts.minimaxType["minimize"])

   # Do the evolution, with stats dump
   # frequency of 20 generations
   ga.evolve(freq_stats=10)

   # Best individual
   print ga.bestIndividual()

if __name__ == "__main__":
   run_main()
