def calculate_choclate(money):
  wrapper = money
  choclate = money
  choclate_with_wrapper = 0
  while wrapper >= 3:
    choclate_with_wrapper = wrapper // 3
    choclate = choclate + choclate_with_wrapper
    wrapper = wrapper % 3 + choclate_with_wrapper
  return choclate

def main():
  money = 12102080
  print(calculate_choclate(money))

main()
  

  