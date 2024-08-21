def validate_url(url):
  if url.startswith('http://') or url.startswith('https://'):
      return True
  return False

def format_query(query):
  return query.replace(' ', '+')
