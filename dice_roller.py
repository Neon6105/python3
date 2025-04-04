import random


class DiceBag:
  def __init__(self, *args):
    self.history = list()
    self.dice = list()
    args = args if args else ["2d6"]
    for arg in args:
      assert isinstance(arg, str)
      assert "d" in arg
      self.dice.append(arg)
  # -- end init

  def roll(self, *args):
    args = args if args else self.dice
    assert len(self.dice) > 0
    _result = list()
    for d in args:
      _iteration = list()
      q, n = d.split("d")
      q, n = int(q), int(n)
      for i in range(0, q):
        _iteration.append(random.randint(1, n))
      _result.append((d, _iteration))
    self.history.append(tuple(_result))
    return _result
  # -- end roll

  @property
  def result(self):
    if len(self.history) <= 0:
      self.roll()
    return self.history[-1]
  # -- end result

  @property
  def stats(self):
    turns = len(self.history)
    total = 0
    dice = 0
    for entry in self.history:
      for result in entry:
        dice += len(result[1])
        for face in result[1]:
          total += face
    return f"Rolled {dice} dice over {turns} turns for a grand total of {total}"

  @property
  def peek(self):
    return f"{self.dice}"

# -- end DiceBag


def main():
  my_bag = DiceBag("2d6", "1d4")
  my_bag.roll()
  print(my_bag.result)
  my_bag.roll()
  print(my_bag.result)
  my_bag.roll("2d4")
  print(my_bag.result)
  print(my_bag.stats)
  print(my_bag.history)
  print(my_bag.peek)


if __name__ == "__main__":
  main()
