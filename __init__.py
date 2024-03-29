from flask import Flask, redirect, url_for, render_template, session, request, jsonify
from Forms import *

from datetime import datetime
from Guest import *
from collections import Counter
from Hospital import *
from Occupation import *
from Vehicle import *
from Supplier import *
from Inventory import *
from Industry import *
from Partnerships import *
from PackageDeal import *
from Order import *
from Request import *
import shelve ,Reservation, Review,smtplib,ssl
import json
import random
import requests
import shelve, User, Staff
from ProductCat import *





app = Flask(__name__)
app.config["SECRET_KEY"]= "@ajhdfbajshd"



#Gerald's part
@app.route('/')
def home_page():
    return render_template('homura.html')

@app.route('/userHome')
def user_home():
    reviews_dict = {}
    try:
        db = shelve.open('review')
        reviews_dict = db['Reviews']
        db.close()
    except:
        print("No reviews found.")
        reviews_dict={}

    reviews_list = []
    print(reviews_dict)
    for key in reviews_dict:
        review = reviews_dict.get(key)
        reviews_list.append(review)
    print(reviews_list)

    return render_template('userHome.html', count_review=len(reviews_list), reviews_list=reviews_list)

@app.route('/admin')
def home():
    return render_template('home.html')

@app.route('/createReservation', methods=['GET', 'POST'])
def createReservation():
    createReservationForm = CreateReservationForm(request.form)
    reservationDateForm = ReservationDateForm()
    if request.method == 'POST' and createReservationForm.validate() and reservationDateForm.validate():
        reservations_dict = {}
        reservation_count_id = 0
        db = shelve.open('Reservation.db')
        try:
            reservations_dict = db['Reservations']
            reservation_count_id = int(db['reservation_count_id'])
        except:
            print("Error in retrieving Reservation from Reservation.db.")

        reservation = Reservation.Reservation(createReservationForm.first_name.data, createReservationForm.last_name.data, createReservationForm.email.data, createReservationForm.contact.data, reservationDateForm.date.data, createReservationForm.time_slot.data, createReservationForm.remarks.data)
        print(reservationDateForm.date.data)
        #auto increment user_id from shelve
        reservation_count_id = reservation_count_id + 1
        reservation.set_reservation_id(reservation_count_id)
        db['reservation_count_id'] = reservation_count_id

        reservations_dict[reservation.get_reservation_id()] = reservation
        db['Reservations'] = reservations_dict
        db.close()

        return redirect(url_for('confirmationReservation'))
    return render_template('createReservation.html', form=createReservationForm, dateform = reservationDateForm)

@app.route('/review', methods=['GET', 'POST'])
def createReview():
    print("hi")
    createReviewForm = CreateReviewForm(request.form)
    print("hello")
    if request.method == 'POST' and createReviewForm.validate():
        reviews_dict = {}
        review_count_review_id = 0
        db = shelve.open('review')
        print("chicken")

        try:
            reviews_dict = db['Reviews']
            review_count_review_id=db['review_count_review_id']
            print(reviews_dict)
        except:
            print("Error in retrieving Reservation from storage.db.")

        print("dinosour")
        review = Review.Review(createReviewForm.reviewfirst_name.data, createReviewForm.reviewlast_name.data, createReviewForm.reviewfeedback.data)
        #auto increment user_id from shelve
        review_count_review_id = review_count_review_id + 1
        review.set_review_id(review_count_review_id)
        print(review_count_review_id)
        db['review_count_review_id'] = review_count_review_id

        reviews_dict[review.get_review_id()] = [review.get_review_id(), review.get_reviewfirst_name(), review.get_reviewlast_name(), review.get_reviewfeedback()]
        db['Reviews'] = reviews_dict
        print(reviews_dict)
        db.close()
        return redirect(url_for('user_home'))
    return render_template('createReview.html', form=createReviewForm)

@app.route('/adm_retrieveReservation', methods = ['POST','GET'])
def adm_retrieveReservation():
    reservations_dict = {}
    try:
        db = shelve.open('Reservation.db')
        reservations_dict = db['Reservations']
        db.close()
    except:
        print("Unable to open storage.db")

    reservations_list = []
    for key in reservations_dict:
        reservation = reservations_dict.get(key)
        reservations_list.append(reservation)
    print(reservations_list)

    reviews_dict = {}
    try:
        db = shelve.open('review', 'r')
        reviews_dict = db ['Reviews']
        db.close()
        print(reviews_dict)
    except:
        print("Unable to open Reviews.db")

    reviews_list = []
    for key in reviews_dict:
        review = reviews_dict.get(key)
        reviews_list.append(review)
    print(reviews_list)
    return render_template('adm_retrieveReservation.html', count_review=len(reviews_list), reviews_list=reviews_list, count=len(reservations_list), reservations_list = reservations_list)

@app.route('/adm_updateReservation/<int:id>/', methods=['GET', 'POST'])
def update_Reservation(id):
    update_reservation_form = CreateReservationForm(request.form)
    update_date_reservation = ReservationDateForm(request.form)
    if request.method == 'POST' and update_reservation_form.validate():
        reservations_dict = {}
        db = shelve.open('Reservation.db')
        reservations_dict = db['Reservations']

        reservation = reservations_dict.get(id)
        reservation.set_first_name(update_reservation_form.first_name.data)
        reservation.set_last_name(update_reservation_form.last_name.data)
        reservation.set_email(update_reservation_form.email.data)
        reservation.set_contact(update_reservation_form.contact.data)
        reservation.set_date(update_date_reservation.date.data)
        reservation.set_time_slot(update_reservation_form.time_slot.data)
        reservation.set_remarks(update_reservation_form.remarks.data)
        db['Reservations'] = reservations_dict
        print(reservation.get_date())
        db.close()

        return redirect(url_for('adm_retrieveReservation'))
    else:
        reservations_dict = {}
        db = shelve.open('Reservation.db')
        reservations_dict = db['Reservations']
        db.close()

        reservation = reservations_dict.get(id)
        update_reservation_form.first_name.data = reservation.get_first_name()
        update_reservation_form.last_name.data = reservation.get_last_name()
        update_reservation_form.email.data = reservation.get_email()
        update_reservation_form.contact.data = reservation.get_contact()
        update_date_reservation.date.data = reservation.get_date()
        update_reservation_form.time_slot.data = reservation.get_time_slot()
        update_reservation_form.remarks.data = reservation.get_remarks()

        return render_template('adm_updateReservation.html', form=update_reservation_form, dateform = update_date_reservation)


@app.route('/confirmation')
def confirmationReservation():

    return render_template('confirmationReservation.html')

@app.route('/adm_deleteReservation/<int:id>', methods=['POST'])
def adm_deleteReservation(id):
    reservations_dict = {}
    db = shelve.open('Reservation.db')
    reservations_dict = db['Reservations']
    reservations_dict.pop(id)

    db['Reservations'] = reservations_dict
    db.close()

    return redirect(url_for('adm_retrieveReservation'))

@app.route('/adm_deleteReview/<id>', methods=['POST','GET'])
def adm_deleteReview(id):
    db = shelve.open('review', 'w')
    reviews_dict = db['Reviews']

    reviews_dict.pop(int(id))

    db['Reviews'] = reviews_dict
    db.close()

    return redirect(url_for('adm_retrieveReservation'))

# Data from cart, do whatever you want with it
# call the stored data in admin
@app.route('/payNowPls',methods=["GET","POST"])
def payNowPls():
    if request.method == 'POST':
        data = request.json
        menu = shelve.open("Menu.db")
        preOrder = menu
        preOrder[session["CurrentUsername"]] = data
        menu = preOrder
        menu.close()
        print(data)
        print("i am in pay now")
        return jsonify(data)
    return redirect(url_for('cart_confirmation'))

@app.route('/cart', methods = ["GET","POST"])
def cart():

    return render_template('AddCart.html')

@app.route('/cart_confirmation', methods = ["GET","POST"])
def cart_confirmation():

    return render_template('cart_confirmation.html')



@app.route('/adm_viewPreOrders', methods = ['POST','GET'])
def view_preOrder():
    menu = shelve.open('Menu.db')
    usernames = []
    for item in menu:
        usernames.append(item)

    return render_template('adm_viewPreOrders.html', preorders=usernames)

@app.route('/adm_viewPreOrdersDetails/<username>', methods = ['POST','GET'])
def preorderdetail(username):
    menu = shelve.open('Menu.db')
    orderDetails = menu[username]
    listing = []
    for i in orderDetails:
        listing.append(i)

    return render_template('adm_viewPreOrdersDetails.html', order=listing)










#Danish's part

@app.route('/hotelRooms')
def hotel_rooms():
    return render_template("hotel_rooms.html")

@app.route("/smallRoom",methods=['GET','POST'])
def small_room():
    form = BookingForm()
    roomList=[]
    guestDict={}
    inventories_dict = {}
    inventorydb = shelve.open('inventory.db', 'c')
    inventories_dict = inventorydb['Inventories']
    inventories_list = []
    inventory_name_list=[]
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)
        inventory_name_list.append(inventory.get_item_name())
    print(inventory_name_list)
    print(inventories_list)

    if request.method== "POST" and form.validate():
        try:
            roomdb = shelve.open("room.db")
            roomList = roomdb["SmallRoom"]
        except:
            print("No Small Rooms occupied.")
            roomList= []
            small_rooms=200
            for i in range(small_rooms):
                roomList.append(i)
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("No guests found.")
            guestDict={}



        chosen_items= request.form.getlist("checkbox")
        print(chosen_items)
        for item in chosen_items:
            if item in inventory_name_list:
                print(item+" is in inventory list, subtracting..")
                original_value= inventories_dict[item].get_quantity()
                print("BEFORE :",original_value)
                inventories_dict[item].set_quantity(original_value-1)
                print("AFTER : ",inventories_dict[item].get_quantity())
        roomsLeft=len(roomList)
        room_number= random.randint(roomList[0],roomList[-1])
        print(room_number)
        roomList.remove(room_number)
        roomdb["SmallRoom"] = roomList
        inventorydb['Inventories'] = inventories_dict
        session['bookindate'] = form.bookindate.data
        session['bookoutdate'] = form.bookoutdate.data
        session['room_choice'] = "Small Room"
        session['room_number'] = room_number
        return redirect(url_for('test_guest'))
    return render_template("small_room.html",form=form, inventories_list=inventories_list)


@app.route("/apartment", methods=['GET', 'POST'])
def apartment():
    form = BookingForm()
    roomList = []
    guestDict = {}
    inventories_dict = {}
    inventorydb = shelve.open('inventory.db', 'c')
    inventories_dict = inventorydb['Inventories']
    inventories_list = []
    inventory_name_list = []
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)
        inventory_name_list.append(inventory.get_item_name())
    print(inventory_name_list)
    print(inventories_list)
    if request.method == "POST" and form.validate():
        try:
            roomdb = shelve.open("room.db")
            roomList = roomdb["apartment"]
        except:
            print("No apartments occupied.")
            roomList = []
            apartments = 200
            for i in range(apartments):
                i=i+200
                roomList.append(i)
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("No guests found.")
            guestDict = {}

        chosen_items = request.form.getlist("checkbox")
        print(chosen_items)
        for item in chosen_items:
            if item in inventory_name_list:
                print(item + " is in inventory list, subtracting..")
                original_value = inventories_dict[item].get_quantity()
                print("BEFORE :", original_value)
                inventories_dict[item].set_quantity(original_value - 1)
                print("AFTER : ", inventories_dict[item].get_quantity())

        roomsLeft = len(roomList)
        room_number = random.randint(roomList[0], roomList[-1])
        print(room_number)
        roomList.remove(room_number)
        roomdb["apartment"] = roomList
        inventorydb['Inventories'] = inventories_dict
        session['bookindate'] = form.bookindate.data
        session['bookoutdate'] = form.bookoutdate.data
        session['room_choice'] = "Apartment"
        session['room_number'] = room_number
        return redirect(url_for('test_guest'))
    return render_template("apartment.html", form=form, inventories_list=inventories_list)


@app.route("/bigApartment", methods=['GET', 'POST'])
def big_apartment():
    form = BookingForm()
    roomList = []
    guestDict = {}
    inventories_dict = {}
    inventorydb = shelve.open('inventory.db', 'c')
    inventories_dict = inventorydb['Inventories']
    inventories_list = []
    inventory_name_list = []
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)
        inventory_name_list.append(inventory.get_item_name())
    print(inventory_name_list)
    print(inventories_list)
    if request.method == "POST" and form.validate():
        try:
            roomdb = shelve.open("room.db")
            roomList = roomdb["BigApartment"]
        except:
            print("No big apartments occupied.")
            roomList = []
            big_apartments = 200
            for i in range(big_apartments):
                i = i + 400
                roomList.append(i)
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("No guests found.")
            guestDict = {}

        chosen_items = request.form.getlist("checkbox")
        print(chosen_items)
        for item in chosen_items:
            if item in inventory_name_list:
                print(item + " is in inventory list, subtracting..")
                original_value = inventories_dict[item].get_quantity()
                print("BEFORE :", original_value)
                inventories_dict[item].set_quantity(original_value - 1)
                print("AFTER : ", inventories_dict[item].get_quantity())

        roomsLeft = len(roomList)
        room_number = random.randint(roomList[0], roomList[-1])
        print(room_number)
        roomList.remove(room_number)
        roomdb["BigApartment"] = roomList
        inventorydb['Inventories'] = inventories_dict
        session['bookindate'] = form.bookindate.data
        session['bookoutdate'] = form.bookoutdate.data
        session['room_choice'] = "Big Apartment"
        session['room_number'] = room_number
        return redirect(url_for('test_guest'))
    return render_template("big_apartment.html", form=form, inventories_list=inventories_list)


@app.route("/villa", methods=['GET', 'POST'])
def villa():
    form = BookingForm()
    roomList = []
    guestDict = {}
    inventories_dict = {}
    inventorydb = shelve.open('inventory.db', 'c')
    inventories_dict = inventorydb['Inventories']
    inventories_list = []
    inventory_name_list = []
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)
        inventory_name_list.append(inventory.get_item_name())
    print(inventory_name_list)
    print(inventories_list)
    if request.method == "POST" and form.validate():
        try:
            roomdb = shelve.open("room.db")
            roomList = roomdb["Villa"]
        except:
            print("No Small Rooms occupied.")
            roomList = []
            villas = 200
            for i in range(villas):
                i = i + 600
                roomList.append(i)
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("No guests found.")
            guestDict = {}

        chosen_items = request.form.getlist("checkbox")
        print(chosen_items)
        for item in chosen_items:
            if item in inventory_name_list:
                print(item + " is in inventory list, subtracting..")
                original_value = inventories_dict[item].get_quantity()
                print("BEFORE :", original_value)
                inventories_dict[item].set_quantity(original_value - 1)
                print("AFTER : ", inventories_dict[item].get_quantity())

        roomsLeft = len(roomList)
        room_number = random.randint(roomList[0], roomList[-1])
        print(room_number)
        roomList.remove(room_number)
        roomdb["Villa"] = roomList
        inventorydb['Inventories'] = inventories_dict
        session['bookindate'] = form.bookindate.data
        session['bookoutdate'] = form.bookoutdate.data
        session['room_choice'] = "Villa"
        session['room_number'] = room_number
        return redirect(url_for('test_guest'))
    return render_template("villa.html", form=form, inventories_list=inventories_list)




@app.route("/server-dash")
def server_dash():
    return render_template("server_rooms.html")

@app.route("/book-rooms",methods=['GET','POST'])
def room_booking():
    form = BookingForm()
    if request.method== "POST" and form.validate():
        session['bookindate'] = form.bookindate.data
        session['bookoutdate'] = form.bookoutdate.data
        session['room_choice'] = form.roomname.data
        print("hello world")
        return redirect(url_for('date'))
    return render_template("booking_rooms.html",form=form)

@app.route('/finish', methods=['GET','POST'])
def date():
    startdate = session['bookindate']
    enddate = session['bookoutdate']
    return render_template('finish.html')

# @app.route('/thanks')
# def thanks():
#     return render_template("")

@app.route('/server-home')
def server_home():
    return render_template("server_rooms.html")

@app.route('/guest-list')
def server_guests():
    guestDict={}
    db=shelve.open("guests.db")
    try:
        guestDict=db["Guests"]
    except:
        print("No guests found.")
        guestDict={}

    guest_list=[]
    for key in guestDict:
        guest=guestDict.get(key)
        guest_list.append(guest)

    # How to count number of hospitals
    hospital_list=[]
    hospitalDict={}
    try:
        hospitalDict=db["Guests"]
    except:
        hospitalDict={}
    for key in hospitalDict:
        guest=hospitalDict.get(key)
        hospital=guest.get_location()
        hospital_list.append(hospital)
    hosp = dict(Counter(hospital_list))
    db.close()
    return render_template("guest_list.html",guest_list=guest_list,count=len(guest_list),hosp=hosp)


@app.route('/test-guest', methods=["GET","POST"])
def test_guest():
    createBooking=GuestBooking(request.form)
    form=GuestBooking()
    hospital_list=[]
    hospitaldb = shelve.open("hospital.db")
    occupation_list = []
    occupationdb=shelve.open("occupation.db")
    industry_list=[]
    error=""
    try:
        hospital_list = hospitaldb["Hospital_choices"]

    except:
        print("Restoring default hospitals.")
        hospitaldb["Hospital_choices"] = Hospital.hospitalList
        hospital_list = hospitaldb["Hospital_choices"]

    try:
        occupation_list = occupationdb["Occupation_choices"]
        industry_list= occupationdb["Industry_choices"]

    except:
        print("Restoring default occupations and industries.")
        occupationdb["Occupation_choices"] = Occupation.occupationList
        occupationdb["Industry_choices"] = Industry.industryList
        industry_list= occupationdb["Industry_choices"]
        occupation_list = occupationdb["Occupation_choices"]

    print(hospital_list)
    print(occupation_list)
    hospitalChoices=list(zip(hospital_list,hospital_list))
    occupationChoices=list(zip(occupation_list,occupation_list))
    industryChoices = list(zip(industry_list, industry_list))
    createBooking.location.choices = hospitalChoices
    createBooking.occupation.choices = occupationChoices
    createBooking.industry.choices= industryChoices
    print(createBooking.industry.choices)
    form.location.choices = hospitalChoices
    form.occupation.choices = occupationChoices
    form.industry.choices=industryChoices


    if request.method== "POST" and createBooking.validate():
        guestDict = {}
        db = shelve.open("guests.db")
        guest_id=0
        guestDict2 = {}

        try:
            guestDict = db["Guests"]
            guest_id=int(db["guest_id"])
            guestDict2 = db["Guest_RoomNumber"]
        except:
            print("Error in Guest Database. Try again.")


        guest = Guest(session["Name"],createBooking.industry.data,createBooking.occupation.data,createBooking.location.data,createBooking.transport.data)
        guest.set_name(session["Name"])
        guest.set_email(session["Email"])
        guest.set_deals(session["Deals"])
        guest.set_username(session["CurrentUsername"])
        guest.set_check_in(session["bookindate"])
        guest.set_check_out(session["bookoutdate"])
        guest_id+=1
        guest.set_guest_id(guest_id)
        guest.set_room_number(session['room_number'])
        guest.set_room_type(session['room_choice'])
        db["guest_id"] = guest_id
        guestDict[guest.get_guest_id()] = guest
        guestDict2[guest.get_room_number()] = guest
        db["Guest_RoomNumber"] = guestDict2
        db["Guests"] = guestDict
        hospitaldb.close()
        db.close()
        return redirect(url_for('server_guests'))


    elif request.method=="POST" and createBooking.validate()==False:
        error = createBooking.errors["transport"]

    return render_template("booking_details.html",form=form,error=error)



@app.route('/grade-assign/<int:id>',methods=["GET","POST"])
def assign_grade(id):
    gradeForm= GradeForm(request.form)
    createBooking = GuestBooking(request.form)
    createRoomType = BookRoomType(request.form)
    hospital_list=[]
    hospitaldb = shelve.open("hospital.db")
    occupation_list = []
    occupationdb=shelve.open("occupation.db")
    hospital_list = hospitaldb["Hospital_choices"]
    occupation_list = occupationdb["Occupation_choices"]
    hospitalChoices=list(zip(hospital_list,hospital_list))
    occupationChoices=list(zip(occupation_list,occupation_list))
    createBooking.location.choices = hospitalChoices
    createBooking.occupation.choices = occupationChoices

    if request.method== "POST" and gradeForm.validate():
        guestDict={}
        guestDict2={}
        try:
            db=shelve.open("guests.db")
            guestDict = db["Guests"]
            guestDict2= db["Guest_RoomNumber"]
        except:
            print("Error opening guest database.")

        guest=guestDict.get(id)
        guest.set_grade(gradeForm.grade.data)
        guest.set_priority(gradeForm.priority.data)
        guest2 = guestDict2.get(guest.get_room_number())
        guest2.set_grade(gradeForm.grade.data)
        guest2.set_priority(gradeForm.priority.data)
        db["Guests"]= guestDict
        db["Guest_RoomNumber"] = guestDict2
        db.close()
        return redirect(url_for('server_guests'))
    else:
        guestDict = {}
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("Error opening guests database.")

        guest=guestDict.get(id)
        createRoomType.room_number.data = guest.get_room_number()
        createRoomType.room_type.data = guest.get_room_type()
        createBooking.occupation.data = guest.get_occupation()
        createBooking.industry.data = guest.get_industry()
        createBooking.location.data = guest.get_location()
        createBooking.transport.data = guest.get_transport()
        gradeForm.grade.data = guest.get_grade()
        gradeForm.priority.data = guest.get_priority()



        return render_template('grade_legend.html',guest=guest,form=gradeForm,guestForm=createBooking)

@app.route('/edit-guest/<int:id>',methods=["GET","POST"])
def edit_guest(id):
    gradeForm= GradeForm(request.form)
    createBooking = GuestBooking(request.form)
    createCheckInOut = BookingForm(request.form)
    createRoomType = BookRoomType(request.form)
    hospital_list=[]
    hospitaldb = shelve.open("hospital.db")
    occupation_list = []
    industry_list=[]
    occupationdb=shelve.open("occupation.db")
    hospital_list = hospitaldb["Hospital_choices"]
    occupation_list = occupationdb["Occupation_choices"]
    industry_list= occupationdb["Industry_choices"]
    industryChoices = list(zip(industry_list, industry_list))
    hospitalChoices=list(zip(hospital_list,hospital_list))
    occupationChoices=list(zip(occupation_list,occupation_list))
    createBooking.location.choices = hospitalChoices
    createBooking.occupation.choices = occupationChoices
    createBooking.industry.choices = industryChoices

    if request.method== "POST" and createBooking.validate():
        guestDict={}
        try:
            db=shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("Error opening guest database.")
        guest=guestDict.get(id)
        guest.set_room_number(createRoomType.room_number.data)
        guest.set_room_type(createRoomType.room_type.data)
        guest.set_occupation(createBooking.occupation.data)
        guest.set_industry(createBooking.industry.data)
        guest.set_location(createBooking.location.data)
        guest.set_transport(createBooking.transport.data)
        db["Guests"]= guestDict
        db.close()
        return redirect(url_for('server_guests'))
    else:
        guestDict = {}
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("Error opening guests database.")

        guest=guestDict.get(id)
        createRoomType.room_number.data = guest.get_room_number()
        createRoomType.room_type.data = guest.get_room_type()
        createBooking.occupation.data=guest.get_occupation()
        createBooking.industry.data = guest.get_industry()
        createBooking.location.data = guest.get_location()
        createBooking.transport.data = guest.get_transport()
        gradeForm.grade.data = guest.get_grade()
        gradeForm.priority.data = guest.get_priority()
        db.close()



        return render_template('guest_edit.html',guest=guest,form=createBooking,guestForm=gradeForm,checkInOut=createCheckInOut, roomType=createRoomType)


@app.route('/edit-checkInOut/<int:id>', methods=["GET", "POST"])
def edit_checkInOut(id):
    createCheckInOut = BookingForm(request.form)

    if request.method == "POST" and createCheckInOut.validate():
        guestDict = {}
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("Error opening guest database.")
        guest = guestDict.get(id)
        guest.set_check_in(createCheckInOut.bookindate.data)
        guest.set_check_out(createCheckInOut.bookoutdate.data)
        db["Guests"] = guestDict
        db.close()
        return redirect(url_for('server_guests'))
    else:
        guestDict = {}
        try:
            db = shelve.open("guests.db")
            guestDict = db["Guests"]
        except:
            print("Error opening guests database.")

        guest = guestDict.get(id)
        db.close()

        return render_template('checkInOut_edit.html', guest=guest, form=createCheckInOut)


@app.route('/delete-guest/<int:id>', methods=['POST'])
def delete_guest(id):
    guest_dict = {}
    db = shelve.open("guests.db")
    guest_dict = db["Guests"]

    guest_dict.pop(id)

    db["Guests"] = guest_dict
    db.close()

    return redirect(url_for('server_guests'))

@app.route('/delete-gp/<int:id>', methods=['POST'])
def delete_gp(id):
    guest_dict = {}
    db = shelve.open("guests.db")
    guest_dict = db["Guests"]

    guest = guest_dict.get(id)

    guest.set_grade("")
    guest.set_priority("")

    db["Guests"] = guest_dict
    db.close()

    return redirect(url_for('server_guests'))

@app.route("/hospital-search",methods=["GET","POST"])
def hospital_search():
    if request.method == 'POST':
        data=request.json
        print("succesS?")
    return render_template("hospital_search.html")


@app.route("/hospital-select", methods=["GET", "POST"])
def hospital_select():
    if request.method == 'POST':
        hospitaldb=shelve.open("hospital.db")
        data = request.json
        hospitaldb["hospital_search"] = data
        print(data)
        return jsonify(data)
    return redirect(url_for('cart_confirm'))

@app.route('/cart-confirm',methods = ["GET","POST"])
def cart_confirm():
    return render_template("cart_confirm.html")




# @app.route('/requestSelectGuest')
# def request_selectguest():
#     guestDict = {}
#     db = shelve.open("guests.db")
#     try:
#         guestDict = db["Guest_RoomNumber"]
#     except:
#         print("No guests found.")
#         guestDict = {}
#
#     guest_list = []
#     for key in guestDict:
#         guest = guestDict.get(key)
#         guest_list.append(guest)
#     db.close()
#     return render_template("request_selectguest.html", guest_list=guest_list, guest=guest)

@app.route("/hospital-create",methods=["GET","POST"])
def hospital_create():
    createHospital= HospitalForm(request.form)
    hospital_list = []
    hospitaldb = shelve.open("hospital.db")
    hospital_dict = {}
    data = hospitaldb["hospital_search"]
    split_name=data.split(", ")
    hospital_name=""
    for i in split_name:
        if "Hospital" in i:
            hospital_name=i
    print("This is data from hospital create : ",data)
    params= {
        "key" : "AIzaSyCO5-kE5NU-8iLRbhk-nG5vgcWedjXgPMg",
        "address" : data

    }
    base_url ="https://maps.googleapis.com/maps/api/geocode/json?"
    #API Call
    response = requests.get(base_url,params=params).json()
    response.keys()
    try:
        hospital_address= response["results"][0]["formatted_address"]
    except:
        print("No address found.")
        hospital_address=data
    if request.method== "POST" and createHospital.validate():
        try:
            hospital_list = hospitaldb["Hospital_choices"]
            hospital_dict=hospitaldb["Hospitals"]
            hospital_id= int(hospitaldb["hospital_id"])
        except:
            print("Error in retrieving database. Restoring default hospitals.")
            hospitaldb["Hospital_choices"] = Hospital.hospitalList
            hospital_id = 1
            for x in Hospital.hospitalDict:
                hospital = Hospital(x["Name"], x["Address"], x["Contact"], x["Beds"])
                hospital_dict[hospital_id] = hospital
                hospital.set_hospital_id(hospital_id)
                hospital_id += 1
            hospitaldb["hospital_id"] = hospital_id
            hospitaldb["Hospitals"] = hospital_dict
            hospital_list = hospitaldb["Hospital_choices"]

        hospital_id += 1
        hospital_name=createHospital.hospital_name.data
        hospital_address = createHospital.hospital_address.data
        hospital = Hospital(createHospital.hospital_name.data, createHospital.hospital_address.data,createHospital.hospital_contact.data,createHospital.hospital_beds.data)
        print(createHospital.hospital_contact.data)
        hospital.set_hospital_id(hospital_id)
        hospital_list.append(hospital.get_name())
        print(hospital_list)
        hospital_dict[hospital.get_hospital_id()] = hospital
        hospitaldb["hospital_id"]=hospital_id
        hospitaldb["Hospitals"] = hospital_dict
        hospitaldb["Hospital_choices"]=hospital_list
        hospitaldb.close()
        return redirect(url_for('hospital_list'))
    return render_template("hospital_create.html",form=createHospital,data=data,hospital_name=hospital_name,hospital_address=hospital_address)

@app.route('/delete-hospital/<int:id>', methods=['POST'])
def delete_hospital(id):
    hospital_dict = {}
    hospital_choices=[]
    hospitaldb = shelve.open("hospital.db")
    hospital_dict = hospitaldb["Hospitals"]
    hospital_choices=hospitaldb["Hospital_choices"]
    print("BEFORE DELETE")
    print(hospital_choices)
    hospital_name = hospital_dict[id].get_name()
    hospital_dict.pop(id)
    hospital_choices.remove(hospital_name)
    print("AFTER DELETE")
    print(hospital_choices)
    hospitaldb["Hospitals"] = hospital_dict
    hospitaldb["Hospital_choices"]=hospital_choices
    hospitaldb.close()

    return redirect(url_for('hospital_list'))

@app.route('/deletemulti',methods=["GET", "POST"])
def hospital_multi():
    hospital_dict = {}
    hospital_choices = []
    hospital_name=""
    hospitaldb = shelve.open("hospital.db")
    hospital_dict = hospitaldb["Hospitals"]
    hospital_choices = hospitaldb["Hospital_choices"]
    print("This is the hospital choices")
    print(hospital_dict)

    if request.method == 'POST':
        data = request.json
        for x in data:
            hospital_name=hospital_dict[int(x)].get_name()
            hospital_dict.pop(int(x))
            hospital_choices.remove(hospital_name)

        hospitaldb["Hospitals"] = hospital_dict
        print(hospital_choices)
        hospitaldb["Hospital_choices"] = hospital_choices
        hospitaldb.close()
        return jsonify(data)
    return redirect(url_for('hospital_list'))

@app.route('/hospital-reset', methods=["POST"])
def hospital_reset():
    hospitaldb = shelve.open("hospital.db")
    hospital_Dict = {}
    hospital_id = int(hospitaldb["hospital_id"])
    print("Resetting hospitals.")
    hospital_id = 0
    hospitaldb["Hospital_choices"] = Hospital.hospitalList
    for x in Hospital.hospitalDict:
        hospital = Hospital(x["Name"], x["Address"], x["Contact"], x["Beds"])
        hospital_Dict[hospital_id] = hospital
        hospital.set_hospital_id(hospital_id)
        hospital_id += 1
        print(hospital_id)
    hospital_id -= 1
    hospitaldb["hospital_id"] = hospital_id
    hospitaldb["Hospitals"] = hospital_Dict
    hospitaldb.close()
    return redirect(url_for('hospital_list'))



@app.route('/hospital-list')
def hospital_list():
    createHospital = HospitalForm(request.form)
    hospitaldb = shelve.open("hospital.db")
    db = shelve.open("guests.db")
    hospital_list = []
    hospital_Dict = {}
    amount_list = []

    try:
        hospital_Dict = hospitaldb["Hospitals"]
        hospital_id = int(hospitaldb["hospital_id"])
    except:
        print("Error loading hospitals. Resetting hospitals.")
        hospital_id = 0
        hospitaldb["Hospital_choices"] = Hospital.hospitalList
        for x in Hospital.hospitalDict:
            hospital = Hospital(x["Name"], x["Address"], x["Contact"], x["Beds"])
            hospital_Dict[hospital_id] = hospital
            hospital.set_hospital_id(hospital_id)
            hospital_id += 1
            print(hospital_id)

        hospital_id-=1
        hospitaldb["hospital_id"] = hospital_id
        hospitaldb["Hospitals"] = hospital_Dict


        print(hospitaldb["Hospital_choices"])

    # Count number of hospitals
    try:
        guestDict = db["Guests"]
    except:
        guestDict = {}
    for key in guestDict:
        guest = guestDict.get(key)
        amount = guest.get_location()
        amount_list.append(amount)
    hosp = dict(Counter(amount_list))

    # Count number of vehicles assigned in hospitals
    try:
        vehicle_list=[]
        vehicledb = shelve.open("Vehicles")
        vehicle_dict = vehicledb["Vehicles"]
    except:
        vehicle_dict = {}
    for key in vehicle_dict:
        vehicle = vehicle_dict.get(key)
        hospital_assignment = vehicle.get_location()
        vehicle_list.append(hospital_assignment)
    hospital_assigned = dict(Counter(vehicle_list))

    for key in hospital_Dict:
        hospital = hospital_Dict.get(key)
        hospital_list.append(hospital)

    # hosp = dict(Counter(hospital_list))
    hospitaldb.close()
    db.close()
    return render_template("hospital_list.html", hospital_list=hospital_list, hosp=hosp, hospital_assigned=hospital_assigned)

@app.route('/hospital-edit/<int:id>',methods=["GET","POST"])
def hospital_edit(id):
    createHospital = HospitalEditForm(request.form)
    if request.method== "POST" and createHospital.validate():
        hospitalDict={}
        hospital_list=[]
        try:
            hospitaldb=shelve.open("hospital.db")
            hospitalDict = hospitaldb["Hospitals"]
            hospital_list = hospitaldb["Hospital_choices"]
        except:
            print("Error opening hospital database.")

        hospital=hospitalDict.get(id)
        hospital.set_name(createHospital.hospital_name.data)
        hospital_list[id] = createHospital.hospital_name.data
        hospital.set_address(createHospital.hospital_address.data)
        hospital.set_contact(createHospital.hospital_contact.data)
        hospital.set_beds(createHospital.hospital_beds.data)
        hospitaldb["Hospitals"]= hospitalDict
        hospitaldb["Hospital_choices"] = hospital_list
        hospitaldb.close()
        return redirect(url_for('hospital_list'))
    else:
        print("2nd option desu")
        hospitalDict = {}
        print(createHospital.errors.items())
        try:
            hospitaldb = shelve.open("hospital.db")
            hospitalDict = hospitaldb["Hospitals"]
        except:
            print("Error opening hospital database.")

        hospital=hospitalDict.get(id)
        createHospital.hospital_name.data=hospital.get_name()
        createHospital.hospital_address.data=hospital.get_address()
        createHospital.hospital_contact.data = hospital.get_contact()
        createHospital.hospital_beds.data = hospital.get_beds()



        return render_template('hospital_edit.html',hospital=hospital,form=createHospital)


@app.route('/occupation-list')
def occupation_list():
    createOccupation = OccupationForm(request.form)
    occupationdb = shelve.open("occupation.db")
    occupation_list = []
    occupation_Dict = {}
    try:
        occupation_Dict = occupationdb["Occupations"]
        occupation_id = int(occupationdb["occupation_id"])
    except:
        print("Error loading occupations in occupations list. Resetting occupations.")
        occupation_id = 1
        occupationdb["Occupation_choices"] = Occupation.occupationList
        for x in Occupation.occupationDict:
            print(occupation_id)
            occupation = Occupation(x["Occupation"],x["Industry"])
            occupation_Dict[occupation_id] = occupation
            occupation.set_occupation_id(occupation_id)
            occupation_id += 1
        occupation_id-=1
        occupationdb["occupation_id"] = occupation_id
        occupationdb["Occupations"] = occupation_Dict


    print(occupation_Dict)

    for key in occupation_Dict:
        occupation = occupation_Dict.get(key)
        occupation_list.append(occupation)
    print(occupation_list)

    # hosp = dict(Counter(hospital_list))
    occupationdb.close()
    return render_template("occupation_list.html", occupation_list=occupation_list)


@app.route("/occupation-create",methods=["GET","POST"])
def occupation_create():
    createOccupation= OccupationForm(request.form)
    occupation_list = []
    occupationdb = shelve.open("occupation.db")
    occupation_dict = {}
    industry_list = []
    try:
        industry_list = occupationdb["Industry_choices"]
    except:
        print("Error in loading industries. Resetting..")
        occupationdb["Industry_choices"] = Industry.industryList
        industry_list = occupationdb["Industry_choices"]

    industryChoices = list(zip(industry_list, industry_list))
    createOccupation.occupation_industry.choices = industryChoices
    print(industryChoices)


    if request.method== "POST" and createOccupation.validate():
        try:
            occupation_list = occupationdb["Occupation_choices"]
            occupation_dict=occupationdb["Occupations"]
            occupation_id= int(occupationdb["occupation_id"])
        except:
            print("Error in retrieving database. Restoring default occupations and industries.")
            occupation_id = 1
            print(occupation_id)
            for x in Occupation.occupationDict:
                occupation = Occupation(x["Occupation"],x["Industry"])
                occupation_dict[occupation_id] = occupation
                occupation.set_occupation_id(occupation_id)
                occupation_id += 1
            occupation_id-=1
            occupationdb["occupation_id"] = occupation_id
            occupationdb["Occupations"] = occupation_dict
            occupation_list = occupationdb["Occupation_choices"]

        occupation = Occupation(createOccupation.occupation_name.data,createOccupation.occupation_industry.data)
        occupation_id+=1
        occupation.set_description(createOccupation.description.data)
        occupation.set_occupation_id(occupation_id)
        occupation_list.append(occupation.get_occupation())
        print(occupation_list)
        occupation_dict[occupation.get_occupation_id()] = occupation
        occupationdb["occupation_id"] = occupation_id
        occupationdb["Occupations"] = occupation_dict
        occupationdb["Occupation_choices"] = occupation_list
        occupationdb.close()
        return redirect(url_for('occupation_list'))
    return render_template("occupation_create.html",form=createOccupation)


@app.route("/industry-create", methods=["GET", "POST"])
def industry_create():
    createIndustry = IndustryForm(request.form)
    if request.method == "POST" and createIndustry.validate():
        industry_list = []
        industrydb = shelve.open("occupation.db")
        industry_dict = {}
        try:
            industry_list = industrydb["Industry_choices"]
            industry_dict = industrydb["Industries"]
            industry_id = int(industrydb["industry_id"])
        except:
            print("Error in retrieving database. Restoring default industries.")
            industrydb["Industry_choices"] = Industry.industryList
            industry_id = 1
            print(industry_id)
            for x in Industry.industryDict:
                industry = Industry(x["Industry"])
                industry_dict[industry_id] = industry
                industry.set_industry_id(industry_id)
                industry_id += 1
            industry_id -= 1
            industrydb["industry_id"] = industry_id
            industrydb["Industries"] = industry_dict
            industry_list = industrydb["Industry_choices"]

        industry = Industry(createIndustry.industry_name.data)
        industry_id += 1
        industry.set_industry_id(industry_id)
        industry_list.append(industry.get_industry())
        print(industry_list)
        industry_dict[industry.get_industry_id()] = industry
        industrydb["industry_id"] = industry_id
        industrydb["Industries"] = industry_dict
        industrydb["Industry_choices"] = industry_list
        industrydb.close()
        return redirect(url_for('occupation_list'))
    return render_template("industry_create.html", form=createIndustry)

@app.route('/occupation-edit/<int:id>',methods=["GET","POST"])
def occupation_edit(id):
    createOccupation= OccupationEditForm(request.form)
    occupation_list = []
    occupationdb = shelve.open("occupation.db")
    occupation_dict = {}
    industry_list = []
    try:
        industry_list = occupationdb["Industry_choices"]
    except:
        print("Error in loading industries. Resetting..")
        occupationdb["Industry_choices"] = Industry.industryList
        industry_list = occupationdb["Industry_choices"]

    industryChoices = list(zip(industry_list, industry_list))
    createOccupation.occupation_industry.choices = industryChoices
    print(industryChoices)
    if request.method== "POST" and createOccupation.validate():
        occupationDict={}
        occupation_list=[]
        try:
            occupationdb=shelve.open("occupation.db")
            occupationDict = occupationdb["Occupations"]
            occupation_list = occupationdb["Occupation_choices"]
            print(occupation_list)
        except:
            print("Error opening Occupation database.")

        occupation=occupationDict.get(id)
        test=occupation.get_occupation()
        occupation.set_occupation(createOccupation.occupation_name.data)
        occupation.set_description(createOccupation.description.data)
        occupation_list.remove(test)
        occupation_list.append(createOccupation.occupation_name.data)
        print(occupation_list)
        occupation.set_industry(createOccupation.occupation_industry.data)
        occupationdb["Occupations"]= occupationDict
        occupationdb["Occupation_choices"] = occupation_list
        occupationdb.close()
        return redirect(url_for('occupation_list'))
    else:
        print("2nd option desu")
        occupationDict = {}
        try:
            occupationdb = shelve.open("occupation.db")
            occupationDict = occupationdb["Occupations"]
        except:
            print("Error opening occupation database.")

        occupation=occupationDict.get(id)
        createOccupation.occupation_name.data=occupation.get_occupation()
        createOccupation.occupation_industry.data=occupation.get_industry()
        createOccupation.description.data=occupation.get_description()

        return render_template('occupation_edit.html',occupation=occupation,form=createOccupation)


@app.route('/delete-occupation/<int:id>', methods=['POST'])
def delete_occupation(id):
    occupation_dict = {}
    occupation_choices=[]
    occupationdb = shelve.open("occupation.db")
    occupation_dict = occupationdb["Occupations"]
    occupation_choices=occupationdb["Occupation_choices"]

    occupation_name = occupation_dict[id].get_occupation()
    occupation_dict.pop(id)
    occupation_choices.remove(occupation_name)

    occupationdb["Occupations"] = occupation_dict
    occupationdb["Occupation_choices"] = occupation_choices
    occupationdb.close()
    return redirect(url_for('occupation_list'))

@app.route('/occupation_multi',methods=["GET", "POST"])
def occupation_multi():
    occupation_dict = {}
    occupation_choices = []
    occupation_name=""
    occupationdb = shelve.open("occupation.db")
    occupation_dict = occupationdb["Occupations"]
    occupation_choices = occupationdb["Occupation_choices"]

    if request.method == 'POST':
        data = request.json
        for x in data:
            occupation_name=occupation_dict[int(x)].get_occupation()
            occupation_dict.pop(int(x))
            occupation_choices.remove(occupation_name)

        occupationdb["Occupations"] = occupation_dict
        print(occupation_choices)
        print("hello")
        occupationdb["Occupation_choices"] = occupation_choices
        occupationdb.close()
        return jsonify(data)
    return redirect(url_for('occupation_list'))

@app.route('/occupation-reset', methods=["POST"])
def occupation_reset():
    occupationdb = shelve.open("occupation.db")
    occupation_Dict = {}
    occupation_id = int(occupationdb["occupation_id"])
    print("Resetting occupations using the reset button.")
    occupation_id = 1
    print(occupation_id)
    occupationdb["Occupation_choices"] = Occupation.occupationList
    for x in Occupation.occupationDict:
        occupation = Occupation(x["Occupation"], x["Industry"])
        occupation_Dict[occupation_id] = occupation
        occupation.set_occupation_id(occupation_id)
        occupation_id += 1
        print(occupation_id)
    occupation_id -= 1
    occupationdb["occupation_id"] = occupation_id
    occupationdb["Occupations"] = occupation_Dict
    occupationdb.close()
    return redirect(url_for('occupation_list'))


@app.route('/rooms-list')
def rooms_list():
    roomsDict={}
    roomsdb=shelve.open("rooms.db")
    db=shelve.open("guests.db")

    try:
        roomsDict=roomsdb["emptyRooms"]
    except:
        roomsDict={}

    rooms_list=[]
    for key in roomsDict:
        rooms=roomsDict.get(key)
        rooms_list.append(rooms)

    # How to count number of hospitals
    # hospital_list=[]
    # hospitalDict={}
    # hospitalDict=db["Guests"]
    # for key in hospitalDict:
    #     guest=hospitalDict.get(key)
    #     hospital=guest.get_location()
    #     hospital_list.append(hospital)
    # hosp = dict(Counter(hospital_list))
    roomsdb.close()
    return render_template("rooms_list.html",rooms_list=rooms_list,count=len(rooms_list))

@app.route("/vehicle-create", methods = ["GET", "POST"])
def vehicle_create():
    createVehicle = VehicleForm(request.form)
    hospitaldb = shelve.open("hospital.db")
    hospital_list = hospitaldb["Hospital_choices"]
    hospitalChoices = list(zip(hospital_list, hospital_list))
    createVehicle.vehicle_location.choices = hospitalChoices

    if request.method == "POST" and createVehicle.validate():
        vehicle_list = []
        vehicledb = shelve.open("Vehicles")
        vehicle_dict = {}
        try:
            vehicle_list = vehicledb["vehicle_choices"]
            vehicle_dict = vehicledb["Vehicles"]
            vehicle_id = int(vehicledb["vehicle_id"])
        except:
            vehicle_list = []
            vehicle_dict = {}
            vehicle_id = 0

        vehicle = Vehicle(createVehicle.vehicle_name.data, createVehicle.vehicle_model.data, createVehicle.vehicle_car_plate.data, createVehicle.vehicle_contact.data, createVehicle.vehicle_location.data)
        vehicle_id += 1
        vehicle.set_vehicle_id(vehicle_id)
        vehicle_list.append(vehicle.get_vehicle_id())
        print(vehicle_list)
        vehicle_dict[vehicle.get_vehicle_id()] = vehicle
        vehicledb["vehicle_id"] = vehicle_id
        vehicledb["Vehicles"] = vehicle_dict
        vehicledb["vehicle_choices"] = vehicle_list
        vehicledb.close()
        return redirect(url_for('vehicle_list'))
    return render_template("vehicle_create.html", form=createVehicle)

@app.route('/vehicle-edit/<int:id>', methods = ["GET", "POST"])
def vehicle_edit(id):
    hospital_list = []
    hospitaldb = shelve.open("hospital.db")
    hospital_list = hospitaldb["Hospital_choices"]
    hospitalChoices = list(zip(hospital_list, hospital_list))
    createVehicle = VehicleForm(request.form)
    createVehicle.vehicle_location.choices = hospitalChoices
    if request.method== "POST" and createVehicle.validate():
        vehicleDict={}
        vehicle_list=[]

        try:
            vehicledb=shelve.open("Vehicles")
            vehicleDict = vehicledb["Vehicles"]
            vehicle_list = vehicledb["Vehicle_choices"]
            print(vehicle_list)
        except:
            print("Error opening Vehicle database.")

        vehicle=vehicleDict.get(id)
        test = vehicle.get_vehicle_id()
        vehicle.set_name(createVehicle.vehicle_name.data)
        vehicle.set_model(createVehicle.vehicle_model.data)
        vehicle.set_car_plate(createVehicle.vehicle_car_plate.data)
        vehicle.set_contact(createVehicle.vehicle_contact.data)
        vehicle.set_location(createVehicle.vehicle_location.data)
        createVehicle.vehicle_location.choices = hospitalChoices
        vehicle_list.append(createVehicle.vehicle_name.data)
        print(vehicle_list)
        vehicledb["Vehicles"]= vehicleDict
        vehicledb["Vehicle_choices"] = vehicle_list
        vehicledb.close()
        return redirect(url_for('vehicle_list'))
    else:
        print("2nd option desu")
        vehicleDict = {}
        try:
            vehicledb = shelve.open("Vehicles")
            vehicleDict = vehicledb["Vehicles"]
        except:
            print("Error opening vehicle database.")

        vehicle=vehicleDict.get(id)
        createVehicle.vehicle_name.data=vehicle.get_name()
        createVehicle.vehicle_model.data=vehicle.get_model()
        createVehicle.vehicle_car_plate.data = vehicle.get_car_plate()
        createVehicle.vehicle_contact.data = vehicle.get_contact()
        createVehicle.vehicle_location.data = vehicle.get_location()

        return render_template('vehicle_edit.html',vehicle=vehicle,form=createVehicle)

@app.route('/delete-vehicle/<int:id>', methods=['POST'])
def delete_vehicle(id):
    vehicle_dict = {}

    vehicledb = shelve.open("Vehicles")
    vehicle_dict = vehicledb["Vehicles"]

    print(vehicle_dict)

    vehicle_dict.pop(id)


    vehicledb["Vehicles"] = vehicle_dict

    vehicledb.close()
    return redirect(url_for('vehicle_list'))

@app.route('/vehicle-list')
def vehicle_list():
    vehicleDict = {}
    db = shelve.open("Vehicles")
    try:
        vehicleDict = db["Vehicles"]
    except:
        print("No vehicles found.")
        vehicleDict = {}

    vehicle_list = []
    print(vehicleDict)
    for key in vehicleDict:
        vehicle = vehicleDict.get(key)
        vehicle_list.append(vehicle)

    hospital_list = []
    for key in vehicleDict:
        guest = vehicleDict.get(key)
        hospital = guest.get_location()
        hospital_list.append(hospital)
    hosp = dict(Counter(hospital_list))

    db.close()

    return render_template("vehicle_list.html",vehicle_list=vehicle_list, hosp=hosp)


@app.route('/request-list')
def request_list():
    requestDict={}
    requestdb=shelve.open("requests.db")
    try:
        requestDict=requestdb["Requests"]
    except:
        print("No requests found.")
        requestDict={}

    request_list=[]
    for key in requestDict:
        request=requestDict.get(key)
        request_list.append(request)

    requestdb.close()
    return render_template("request_list.html",request_list=request_list,count=len(request_list))

@app.route('/requestSelectGuest')
def request_selectguest():
    guestDict = {}
    db = shelve.open("guests.db")
    try:
        guestDict=db["Guest_RoomNumber"]
    except:
        print("No guests found.")
        guestDict = {}

    guest_list = []
    for key in guestDict:
        guest = guestDict.get(key)
        guest_list.append(guest)
    db.close()
    return render_template("request_selectguest.html",guest_list=guest_list,guest=guest)



@app.route('/request-create/<int:roomnum>', methods=["GET","POST"])
def create_request(roomnum):
    createRequest=RequestForm(request.form)

    if request.method== "POST" and createRequest.validate():
        print("1st choice")
        guestDict={}
        request_id = 0
        requestDict = {}
        try:
            db=shelve.open("guests.db")
            guestDict=db["Guest_RoomNumber"]
            print(guestDict)
        except:
            print("No guests found.")

        try:
            requestdb=shelve.open("requests.db")
            requestDict=requestdb["Requests"]
            print(requestDict)
        except:
            print("No requests found.")
        guest = guestDict.get(roomnum)
        print(guest)
        guest.set_request_type(createRequest.type.data)
        guest.set_request_topic(createRequest.topic.data)
        guest.set_request_details(createRequest.details.data)
        request_id+=1
        guest.set_request_id(request_id)
        requestDict[guest.get_request_id()] = guest
        requestdb["Requests"] = requestDict
        db.close()
        requestdb.close()
        return redirect(url_for('request_list'))
    else:
        print("2nd choice of creating request")
        guestDict = {}
        requestDict = {}
        try:
            db=shelve.open("guests.db")
            guestDict=db["Guest_RoomNumber"]
            guestDict2=db["Guests"]
            print(guestDict)
            print(guestDict2)
        except:
            print("No guests found.")

        try:
            requestdb=shelve.open("requests.db")
            requestDict=requestdb["Requests"]
            print(requestDict)
        except:
            print("No requests found.")
            request_id=0
        guest = guestDict.get(roomnum)

        createRequest.type.data = guest.get_request_type()
        createRequest.topic.data = guest.get_request_topic()
        createRequest.details.data = guest.get_request_details()

        requestdb.close()
        db.close()

    return render_template("request_create.html",form=createRequest,guest=guest)


@app.route('/edit-request/<int:id>',methods=["GET","POST"])
def edit_request(id):
    createRequest = RequestForm(request.form)
    if request.method== "POST" and createRequest.validate():
        requestDict={}
        print("1st choice of editing request")
        try:
            requestdb=shelve.open("requests.db")
            requestDict = requestdb["Requests"]
        except:
            print("Error opening request database.")
        quest=requestDict.get(id)
        quest.set_request_type(createRequest.type.data)
        quest.set_request_topic(createRequest.topic.data)
        quest.set_request_details(createRequest.details.data)
        requestdb["Requests"]= requestDict
        requestdb.close()
        return redirect(url_for('request_list'))
    else:
        requestDict = {}
        try:
            requestdb = shelve.open("requests.db")
            requestDict = requestdb["Requests"]
        except:
            print("Error opening requests database.")

        guest=requestDict.get(id)
        print(guest)
        createRequest.type.data=guest.get_request_type()
        createRequest.topic.data=guest.get_request_topic()
        createRequest.details.data = guest.get_request_details()
        requestdb.close()



        return render_template('request_edit.html',guest=guest,form=createRequest)


@app.route('/delete-request/<int:id>', methods=['POST'])
def delete_request(id):
    request_dict = {}
    requestdb = shelve.open("requests.db")
    request_dict = requestdb["Requests"]

    request_dict.pop(id)

    requestdb["Requests"] = request_dict
    request.close()

    return redirect(url_for('request_list'))




























#ziyuan's part

@app.route('/createProduct', methods=['GET', 'POST'])
def createProduct():
    createProductForm = CreateProductForm(request.form)
    if request.method == "POST" and createProductForm.validate():
        productname_dict = {}
        db = shelve.open('productname.db', 'c')
        try:
            productname_dict = db['Product Name']
        except:
            print("Error in retrieving Product Category from productname.db.")
        product = ProductCat(createProductForm.product_name.data)

        print(createProductForm.product_name.data)
        productname_dict[product.get_product_name()] = product
        db['Product Name'] = productname_dict
        db.close()
        return redirect(url_for('retrieve_productcat'))
    return render_template("createProduct.html", form=createProductForm)


@app.route('/retrieveProduct')
def retrieve_productcat():
    productname_dict = {}
    db = shelve.open('productname.db')
    try:
        productname_dict = db['Product Name']
    except:
        print('Error in retrieving Product Category from productname.db.')
        productname_dict = {}

    productname_list = []
    db.close()
    for key in productname_dict:
        product = productname_dict.get(key)
        productname_list.append(product)

    return render_template("ProductCat.html", productcat_list=productname_list)


@app.route('/deleteProductCat/<product>', methods=['POST'])
def delete_productcat(product):
    productname_dict = {}
    db = shelve.open('productname.db', 'w')
    productname_dict = db['Product Name']
    productname_dict.pop(product)
    db['Product Name'] = productname_dict
    db.close()
    return redirect(url_for('retrieve_productcat'))

@app.route('/createSupplier', methods=['GET', 'POST'])
def createSupplier():
    createSupplierForm = CreateSupplierForm(request.form)
    productname_dict = {}
    try:
        db = shelve.open("productname.db")
        productname_dict = db["Product Name"]
        db.close()
    except:
        print("Error in retrieving Product Category from productname.db.")

    productname_list = []
    for key in productname_dict:
        productname_list.append((key, key))
    createSupplierForm.product_name.choices = productname_list

    if request.method == 'POST' and createSupplierForm.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'c')
        try:
            suppliers_dict = db['Suppliers']
            supplier_company_name = db['supplier_company_name']
        except:

            print("Error in retrieving Supplier from supplier.db.")
        supplier = Supplier(createSupplierForm.company_name.data, createSupplierForm.uen_number.data,
                            createSupplierForm.email.data, createSupplierForm.product_name.data)

        print(createSupplierForm.product_name.data)
        suppliers_dict[supplier.get_company_name()] = supplier
        db['Suppliers'] = suppliers_dict
        db.close()
        return redirect(url_for('retrieve_suppliers'))
    return render_template('createSupplier.html', form=createSupplierForm)


@app.route('/retrieveSuppliers')
def retrieve_suppliers():
    suppliers_dict = {}
    db = shelve.open('supplier.db')
    try:
        suppliers_dict = db['Suppliers']
    except:
        print('Error in retrieving Supplier from supplier.db.')
        suppliers_dict = {}

    suppliers_list = []
    db.close()
    for key in suppliers_dict:
        supplier = suppliers_dict.get(key)
        suppliers_list.append(supplier)

    return render_template('retrieveSuppliers.html', count=len(suppliers_list), suppliers_list=suppliers_list)


@app.route('/updateSupplier/<company_name>', methods=['GET', 'POST'])
def update_supplier(company_name):
    createSupplierForm = CreateSupplierForm(request.form)
    productname_dict = {}
    try:
        db = shelve.open("productname.db")
        productname_dict = db["Product Name"]
        db.close()
    except:
        print("Error in retrieving Product Category from productname.db.")

    productname_list = []
    for key in productname_dict:
        productname_list.append((key, key))
    createSupplierForm.product_name.choices = productname_list

    if request.method == 'POST' and createSupplierForm.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'w')
        suppliers_dict = db['Suppliers']

        supplier = suppliers_dict.get(company_name)
        supplier.set_company_name(createSupplierForm.company_name.data)
        supplier.set_uen_number(createSupplierForm.uen_number.data)
        supplier.set_email(createSupplierForm.email.data)
        supplier.set_product_name(createSupplierForm.product_name.data)

        db['Suppliers'] = suppliers_dict
        db.close()

        return redirect(url_for('retrieve_suppliers'))
    else:
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()

        supplier = suppliers_dict.get(company_name)
        createSupplierForm.company_name.data = supplier.get_company_name()
        createSupplierForm.uen_number.data = supplier.get_uen_number()
        createSupplierForm.email.data = supplier.get_email()
        createSupplierForm.product_name.data = supplier.get_product_name()

        return render_template('updateSupplier.html', form=createSupplierForm)


@app.route('/deleteSupplier/<string:company_name>', methods=['POST'])
def delete_supplier(company_name):
    suppliers_dict = {}
    db = shelve.open('supplier.db', 'w')
    suppliers_dict = db['Suppliers']
    suppliers_dict.pop(company_name)
    db['Suppliers'] = suppliers_dict
    db.close()
    return redirect(url_for('retrieve_suppliers'))


@app.route('/createInventory', methods=['GET', 'POST'])
def createInventory():
    suppliers_dict = {}
    try:
        db = shelve.open('supplier.db')
        suppliers_dict = db['Suppliers']
        db.close()
    except:
        print('Error in retrieving Supplier from supplier.db.')

    suppliers_list = [('', 'Select')]
    for key in suppliers_dict:
        # supplier = suppliers_dict.get(key)
        # suppliers_list.append((supplier.get_company_name(), supplier.get_company_name()))
        suppliers_list.append((key, key))
    createInventoryForm = CreateInventoryForm(request.form)
    createInventoryForm.supplier.choices = suppliers_list

    productname_dict = {}
    try:
        db = shelve.open("productname.db")
        productname_dict = db["Product Name"]
        db.close()
    except:
        print("Error in retrieving Product Category from productname.db.")

    productname_list = [('', 'Select')]
    for key in productname_dict:
        productname_list.append((key,key))
    createInventoryForm.product_name.choices = productname_list

    if request.method == 'POST' and createInventoryForm.validate():
        inventories_dict = {}
        db = shelve.open('inventory.db', 'c')
        try:
            inventories_dict = db['Inventories']
        except:
            print("Error in retrieving Item List from inventory.db.")
        inventory = Inventory(createInventoryForm.item_name.data, createInventoryForm.supplier.data,
                              createInventoryForm.product_name.data, createInventoryForm.quantity.data)

        inventories_dict[inventory.get_item_name()] = inventory
        db['Inventories'] = inventories_dict
        db.close()
        return redirect(url_for('retrieve_inventories'))
    return render_template('createInventory.html', form=createInventoryForm)


@app.route('/retrieveInventories')
def retrieve_inventories():
    inventories_dict = {}
    try:
        db = shelve.open('inventory.db', 'r')
        inventories_dict = db['Inventories']
        db.close()
    except:
        print('Error in retrieving Item List from inventory.db.')

    inventories_list = []
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)

    return render_template('retrieveInventories.html', count=len(inventories_list), inventories_list=inventories_list)


@app.route('/updateInventory/<string:item_name>/', methods=['GET', 'POST'])
def update_inventory(item_name):
    suppliers_dict = {}
    try:
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()
    except:
        print('Error in retrieving Supplier from supplier.db.')

    suppliers_list = [('', 'Select')]
    for key in suppliers_dict:
        # supplier = suppliers_dict.get(key)
        # suppliers_list.append((supplier.get_company_name(), supplier.get_company_name()))
        suppliers_list.append((key, key))
    update_inventory_form = CreateInventoryForm(request.form)
    update_inventory_form.supplier.choices = suppliers_list

    productname_dict = {}
    try:
        db = shelve.open("productname.db")
        productname_dict = db["Product Name"]
        db.close()
    except:
        print("Error in retrieving Product Category from productname.db.")

    productname_list = [('', 'Select')]
    for key in productname_dict:
        productname_list.append((key, key))
    update_inventory_form.product_name.choices = productname_list

    if request.method == 'POST' and update_inventory_form.validate():
        inventories_dict = {}
        db = shelve.open('inventory.db', 'w')
        inventories_dict = db['Inventories']

        inventory = inventories_dict.get(item_name)
        inventory.set_item_name(update_inventory_form.item_name.data)
        inventory.set_supplier(update_inventory_form.supplier.data)
        inventory.set_product_name(update_inventory_form.product_name.data)
        quantity = int(inventory.get_quantity() + update_inventory_form.quantity.data)
        inventory.set_quantity(quantity)

        db['Inventories'] = inventories_dict
        db.close()

        return redirect(url_for('retrieve_inventories'))
    else:
        inventories_dict = {}
        db = shelve.open('inventory.db', 'r')
        inventories_dict = db['Inventories']
        db.close()

        inventory = inventories_dict.get(item_name)
        update_inventory_form.item_name.data = inventory.get_item_name()
        update_inventory_form.supplier.data = inventory.get_supplier()
        update_inventory_form.product_name.data = inventory.get_product_name()
        update_inventory_form.quantity.data = inventory.get_quantity()

        return render_template('updateInventory.html', form=update_inventory_form)


@app.route('/deleteInventory/<string:item_name>', methods=['POST'])
def delete_inventory(item_name):
    inventories_dict = {}
    db = shelve.open('inventory.db', 'w')
    inventories_dict = db['Inventories']
    inventories_dict.pop(item_name)
    db['Inventories'] = inventories_dict
    db.close()

    return redirect(url_for('retrieve_inventories'))


@app.route('/createOrder', methods=['GET', 'POST'])
def createOrder():
    createOrderForm = CreateOrderForm(request.form)
    inventory_dict = {}
    try:
        db = shelve.open('inventory.db', 'r')
        inventory_dict = db['Inventories']
        db.close()
    except:
        print('Error in retrieving Inventory from inventory.db.')

    inventory_list = [('', 'Select')]
    for key in inventory_dict:
        inventory_list.append((key, key))
    createOrderForm.item_name.choices = inventory_list

    suppliers_dict = {}
    try:
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()
    except:
        print('Error in retrieving Supplier from supplier.db.')

    suppliers_list = [('', 'Select')]
    suppliers_email = []
    supplierorder = {}
    for key in suppliers_dict:
        # supplier = suppliers_dict.get(key)
        # suppliers_list.append((supplier.get_company_name(), supplier.get_company_name()))
        supplier = suppliers_dict.get(key)
        suppliers_list.append((supplier.get_company_name(), supplier.get_company_name()))
        # suppliers_list.append((key, key))
        suppliers_email.append(supplier.get_email())
    createOrderForm.supplier.choices = suppliers_list

    productname_dict = {}
    try:
        db = shelve.open("productname.db")
        productname_dict = db["Product Name"]
        db.close()
    except:
        print("Error in retrieving Product Category from productname.db.")

    productname_list = [('', "Select")]
    for key in productname_dict:
        productname_list.append((key, key))
    createOrderForm.product_name.choices = productname_list

    if request.method == 'POST' and createOrderForm.validate():
        order_dict = {}
        order_count_id = 0
        db = shelve.open('order.db', 'c')
        try:
            order_dict = db['Order']
            order_count_id = int(db['order_count_id'])
        except:
            print("Error in retrieving Order List from order.db.")
        order = Order(createOrderForm.item_name.data, createOrderForm.product_name.data,
                      createOrderForm.supplier.data, createOrderForm.quantity.data, createOrderForm.remarks.data)
        # auto increment order_id from shelve
        order_count_id = order_count_id + 1
        order.set_order_id(order_count_id)
        db['order_count_id'] = order_count_id
        order_dict[order.get_order_id()] = order
        db['Order'] = order_dict
        db.close()

        count = 0
        for key in suppliers_dict:
            supplierorder[key] = suppliers_email[count]
            if createOrderForm.supplier.data == key:
                email = suppliers_email[count]
            count += 1
        print(email)

        port = 587  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "hotel.la.bodo@gmail.com"
        password = "Admin-123"
        subject = "Order From Hotel La Bodo"
        text = "Dear " + createOrderForm.supplier.data + ",\n" + "\nWe would like to order another " + str(
            createOrderForm.quantity.data) \
               + " " + createOrderForm.item_name.data + ".\n\nAdditional Remarks:" + "\n" + createOrderForm.remarks.data + "\n\nWe hope to hear from you soon!\n" + "Sincerely,\nHotel La Bodo"
        message = "Subject: {}\n\n{}".format(subject, text)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, email, message)
        except:
            print("fail")
        print(message)

        return redirect(url_for('retrieve_order'))
    return render_template('createOrder.html', form=createOrderForm)


@app.route('/retrieveOrder')
def retrieve_order():
    order_dict = {}
    try:
        db = shelve.open('order.db', 'r')
        order_dict = db['Order']
        db.close()
    except:
        print('Error in retrieving Order List from order.db.')

    order_list = []
    for key in order_dict:
        order = order_dict.get(key)
        order_list.append(order)

    return render_template('retrieveOrder.html', count=len(order_list), order_list=order_list)




































#Gabriel's part

@app.route('/createPartnerships', methods=['GET', 'POST'])
def createPartnerships():
    createPartnershipsForm = CreatePartnershipsForm(request.form)
    if request.method == 'POST' and createPartnershipsForm.validate():

        company_dict = {}
        db = shelve.open('company.db', 'c')
        try:
            company_dict = db['company']

        except:
            print('Error in retrieving Company Name from ')

        partnerships = Partnerships(createPartnershipsForm.company.data,
                                    createPartnershipsForm.resources.data,
                                    createPartnershipsForm.industry.data)

        company_dict[partnerships.get_company()] = partnerships
        db['company'] = company_dict

        db.close()
        print("hello")
        return redirect(url_for('retrievePartnerships'))
    return render_template('createPartnerships.html', form=createPartnershipsForm)


@app.route('/retrievePartnerships')
def retrievePartnerships():
    partnerships_dict = {}
    db = shelve.open('company.db')
    try:
        partnerships_dict = db['company']

    except:
        print('Error in retrieving Partnerships from partnerships.db.')
        partnerships_dict = {}

    partnerships_list = []
    db.close()
    for key in partnerships_dict:
        partnerships = partnerships_dict.get(key)
        partnerships_list.append(partnerships)
    print("bye")

    return render_template('retrievePartnerships.html', count=len(partnerships_list),
                           partnerships_list=partnerships_list)


@app.route('/updatePartnerships/<company>', methods=['GET', 'POST'])
def updatePartnerships(company):
    update_partnerships_form = CreatePartnershipsForm(request.form)
    if request.method == 'POST' and update_partnerships_form.validate():
        partnerships_dict = {}
        db = shelve.open('company.db', 'w')
        partnerships_dict = db['company']

        partnerships = partnerships_dict.get(company)
        partnerships.set_company(update_partnerships_form.company.data)
        partnerships.set_resources(update_partnerships_form.resources.data)
        partnerships.set_industry(update_partnerships_form.industry.data)

        db['company'] = partnerships_dict
        db.close()

        return redirect(url_for('retrievePartnerships'))
    else:
        partnerships_dict = {}
        db = shelve.open('company.db')
        partnerships_dict = db['company']

        partnerships = partnerships_dict.get(company)

        update_partnerships_form.company.data = partnerships.get_company()
        update_partnerships_form.resources.data = partnerships.get_resources()
        update_partnerships_form.industry.data = partnerships.get_industry()

        db.close()

        return render_template('updatePartnerships.html', form=update_partnerships_form, partnerships=partnerships)


@app.route('/deletePartnerships/<company>', methods=['POST'])
def deletePartnerships(company):
    partnerships_dict = {}
    db = shelve.open('company.db', 'w')
    partnerships_dict = db['company']
    partnerships_dict.pop(company)
    db['company'] = partnerships_dict
    db.close()

    return redirect(url_for('retrievePartnerships'))


@app.route('/createPackageDeal', methods=['GET', 'POST'])
def createPackageDeal():
    print("hi")
    createPackageDealForm = CreatePackageDeal(request.form)
    print("hi")
    if request.method == 'POST' and createPackageDealForm.validate():
        print("chicken")
        attractions_dict = {}
        db = shelve.open('attractions.db', 'c')
        try:
            attractions_dict = db['attraction']

        except:
            print('Error in retrieving Package Deal from ')
        pd = PackageDeal(createPackageDealForm.attractions.data,
                         createPackageDealForm.transport.data,
                         createPackageDealForm.price.data,
                         createPackageDealForm.code.data)

        attractions_dict[pd.get_attractions()] = pd
        db['attraction'] = attractions_dict

        db.close()
        print("hello")
        return redirect(url_for('retrievePackageDeal'))
    return render_template('createPackageDeal.html', form=createPackageDealForm)


@app.route('/retrievePackageDeal')
def retrievePackageDeal():
    attractions_dict = {}
    print("hello")
    db = shelve.open('attractions.db')
    try:
        attractions_dict = db['attraction']

    except:
        print('Error in retrieving Package Deal from attractions.db.')
        attractions_dict = {}

    attractions_list = []
    db.close()
    for key in attractions_dict:
        attractions = attractions_dict.get(key)
        attractions_list.append(attractions)
    print("bye")

    return render_template('retrievePackageDeal.html', count=len(attractions_list), attractions_list=attractions_list)


@app.route('/updatePackageDeal/<packagedeal>', methods=['GET', 'POST'])
def updatePackageDeal(packagedeal):
    update_packagedeal_form = CreatePackageDeal(request.form)
    if request.method == 'POST' and update_packagedeal_form.validate():
        packagedeal_dict = {}
        db = shelve.open('attractions.db', 'w')
        packagedeal_dict = db['attraction']

        packagedeal = packagedeal_dict.get(packagedeal)
        packagedeal.set_attractions(update_packagedeal_form.attractions.data)
        packagedeal.set_transport(update_packagedeal_form.transport.data)
        packagedeal.set_price(update_packagedeal_form.price.data)
        packagedeal.set_code(update_packagedeal_form.code.data)

        db['attraction'] = packagedeal_dict
        db.close()

        return redirect(url_for('retrievePackageDeal'))
    else:
        packagedeal_dict = {}
        db = shelve.open('attractions.db')
        packagedeal_dict = db['attraction']

        packagedeal = packagedeal_dict.get(packagedeal)

        update_packagedeal_form.attractions.data = packagedeal.get_attractions()
        update_packagedeal_form.transport.data = packagedeal.get_transport()
        update_packagedeal_form.price.data = packagedeal.get_price()
        update_packagedeal_form.code.data = packagedeal.get_code()

        db.close()

        return render_template('updatePackageDeal.html', form=update_packagedeal_form, packagedeal=packagedeal)


@app.route('/deletePackageDeal/<attractions>', methods=['POST'])
def deletePackageDeal(attractions):
    attractions_dict = {}
    db = shelve.open('attractions.db', 'w')
    attractions_dict = db['attraction']
    attractions_dict.pop(attractions)
    db['attraction'] = attractions_dict
    db.close()

    return redirect(url_for('retrievePackageDeal'))

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    sign_up_form = Signup(request.form)
    print("yeeyee")
    if request.method == 'POST' and sign_up_form.validate():
        print("mmm")
        users_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            users_dict = db['Users']
            print("haircut")
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(sign_up_form.name.data,
                         sign_up_form.username.data,
                         sign_up_form.email.data,
                         sign_up_form.gender.data,
                         sign_up_form.phone_num.data,
                         sign_up_form.password.data,
                         sign_up_form.deals.data
                         )

        users_dict[user.get_username()] = user
        session['CurrentUsername'] = user.get_username()
        session["Name"]= user.get_name()
        session["Email"] = user.get_email()
        session["Deals"] = user.get_deals()
        db['Users'] = users_dict
        db.close()
        print('working')
        return redirect(url_for('profile'))
    return render_template('createUser.html', form=sign_up_form)

@app.route('/GuestL', methods = ['GET', 'POST'])
def login_user():
    log_in_user_form = Login(request.form)
    if request.method == 'POST' and log_in_user_form.validate():
        customer_dict = {}
        db = shelve.open('storage.db', 'r')
        try:
            customer_dict = db['Users']
        except:
            print('Error in retrieving information')

        username = log_in_user_form.username.data
        password = log_in_user_form.password.data
        print('1')
        if username in customer_dict:
            real_password = customer_dict[username].get_password()
            print('2')
            if password == real_password:
              session['CurrentUsername'] = username
              print('3')
              return redirect(url_for('home_page'))
    return render_template('GuestL.html', form = log_in_user_form)

@app.route('/GuestL')
def logout():
    session.pop('CurrentUsername', None)
    return redirect(url_for('GuestL'))

@app.route('/createStaff', methods=['GET', 'POST'])
def create_staff():
    staff_sign_up_form = Staff_Signup(request.form)
    print("yeeyee")
    if request.method == 'POST' and staff_sign_up_form.validate():
        print("ok")
        staff_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            staff_dict = db['Staff']
            print("haircut")
        except:
            print("Error in retrieving Users from storage.db.")

        staff = Staff.Staff(staff_sign_up_form.id.data,
                            staff_sign_up_form.email.data,
                            staff_sign_up_form.password.data,
                            )

        staff_dict[staff.get_id()] = staff
        session['CurrentID'] = staff.get_id()
        db['Staff'] = staff_dict
        db.close()
        print('working')
        return redirect(url_for('login_staff'))
    return render_template('createStaff.html', form=staff_sign_up_form)

@app.route('/StaffL', methods = ['GET', 'POST'])
def login_staff():
    log_in_staff_form = Staff_Login(request.form)
    if request.method == 'POST' and log_in_staff_form.validate():
        staff_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            staff_dict = db['Staff']
        except:
            print('Error in retrieving information')

        id = log_in_staff_form.id.data
        password = log_in_staff_form.password.data
        print('1')
        if id in staff_dict:
            real_password = staff_dict[id].get_password()
            print('2')
            if password == real_password:
              session['CurrentID'] = id
              print('3')
              return redirect(url_for('home'))
    return render_template('StaffL.html', form = log_in_staff_form)


@app.route('/StaffL')
def staff_logout():
    session.pop('CurrentID', None)
    return redirect(url_for('StaffL'))


@app.route('/profile')
def profile():
    customer_dict = {}
    db = shelve.open('storage.db', 'r')
    try:
        customer_dict = db['Users']
    except:
        print('error')
    id = session['CurrentUsername']
    user = customer_dict[id]
    return render_template('profile.html', user = user)

@app.route('/updateProfile/<id>/', methods=['GET','POST'])
def updateProfile(id):
    update_profile = Signup(request.form)
    if request.method == 'POST' and update_profile.validate():
        users_dict = {}
        db = shelve.open('storage.db')
        users_dict = db['Users']

        profile = users_dict.get(User)
        profile.set_name(update_profile.name.data)
        profile.set_username(update_profile.username.data)
        profile.set_email(update_profile.email.data)
        profile.set_phone_num(update_profile.phone_num.data)
        profile.set_gender(update_profile.gender.data)
        profile.set_password(update_profile.password.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('updateProfile'))
    else:
        users_dict = {}
        db = shelve.open('storage.db')
        users_dict = db['Users']
        id = session['CurrentUsername']
        profile = users_dict[id]

        update_profile.name.data = profile.get_name()
        update_profile.username.data = profile.get_username()
        update_profile.email.data = profile.get_email()
        update_profile.phone_num.data = profile.get_phone_num()
        update_profile.gender.data = profile.get_gender()
        update_profile.password.data = profile.get_password()

        db.close()

        return render_template('updateProfile.html', form=update_profile,user=profile)


@app.route('/price_deal')
def price_deal():
    return render_template("price_deal.html")

if __name__ == '__main__':
    app.run(debug=True)
