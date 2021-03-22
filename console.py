import pdb

from models.keiko import Keiko
import repositories.keiko_repository as keiko_repository

from models.sensei import Sensei
import repositories.sensei_repository as sensei_repository

from models.deshi import Deshi
import repositories.deshi_repository as deshi_repository

from models.waza import Waza
import repositories.waza_repository as waza_repository

keiko_repository.delete_all()
sensei_repository.delete_all()
deshi_repository.delete_all()
waza_repository.delete_all()

waza_1 = Waza("Kokyo Ho")
waza_repository.save(waza_1)

waza_2 = Waza("Ikkyo")
waza_repository.save(waza_2)

waza_3 = Waza("Nikyo")
waza_repository.save(waza_3)

waza_4 = Waza("Kubi Nage")
waza_repository.save(waza_4)

sensei_1 = Sensei("Musashi")
sensei_repository.save(sensei_1)

sensei_2 = Sensei("Nobunaga")
sensei_repository.save(sensei_2)

deshi_1 = Deshi("Bulma")
deshi_repository.save(deshi_1)

deshi_2 = Deshi("Picollo")
deshi_repository.save(deshi_2)

keiko_1 = Keiko(sensei_1, "19:30:00")
keiko_repository.save(keiko_1)

keiko_2 = Keiko(sensei_2, "10:00:00")
keiko_repository.save(keiko_2)







pdb.set_trace()
