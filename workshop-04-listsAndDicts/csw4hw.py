print("Q1")

myFavoriteNumbers = [16, 10, 6, 8, 11]
myFavoriteNumbers.append(7)
print(myFavoriteNumbers[2])
print(myFavoriteNumbers[0 : 3])
print(myFavoriteNumbers[ :: -1])


sum =0
for i in myFavoriteNumbers:
    sum += i

print(sum)
###################################################
print(" ")
print("Q2")

myFavoritePipettes = {}

myFavoritePipettes = {
"20ulPipette" : "nimble",
"1000ulPipette" : "robust" }

myFavoritePipettes["200ulPipette"] = "much versatile, such wow"


#########################################################
print(" ")
print("Q3")

flowData = [
  ["sampleID", "CD3", "CD4", "CD8"],
  ["stim", 58.3, 24.3, 20.5],
  ["noStim", 32.1, 34.2, 50.3],
  ["PMAstim", 34.3, 15.3, 31.3]
]

flowDataDict = {}

for k in range(0, len(flowData[0])):
    named = flowData[0][k]
    flowDataDict[named] = [flowData[1][k]]
    for i in range(2, len(flowData)):
        flowDataDict[named].append(flowData[i][k])

for j in flowDataDict:
    print(flowDataDict[j])
