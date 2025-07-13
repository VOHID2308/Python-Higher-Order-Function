prices = ["$120", "$340", "$50", "$90"]

result = list(map(lambda x: float(x.replace("$", "")), prices))

print(result)
