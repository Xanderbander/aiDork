import random

class DorkGenerator:
    def __init__(self):
        self.templates = [
            'inurl:"index of" {}',
            'intitle:"index of" {}',
            'inurl:"admin" {}',
            'inurl:"login" {}',
            'site:{} "{}"',
            '"{}" filetype:{}'
        ]

    def generate_dork(self, keyword, filetype=None, site=None):
        template = random.choice(self.templates)
        if '{}' in template:
            if filetype:
                return template.format(keyword, filetype)
            elif site:
                return template.format(keyword, site)
            else:
                return template.format(keyword)
        else:
            return template
