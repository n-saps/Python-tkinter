from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800")

    def menu(self):
        self.label=Label(self, text="GEOGRAPHICAL AGRO SURVEY ANALYSIS",
                         relief=SUNKEN, font="Cambria 31 bold", fg="green", bg="pink")
        self.label.pack(fill="x" , padx=50, pady=50)
        self.l2=Label(self, text="PLEASE SELECT THE STATE-",
                      font="Cambria 16 bold").pack(pady=10)
        options=["Rajasthan", "Gujarat", "Haryana", "Arunachal Pradesh",
                 "Assam", "Bihar", "Delhi", "Himachal Pradesh", "Jammu",
                 "Jharkhand", "Madhya Pradesh", "Manipur", "Punjab",
                 "Uttar Pradesh"]


        global clicked
        clicked=StringVar()
        clicked.set(options[0])

        self.drop=OptionMenu(self, clicked, *options).pack()

        self.button=Button(self, text="Show Results")
        self.button["command"]=self.show
        self.button.pack(pady=10)

        self.listbox=Listbox(height=0)

        self.listbox.pack(anchor="w", fill="x", padx=10, pady=10)



    def show(self):
        self.listbox.delete(0,END)
        l1=['Rajasthan']
        l1f=['* Barley ', '* Wheat','* Gram' ,'* Pulse','* Mustard']
        l1c=['* Bajra','* Jowar','* Maize','* Groundnut']
        l1w=["* 32-45 'C during summer ","* 10-27 'C during winter","* Recives 90% of the rainfall during the time of jult to september upto 32.7 cm-64.9cm"]
        l1s=['* Sandy soil','* Red loamy soil','* Mixed red black soil','* Alluvial soil']
        l1l=['1. Ajmer','2. Hanumangarh','3. Dhoplur','4. Rajasmand','5. Alwar','6. Jaisalmer']
        l1gp=['1. For spices 1500000/annum for 3 years ','2. For fruits and vegetable within country 1500000/annum','3. Incentives for quality certificates 200000/annum or 40% upto 50000','4. For research and developement 2000000/annum or 50% of cost for 5 years']
        l1.append(l1f)
        l1.append(l1c)
        l1.append(l1w)
        l1.append(l1s)
        l1.append(l1l)
        l1.append(l1gp)
        l2=['Gujarat']
        l2s=['* Hilly soil','* Loamy soil','* Alluvial soil','* Saline soil',]
        l2l=['1. Surat','2. Bhawnagar','3. Gandhinagar','4. Kheda','5. Anand']
        l2w=['* 25-45 C during summer','* 15-35 during winter','* Recives 95% of rainfall during june to september which is 30 cms to 210 cms']
        l2c=['* Wheat','* Sugarcane','* Cotton','* Rice which holds 28% profits in state']
        l2f=['* Wheat','* Mango','* Banana','* Groundnut']
        l2gp=['1. Pradhan mantri fhasal beema yojna','2. Sardar patel agriculture and rural development foundation','3. and have the largest sea port in india for trading ']
        l2.append(l2l)
        l2.append(l2s)
        l2.append(l2w)
        l2.append(l2c)
        l2.append(l2f)
        l2.append(l2gp)
        l3=['Haryana']
        l3l=['1. Rawari','2. Gurugram','3. Bhiwani','4. Jind','5. Ambala','6. Sonipat']
        l3s=['* Kankar soil','* Clay','* Sandy','* Old alluvial soil']
        l3w=['* 40-46 C during summer','* 5-4 C during winter','recives rainfall during july to spetember 16cms to 75cms']
        l3c=['* Rabi','* Wheat','* Rice','* Mustard','* Tobacco','* Sugarcane']
        l3f=['* Groundnut','* Mango','* Potato','* Maize','* Cauliflower']
        l3gp=['1. 250 heactacer land is reserved for organic farming','2. Rastra krishi vikash yojna with annual growth of 4%','3. 10% subsidy is provided with 50:50 of state and central','4. National agriculture inssurance scheme']
        l3.append(l3l)
        l3.append(l3s)
        l3.append(l3w)
        l3.append(l3c)
        l3.append(l3f)
        l3.append(l3gp)
        l4=["Arunachal Pradesh"]
        l4l=['1. Trupathi','2. Hindupur','3. Kovvur','4. Gooty','5. Rajanagaram','6. Kadari','7. Bapatla']
        l4s=['* Red soil','* Black soil','* Alluvial soil','* Laterite soil','* Marshy soil','* Saline soil']
        l4w=['* Temperature of the state varies from 20 degree C to 40 degree C ','* Recives  31-78 cm of rainfall','* During snowfall the temp. can drop till negative 20 degree celcious']
        l4c=['* Chilli','* Pepper','* Tabacco','* Sunflower oilseeds','* Cotton']
        l4f=['* Wheat','* Rice','* Jowar','* Mango','* Banana','* Brinjal']
        l4gp=['1. Chief Minister Sashakt Kisan Yojana','2. Arunachal Pradesh Agriculture Marketing Board','3. Arunachal Pradesh Crop Insurance Scheme','4. Integrated Horticulture Development Scheme','5. National Mission for Sustainable Agriculture','6.Agriculture Mechanization Programme']
        l4.append(l4l)
        l4.append(l4s)
        l4.append(l4w)
        l4.append(l4c)
        l4.append(l4f)
        l4.append(l4gp)
        l5=['Assam']
        l5l=['1. Darjeeling','2. Dhing','3. Kampan','4. Lanka','5. Raha','6. Rupahi','7. Hojai','8. Dobaka']
        l5s=['* Hill soil','* Lateritic soil','* Alluvial soil','* Piedmont soil']
        l5w=['* Maximum temperature is 32 C','* Gets 260-320cms of rainfall','* Gets a short winter stays humid overall the year']
        l5c=['* Tea','* Jute','* Sugarcane','* Cotton','* Ornamental plants','* Oilseeds']
        l5f=['* Rice','* Wheat','* Mushroom','* Patato','* Maize','* Oats']
        l5gp=['1. MISSION ORGANIC VALUE CHAIN DEVELOPMENT IN ASSAM (MOVCD)','2. RASHTRIYA KRISHI VIKAS YOJANA(RKVY)','3. PARAMPARAGAT KRISHI VIKAS YOJANA(PKVY)','4. NATIONAL MISSION FOR SUISTAINABLE AGRICULTURE(NMSA)']
        l5.append(l5l)
        l5.append(l5s)
        l5.append(l5w)
        l5.append(l5c)
        l5.append(l5f)
        l5.append(l5gp)
        l6=['Bihar']
        l6l=['1. Champaran','2. Siwan','3. Saran','4. Vaishali','5. Muzaffarnagar','6. Gopalgang','7. Samastipur','8. Darbanga','9. Begusarai']
        l6s=['* Terai soil','* Clay soil','* Sandy soil','* Loamy soil','* Marshy swamp','* Gangetic Alluvial','* Montane']
        l6w=['* In summer temperature ranges 34-40 C','* Recives 86-221 cms of rainfall ','* In winters is around december to febuary with7-11 C']
        l6c=['* Linseed','* Jute','* Rai','* Cole crop','* Okra','* Turmeric']
        l6f=['* Wheat','* Rice','* Gram','* Beans','* Methi','* Banana','* Lichi','* makhana','* Garlic']
        l6gp=['1. Kisan Credit Card Scheme','2.Integrated Agriculture Development Scheme','3.Bihar State Seed and Organic Certification Agency','4.Krishi Input Subsidy Scheme','5. Krishi Anudan Yojana','6. Mukhyamantri Fasal Sahayata Yojana']
        l6.append(l6l)
        l6.append(l6s)
        l6.append(l6w)
        l6.append(l6c)
        l6.append(l6f)
        l6.append(l6gp)
        l7=['Delhi']
        l7l=['1. Razapur','2. Kakra','3. Daryapur','4. Palam','5. Najafgarh','6. Alipur','7. Wazirabad','8. Palla']
        l7s=['* Sandy loam soil','* Rocky aravalli rddges','* Loam silt loams ','* Silty clay loam','*Loamy sands']
        l7w=['* High variation between summer and winter temperatures and precipitation.','* The monsoons recede in late September, and the post-monsoon season continues till late October, with average temperatures sliding from 29 to 21 °C (84 to 70 °F).','* New Delhi earns an average of 790 mm (31.1 in) of rainfall per yearor 65.8 mm (2.6 in) per mon']
        l7c=['* Oilseed','* Sugarcane','* Tobacco','* Fodder']
        l7f=['* Wheat','* Rice','* Jowar','* Arhar','* Green gram']
        l7gp=['1. Agricultural Land Use Policy','2. Farm to Fork','Kisan Call Centres','3. Subsidies for Farmers','4. Krishi Vigyan Kendras','5. Delhi State Agricultural Marketing Board']
        l7.append(l7l)
        l7.append(l7s)
        l7.append(l7w)
        l7.append(l7c)
        l7.append(l7f)
        l7.append(l7gp)
        l8=['Himachal Pradesh']
        l8l=['1. Chamba','2. Palampur','3. Kangra','4. Mandi','5. Una','6. Kullu']
        l8s=['* Planosolic soil','* Alpine humus','* Podozolic soil','* Brown earth','* Brown forest soil','* Brown hill soil','* Alluvial soil']
        l8w=["* Weather stays dry and cold throughout the year except when it's raining",'* May expreince snowfall with increase in height','* The average annual rainfall is 1,251(mm). ']
        l8c=['* Oil seed','* Chicory seeds','* Pulse','* Hops']
        l8f=['* Olives','* Wheat','* Rice','* Pulses','* Soybean']
        l8gp=['1. HIMCAD','2. PM Kisan Nidhi Yojana','3. Himachal Pushp Kranti','4.SOLAR IRRIGATION SCHEME','5. State agricultural mechanization program','6. Quality feed production scheme','7. CM Farmer and Agricultural Laborers Life Protection Scheme']
        l8.append(l8l)
        l8.append(l8s)
        l8.append(l8w)
        l8.append(l8c)
        l8.append(l8f)
        l8.append(l8gp)
        l9=['Jammu']
        l9l=['1. Kupwara','2. Anantnag','3. Baramulla','4. Pulwama','5. Kargi','6. Leh','7. Doda']
        l9s=['* Lithosols soil','* Saline Alkali soil','* Mountain meadow soil','* Hill and Mountain forest soil','* Brown earth/forest soil','* Podzolic soil']
        l9w=['* Snowfall increases with the altitude','* Average rainfall is 65 cms','temperature stays moderate']
        l9c=['* Walnut','* Almonds','* Oilseeds','* Fodder','* Cotton','* Sugarcane','* Tabacco','* Saffron']
        l9f=['* Peas','* Beans','* Pulse','* Corn','* Peach','* Cherrry','* Apple','* Rice','* Wheat']
        l9gp=['1. Rashtriya Krishi Vikas Yojana (RKVY)','2. National Food Security Mission (NFSM)','3. Pradhan Mantri Fasal Bima Yojana (PMFBY)','4. Soil Health Card Scheme','5. Horticulture Mission for North East and Himalayan States (HMNEH)','6. Pradhan Mantri Krishi Sinchai Yojana (PMKSY)']
        l9.append(l9l)
        l9.append(l9s)
        l9.append(l9w)
        l9.append(l9c)
        l9.append(l9f)
        l9.append(l9gp)
        l10=["Jharkhand"]
        l10l=['1. Rajmahal','2. Dhanbad','3. Koderma','4. Damodar valley','5. Ranchi']
        l10s=['* Red soil','* Sandy soil','* Black soil','* Laterite soil','* Micacious soil','* Red micacious soil']
        l10w=['* Temperature goes to 20-37 degree C','* Recives 40-60 cms of rainfall during july-september','* In winter temperature may goes till -5 degree C']
        l10c=['* Ground nut','* Mustard','* Jowar','* Sunflower','* Paddy','* Sesamum']
        l10f=['* Mango','* Potato','* Banana','* Jack fruit','* Litchi']
        l10gp=["1. Jharkhand State Agricultural Policy","2. Pradhan Mantri Fasal Bima Yojana (PMFBY)","3. Mukhyamantri Krishi Ashirwad Yojana","4. Agriculture Infrastructure Development Fund (AIDF)"]
        l10.append(l10l)
        l10.append(l10s)
        l10.append(l10w)
        l10.append(l10c)
        l10.append(l10f)
        l10.append(l10gp)
        l11=["Madhya Pradesh"]
        l11l=['1. Satpura hills','2. Narmada valley','3. Nirmar region','4. malwa region','5. Gwalior region']
        l11s=['* Black soil','* Alluvial soil','* Laterite soil','* Mix soil','* Red soil']
        l11w=['* Temperature varies so much in region','* Recives 100-125 cms of rainfall','* December to febuary are the most cold months']
        l11c=['* Sesamum','* Wheat','* Sugarcane','* Pulse','* Paddy']
        l11f=['* Soyabeans','* Peas','* Grams']
        l11gp=["1. Mukhya Mantri Gramodyog Rojgar Yojana","2. Pradhan Mantri Fasal Bima Yojana (PMFBY)","3. Mukhya Mantri Krishi Kalyan Yojana","4. Mukhya Mantri Krishi Sichai Yojana","5. Mukhya Mantri Fasal Rin Mochan Yojana","6. Mukhya Mantri Krishi Samuhik Beema Yojana"]
        l11.append(l11l)
        l11.append(l11s)
        l11.append(l11w)
        l11.append(l11c)
        l11.append(l11f)
        l11.append(l11gp)
        l12=["Manipur"]
        l12l=['1. Bishnupur','2. Senapati','3. Chandel','4. Kangabok','5. Thaubal']
        l12s=['* Loamy soil','* Alluvila soil','* Red soil','* Sandy soil','* Clay soil']
        l12w=['* Average tempertaure is moderate from 39-91 degree F','* Recives upto 151 cms of rainfall','* Rain accurs throughout the year and hottest month is may']
        l12c=['* Cashew nut','* Wallnut','* Sugarcane','* Oil seed','* Cotton']
        l12f=['* Ginger','* Garlic','* Carrot','* Radish','* Turmric','* Oranges']
        l12gp=["1. Mission Organic Value Chain Development for North Eastern Region (MOVCDNER)","2. Pradhan Mantri Fasal Bima Yojana (PMFBY)","3. National Horticulture Mission (NHM)","4. National Agriculture Market (e-NAM):"]
        l12.append(l12l)
        l12.append(l12s)
        l12.append(l12w)
        l12.append(l12c)
        l12.append(l12f)
        l12.append(l12gp)
        l13=["Punjab"]
        l13l=['1. Gurdaspur','2. Pathankot','3. Mansa','4. Zira','5. Patila']
        l13s=['* Forest soil','* Saline soil','* Flood plains','* Sandy soil','* Loamy soil','* Desert soil']
        l13w=['* Temperature varies from 9-25 degree C','* Recives raimnfall upto 19 cms in a day during monsoon','* Winters are cold with average temperature of 7 degree C']
        l13c=['* Mustard','* Sunflower','* Cotton','* Wheat','* Rice','* Pulses']
        l13f=['* Peach','* Mango','* Onion','* Ladyfinger','* Radish','* Carrot']
        l13gp=["1. KISAN DOST LIVE STOCK DEVELOPMENT SCHEME","2. KISSAN DOST COMMERCIAL AGRO SERVICES FINANCE SCHEME","3. KISAN DOST AABRARI SCHEME","4. KISAN DOST AGREE FINANCE SCHEMES","5. Freight Assistance Scheme for Exports from MSMEs"]
        l13.append(l13l)
        l13.append(l13s)
        l13.append(l13w)
        l13.append(l13c)
        l13.append(l13f)
        l13.append(l13gp)
        l14=["Uttar Pradesh"]
        l14l=['1. Baharaich', '2. Gonda','3. Balrampur', '4. Basti', '5. Gorakhpur','6. Sidharth Nagar', '7. Maharajkunj', '8. Kushinagar', '9. Deoria']
        l14s=['* Black soil','* Clay soil','* Red soil','* Clay soil','* Alluvial soil','* Sandy soil','* Parwa soil','* Maaf soil','* Momta soil']
        l14w=['* Average temperature during summer is 25-37 degree C','* Recives upto 100-200 cms of rainfall in different part ','* Temperature goes down to 2-4 degree C during winter']
        l14c=['* Rice','* Wheat','* Grean peas','* Mustard','* Sugarcane','* Pulse']
        l14f=['* Potatos','* Muskmelon','* Amla','* Mango']
        l14gp=["1. Annapurna Scheme","2. Samuhik Kisan Credit Card Scheme","3. Samuhik Paudh Leher Abhiyaan","4. Uttar Pradesh Agriculture and Processed Food Products Export Development Authority (UPAPEDA)"]
        l14.append(l14l)
        l14.append(l14s)
        l14.append(l14w)
        l14.append(l14c)
        l14.append(l14f)
        l14.append(l14gp)

        sn=[]
        sn.append(l1[0])
        sn.append(l2[0])
        sn.append(l3[0])
        sn.append(l4[0])
        sn.append(l5[0])
        sn.append(l6[0])
        sn.append(l7[0])
        sn.append(l8[0])
        sn.append(l9[0])
        sn.append(l10[0])
        sn.append(l11[0])
        sn.append(l12[0])
        sn.append(l13[0])
        sn.append(l14[0])


        if clicked.get()==l1[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Rajasthan is :")
            for i in range(0,len(l1l)):
                self.listbox.insert(END, l1l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l1s)):
                self.listbox.insert(END, l1s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l1w)):
                self.listbox.insert(END, l1w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l1c)):
                self.listbox.insert(END, l1c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l1f)):
                self.listbox.insert(END, l1f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l1gp)):
                self.listbox.insert(END, l1gp[i])

            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))

        if clicked.get()==l2[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Gujarat is :")
            for i in range(0,len(l2l)):
                self.listbox.insert(END, l2l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l2s)):
                self.listbox.insert(END, l2s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l2w)):
                self.listbox.insert(END, l2w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l2c)):
                self.listbox.insert(END, l2c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l2f)):
                self.listbox.insert(END, l2f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l2gp)):
                self.listbox.insert(END, l2gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))

        if clicked.get()==l3[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Haryana is :")
            for i in range(0,len(l3l)):
                self.listbox.insert(END, l3l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l3s)):
                self.listbox.insert(END, l3s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l3w)):
                self.listbox.insert(END, l3w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l3c)):
                self.listbox.insert(END, l3c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l3f)):
                self.listbox.insert(END, l3f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l3gp)):
                self.listbox.insert(END, l3gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l4[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Arunachal Pradesh is :")
            for i in range(0,len(l4l)):
                self.listbox.insert(END, l4l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l4s)):
                self.listbox.insert(END, l4s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l4w)):
                self.listbox.insert(END, l4w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l4c)):
                self.listbox.insert(END, l4c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l4f)):
                self.listbox.insert(END, l4f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l4gp)):
                self.listbox.insert(END, l4gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l5[0]:


            self.listbox.insert(0,"The area which is suitable for vegetation in Assam is :")
            for i in range(0,len(l5l)):
                self.listbox.insert(END, l5l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l5s)):
                self.listbox.insert(END, l5s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l5w)):
                self.listbox.insert(END, l5w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l5c)):
                self.listbox.insert(END, l5c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l5f)):
                self.listbox.insert(END, l5f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l5gp)):
                self.listbox.insert(END, l5gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l6[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Bihar is :")
            for i in range(0,len(l6l)):
                self.listbox.insert(END, l6l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l6s)):
                self.listbox.insert(END, l6s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l6w)):
                self.listbox.insert(END, l6w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l6c)):
                self.listbox.insert(END, l6c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l6f)):
                self.listbox.insert(END, l6f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l6gp)):
                self.listbox.insert(END, l6gp[i])

            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l7[0]:


            self.listbox.insert(0,"The area which is suitable for vegetation in Delhi is :")
            for i in range(0,len(l7l)):
                self.listbox.insert(END, l7l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l7s)):
                self.listbox.insert(END, l7s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l7w)):
                self.listbox.insert(END, l7w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l7c)):
                self.listbox.insert(END, l7c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l7f)):
                self.listbox.insert(END, l7f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l7gp)):
                self.listbox.insert(END, l7gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l8[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Himachal Pradesh is :")
            for i in range(0,len(l8l)):
                self.listbox.insert(END, l8l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l8s)):
                self.listbox.insert(END, l8s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l8w)):
                self.listbox.insert(END, l8w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l8c)):
                self.listbox.insert(END, l8c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l8f)):
                self.listbox.insert(END, l8f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l8gp)):
                self.listbox.insert(END, l8gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l9[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Jammu is :")
            for i in range(0,len(l9l)):
                self.listbox.insert(END, l9l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l9s)):
                self.listbox.insert(END, l9s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l9w)):
                self.listbox.insert(END, l9w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l9c)):
                self.listbox.insert(END, l9c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l9f)):
                self.listbox.insert(END, l9f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l9gp)):
                self.listbox.insert(END, l9gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l10[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Jharkhand is :")
            for i in range(0,len(l5l)):
                self.listbox.insert(END, l5l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l10s)):
                self.listbox.insert(END, l10s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l10w)):
                self.listbox.insert(END, l10w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l10c)):
                self.listbox.insert(END, l10c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l10f)):
                self.listbox.insert(END, l10f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l10gp)):
                self.listbox.insert(END, l10gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l11[0]:


            self.listbox.insert(0,"The area which is suitable for vegetation in Madhya Pradesh is :")
            for i in range(0,len(l11l)):
                self.listbox.insert(END, l11l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l11s)):
                self.listbox.insert(END, l11s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l11w)):
                self.listbox.insert(END, l11w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l11c)):
                self.listbox.insert(END, l11c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l11f)):
                self.listbox.insert(END, l11f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l11gp)):
                self.listbox.insert(END, l11gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))

        if clicked.get()==l12[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Manipur is :")
            for i in range(0,len(l12l)):
                self.listbox.insert(END, l12l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l12s)):
                self.listbox.insert(END, l12s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l12w)):
                self.listbox.insert(END, l12w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l12c)):
                self.listbox.insert(END, l12c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l12f)):
                self.listbox.insert(END, l12f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l12gp)):
                self.listbox.insert(END, l12gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l13[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Punjab is :")
            for i in range(0,len(l13l)):
                self.listbox.insert(END, l13l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l13s)):
                self.listbox.insert(END, l13s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l13w)):
                self.listbox.insert(END, l13w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l13c)):
                self.listbox.insert(END, l13c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l13f)):
                self.listbox.insert(END, l13f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l13gp)):
                self.listbox.insert(END, l13gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


        if clicked.get()==l14[0]:

            self.listbox.insert(0,"The area which is suitable for vegetation in Uttar Pradesh is :")
            for i in range(0,len(l14l)):
                self.listbox.insert(END, l14l[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with the soil texture consist of :" )
            for i in range(0,len(l14s)):
                self.listbox.insert(END, l14s[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"with weather condition :" )
            for i in range(0,len(l14w)):
                self.listbox.insert(END, l14w[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable cash crops are :" )
            for i in range(0,len(l14c)):
                self.listbox.insert(END, l14c[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END,"suitable food crops are :" )
            for i in range(0,len(l14f)):
                self.listbox.insert(END, l14f[i])
            self.listbox.insert(END, "\n")

            self.listbox.insert(END, "Some government policies are:")
            for i in range(0,len(l14gp)):
                self.listbox.insert(END, l14gp[i])
            self.listbox.configure(bg="light grey", fg="darkcyan", font=("Cambria", 14))


if __name__== '__main__':
    window=GUI()
    window.menu()
    window.mainloop()

