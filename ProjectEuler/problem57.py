

iterations = 1000
numerator = 1
denominator = 2
acc = numerator/denominator


terms = [[3,2]]


count = 0
for i in range(iterations):
   numerator = terms[-1][0]
   denominator = terms[-1][1]

   if len(str(numerator)) > len(str(denominator)):
      count += 1

   numerator -= denominator

   d_numerator = 2 * denominator + numerator
   d_denominator = denominator

   terms += [[d_denominator+d_numerator,d_numerator]]

print(terms, count)


