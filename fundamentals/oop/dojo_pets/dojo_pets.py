from ninja import Ninja
from pets import Pet, Fish

richie = Pet('Richie', 'Dog',['Fetch', 'Roll over', 'Play dead'], 'Bark bark')

john = Ninja('John', 'Tran', ['Crackers', 'Chips', 'Cookies'], ['Kibbles', 'Steak', ' Chicken'], richie)

bob = Fish('Bob')

john.about()
john.bathe().walk().feed().feed().feed().feed().feed()
john.about()

bob.stats()