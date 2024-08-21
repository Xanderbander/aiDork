class ResultParser:
  def __init__(self):
      pass

  def filter_results(self, links, keyword):
      return [link for link in links if keyword.lower() in link.lower()]
