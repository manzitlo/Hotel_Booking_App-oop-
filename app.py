import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_card = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        """book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def confirm(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data: 
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        City: {self.hotel.city}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validation(self, expiration, holder_name, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder_name, "cvc": cvc}
        if card_data in df_card:
            return True
        else:
            return False


print(df)

hotel_ID = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_ID)

if hotel.available():
    card_number = input("Enter the credit card number: ")
    credit_card = CreditCard(number=card_number)
    card_expiration = input("Enter the expiration time: (xx/xx)")
    card_holder = input("Enter the holder name in the card: ")
    card_cvc = input("Enter the cvc code: ")

    if credit_card.validation(card_expiration, card_holder, card_cvc):
        hotel.book()

        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(reservation_ticket.confirm())
    else:
        print("There was a problem with your payment")

else:
    print("Hotel is not free.")
