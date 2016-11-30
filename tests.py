ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]

ByTen = [
"zero",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

zGroup = [
"",
"thousand",
"million",
"billion",
"trillion",
"quadrillion",
"quintillion",
"sextillion",
"septillion",
"octillion",
"nonillion",
"decillion",
"undecillion",
"duodecillion",
"tredecillion",
"quattuordecillion",
"sexdecillion",
"septendecillion",
"octodecillion",
"novemdecillion",
"vigintillion"
]


def subThousand(n):
    print("lo que llega", n)
    if n <= 19:
        return ByOne[n]
    elif n <= 99:
        q, r = divmod(n, 10)
        return ByTen[q] + (" " + subThousand(r) if r else "")
    else:
        q, r = divmod(n, 100)
        return ByOne[q] + " hundred" + (" and " + subThousand(r) if r else "")

def thousandUp(n):
    return " ".join(reversed([subThousand(z) + (" " + zGroup[i] if i else "") if z else "" for i,z in enumerate(splitByThousands(n))]))

def splitByThousands(n):
    res = []
    while n:
        n, r = divmod(n, 1000)
        res.append(r)
    return res

def get_number_as_words(n):
  if n==0:
    return "Zero"
  return ("Minus " if n < 0 else "") + thousandUp(abs(n))

def main():
  n = 1023 # int(raw_input("Please enter an integer:\n>> "))
  print(get_number_as_words(n))

if __name__ == "__main__":
  main()