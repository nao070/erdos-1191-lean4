from pathlib import Path
import importlib.util
p=Path('tests/test_validate_pack.py');s=importlib.util.spec_from_file_location('pack_tests',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
names=sorted(n for n in vars(m) if n.startswith('test_') and callable(getattr(m,n)))
for n in names:getattr(m,n)();print('PASS',n)
print('TESTS:',len(names),'passed')
