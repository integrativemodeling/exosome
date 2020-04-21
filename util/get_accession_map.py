# Create the accession map used by test/mock/sitecustomize.py

import ihm.reference

codes = ['Q08162', 'Q05636', 'P38792', 'P53859', 'P48240', 'Q08285', 'Q12277',
         'P46948', 'P53256', 'P25359', 'P38801', 'Q12149', 'P53725', 'Q08491']

def pp(s):
    indent = 8
    width = 66
    def get_lines(s):
        for i in range(0, len(s), width):
            yield ' ' * indent + "'" + s[i:i+width] + "'"
    return '\n'.join(l for l in get_lines(s))

for code in codes:
    u = ihm.reference.UniProtSequence.from_accession(code)
    print("    '%s': {'db_code':'%s', 'sequence':\n%s},"
          % (code, u.db_code, pp(u.sequence)))
