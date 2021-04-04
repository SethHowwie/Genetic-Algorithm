from random import randint
from random import randrange
import random

def fitness(genome,key):
    seed = 'ztVvDguRAQDaSXXmLeJkUxRejhCGKfRjWDJCwowiSioIwtDqDHwelMnDfsXlhceWgMKXBUbsqlDVvXhpXXgtTjNmdBQfVsacmEvbHxQXodqKLaeFsrwlyMTkvziWPOAbgDjMXZRpUyrMVRmKhZotMIQtZHuzkvrlpgYgYAjFgOHYhrDquFTKxfargRnZDtISDpvEZqQJgLmRlyJrnqMiampUBMlcyyLqKJypCAiKhFIxuYlZkiYeOtVQCktDJAvgjiickEOvISfiaJqHUjOfuaRpdGFysIgoyXnVbjIVfDQhpgtVDIvHRmRnApMTDFQIPFWLNMkCWoMPgvNCpAFFDIEzxIWAodRAOrErfuTzdbRjMroKhomBBEzvraoKpAMeQXlzantpvUhWPNNCodmpJaThVTFYevCCwVahUpUncRDKpWhoogIUcpBcSSudgHrsIjQAcNjWFjOITSBWeASqotPMBIjzomMsdWEnyIkrfPgnbnYXgrwfZlNfYyAvBsUxQgVoLnHkWtXaKrGiDjEbJeMcOqTpCzFuSmRhIwPd'
    mult = list(range(-33,0))+list(range(1,33))
    s = 0
    for x in range(len(genome)):
        #print(int(genome[x]))
        s+=(ord(seed[x+key])-ord(seed[key-1]))*(mult[int(genome[x])+32])+10
    return s


######################################################
#  Do not change the code above this section
#  Modify the code BELOW this section
######################################################


"""
Part One
Method:  newChromosome() 
Inputs:  None
Outputs: A single, length 32 string of 1s and 0s
"""
def newChromosome():
    n = 0
    chromosome = ""
    while n <= 31:
        val = randint(0,1)
        chromosome += str(val)
        n += 1
    return chromosome
    

"""
Part Two
Method:  mutation() 
Inputs:  A length 32 string
Outputs: A length 32 string that only differs by one "bit" from the input
"""
def mutation(originalChromosome):
    mutatedChromosome = ""
    valList = []
    for value in originalChromosome:
        valList.append(int(value))
    
    val = randrange(len(valList))
    mut = valList[val]
    if mut == 0:
        valList[val] += 1
    else:
        valList[val] -= 1
    for newVal in valList:
        mutatedChromosome += str(newVal)
    return mutatedChromosome


"""
Part Three
Method:  crossover() 
Inputs:  Two length 32 strings
Outputs: Two length 32 strings that were formed by using a random crossover point
NOTE: Crossover point should be a number from 1-31 and the point should indicate HOW MANY
      characters to take from the front of one string.  Obviously, you would take 32-Crossover point
      characters from the second string
"""
def crossover(orig1, orig2):
    select1 = ""
    select2 = ""
    split = randint(1,31)
    print(split)
    c1 = []
    c2 = []
    c1SplitAfter = []
    c2SplitAfter = []
    c1SplitBefore = []
    c2SplitBefore = []
    for char in orig1:
        c1.append(char)
    for val in orig2:
        c2.append(val)
    c1Split1 = c1[split:]
    print(c1Split1)
    c1Split2 = c1[:split]
    print(c1Split2)
    c2Split1 = c2[split:]
    print(c2Split1)
    c2Split2 = c2[:split]
    print(c2Split2)
    for val in c1Split2:
        select1 += val
    for val in c2Split1:
        select1 += val
    for val in c2Split2:
        select2 += val
    for val in c1Split1:
        select2 += val 
    return select1,select2


        
"""
Part Four
Method:  bestFits() 
Inputs:  A list of chromosomes - one population
         The key to be used by the fitness function
Outputs: A single chromsome from the list of chromsomes
         The fitness score for that chromosome
NOTE: The outputs should be the BEST score found in the list of chromosomes
"""
def bestFits(population,key):
    bestChromosome=""
    bestScore=-1000
    fitDict = {}
    for chrom in population:
        s = fitness(chrom, key)
        fitDict[s] = chrom
    keyList = [*fitDict]
    maxKey = max(keyList)
    bestChromosome += str(fitDict[maxKey])
    bestScore = maxKey
    return bestChromosome,bestScore



"""
Part Five
Method:  lottery() 
Inputs:  A list of chromosomes - one population
         The key to be used by the fitness function
Outputs: A significantly larger list of chromsomes.  
NOTE: The length of the output list is variable depending on the chromsomes in the input
       population and their fitness functions.
       Each chromosome from the input population will likely occur
       multiple times in the output list.
"""
def lottery(population,key):
    outputList=[]
    for chrom in population:
        #print(chrom)
        s = fitness(chrom, key)
        if s >= 10:
            copies = s // 10
            for cop in range(copies):
                outputList.append(chrom)

    return outputList


"""
Part Six
Method:  GARunner()
Inputs: pSize - an int, the number of chromsomes in each population
        gen - the number of generations for which the GA is run
        sel - the number of members of gen N who automatically pass to gen N+1 (selection)
        mut - the number of members of gen N who are mutated and moved on to gen N+1 (mutation)
        nb  - the number of brand new chromosomes introduced each generation (new blood)
        co  - the number of PAIRS of chromosomes that undergo crossover each generation (crossover)
        key - the key used by the fitness function
Outputs:    bestChromosome - The best length 32 chromsome from the final generation
            bestScore - The fitness value of that best Chromosome
NOTE : sel + mut + nb + 2*co must equal pSize.  If not, you should return "" and -1000 for the output values
"""
def GARunner(pSize,gen,sel,mut,nb,co,key):
    bestChromosome=""
    bestScore = -1000
    population = []
    for val in range(pSize):
        chrom = newChromosome()
        population.append(chrom)
    check = sel + mut + nb + (2*co)
    if pSize != check:
        return "", -1000
    print("Best in generation 0: ", bestFits(population, key))
    previousGen = population
    n = 1
    nextGen = []
    while n <= gen:
        chrom = lottery(previousGen, key)
        #print(previousGen)
        for val in range(sel):
            index = randint(0,len(chrom) - 1)
            nextGen.append(chrom[index])
        for val in range(mut):
            index = randint(0,len(chrom) - 1)
            mutated = mutation(chrom[index])
            nextGen.append(mutated)
        for val in range(nb):
            chrom = newChromosome()
            nextGen.append(chrom)
        for val in range(co):
            index1 = randint(0, len(chrom) - 1)
            index2 = randint(0,len(chrom) - 1)
            crossed = crossover(chrom[index1], chrom[index2])
            nextGen.append(crossed)
        previousGen.clear()
        for chrom in nextGen:
            previousGen.append(chrom)
        nextGen.clear()
        print("Best in generation",n,":", bestFits(previousGen, key))
        n += 1
    best = bestFits(previousGen, key)
    bestChromosome += str(best[0])
    bestScore = best[1]

    return bestChromosome,bestScore
    


