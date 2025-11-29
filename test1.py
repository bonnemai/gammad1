from simplefix import FixMessage

# Créer un message FIX
msg = FixMessage()
msg.append_string("8=FIX.4.2")
msg.append_string("9=100")
msg.append_string("35=D")  # New Order - Single
msg.append_string("49=SENDER")
msg.append_string("56=TARGET")
msg.append_string("34=1")
msg.append_string("52=20230101-12:00:00")
msg.append_string("11=ORDER123")  # ClOrdID
msg.append_string("55=AAPL")  # Symbol
msg.append_string("54=1")  # Side (1 = Buy)
msg.append_string("38=100")  # OrderQty
msg.append_string("40=2")  # OrdType (2 = Limit)
msg.append_string("44=150.50")  # Price

# Afficher le message encodé
print("Message FIX encodé:")
encoded = msg.encode()
print(encoded)

# Accéder aux champs du message
print("\nChamps du message:")
print(f"  Message Type (35): {msg.get(35)}")
print(f"  Symbol (55): {msg.get(55)}")
print(f"  OrderQty (38): {msg.get(38)}")
print(f"  Price (44): {msg.get(44)}")