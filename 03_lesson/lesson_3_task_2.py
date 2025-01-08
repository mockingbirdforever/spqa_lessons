from smartphone import Smartphone

catalog = []

nokia = Smartphone('+798798902323', 'N-Gage QD', 'nokia')
samsung = Smartphone('+798798902323', 'Galaxy S23 Ultra', 'samsung')
apple = Smartphone('+798798902323', 'iPhone 11 Pro Max', 'apple')
poco = Smartphone('+798798902323', 'F6 PRO', 'poco')
realme = Smartphone('+798798902323', 'GT Neo6', 'realme')


catalog.append(nokia)
catalog.append(samsung)
catalog.append(apple)
catalog.append(poco)
catalog.append(realme)


for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')
