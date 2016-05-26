def Fractions(a, b):
  def gcd(F, S):
    if S == 0 :
      return F
    else:
      while S:
          F, S = S, F % S
    return F
  
  
  
  c_div = gcd(a,b)
  (r_n,r_de) = (a/c_div, b/c_div)
  
  if r_de == 1:
    return "%d/%d" % (r_n, 1)
  elif c_div == 1:
    return "%d/%d" % (a, b)
  else:
    return "%d/%d" % (r_n, r_de)
print(Fractions(20, 8))
print(Fractions(2, 4))
print(Fractions(10, 100))
print(Fractions(8, 4))

