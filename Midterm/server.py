import random
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

#Each data item needs to have multiple fields. At the minimum, this must include:
# • An id
# • A short title or name for the item (movie title, restaurant name, etc)
# • A link to media (image, video, or gif).
# o For large media files, you must provide an external link (like a link to a youtube
# video). Do NOT download the file and submit it with the assignment because if
# you did that, it will take your grader forever to download all the assignments.
# • A text paragraph of explanation (At least 4 sentences)
# • Some sort of numerical data (a year, a price, a rating, etc.)
# • A list of some kind of data (such as a list of reviews for the movie, list of popular dishes
# at the restaurant, a list of similar restaurants nearby, etc)


ev_companies = {

    "Rivian" : {
        "id" : "1",
        "ticker" : "RIVN",
        "logo" : "https://imgs.search.brave.com/ki9b6JY5MEH6HFCdh310MUizG5ufETV_CX08lJ90Vkw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/aGF0Y2h3aXNlLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAy/Mi8wOS9yaXZpYW4t/bG9nby1nb2xkLXdo/aXRlLTEzMDB4MTE1/MC0xLTEwMjR4OTA2/LnBuZw",
        "description": 
        "Rivian is an American electric vehicle manufacturer focused on"
        "adventure-oriented EVs and sustainable transportation solutions. "
        "The company offers the R1T electric pickup truck, the R1S electric SUV, "
        "and has announced the upcoming R2 and R3 models aimed at a broader market. "
        "Rivian has received significant investment from major players such as Amazon "
        "and Ford, with Amazon also securing an exclusive contract for Rivian's "
        "electric delivery vans. With a strong emphasis on battery technology, "
        "rugged capability, and software innovation, Rivian is positioning "
        "itself as a competitor to Tesla and legacy automakers in the EV space.",

        "share_price" : "$12.00",
        "models" : ["R1S", "R1T", "R2", "R3"]
    },

    "Tesla" : {
        "id" : "2",
        "ticker" : "TSLA",
        "logo" : "https://imgs.search.brave.com/k_XImqvp9x1KRDgrwcYJZoQScesfRUSk5JlR6OcR2jg/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cHJvZC53ZWJzaXRl/LWZpbGVzLmNvbS82/NWNhZmVhZTBkNjJk/OWU0MTYzZDE1NDUv/NjY5YTVjYmJkYjU5/NzVhNWJjMzE0OTNm/X0FEXzRuWGZGVzE3/VVVVVl96US0weEJF/NWt2RWxxN213MzlE/bmYybkxTazZra0t3/Q0pKRlF0VHNtM1BT/VVY1WC1NLWQ3blFv/dmhpemlSWldWYXRM/Zl9TUmxTdHJuY3lR/ZjZtSTdMcVl3bEly/Qm90eUR0RURPZlc0/UlNSYndEcERaUEJL/XzdNZnZjYi15UTg2/THVPY1p5dEdWTkJ2/TTZFR0EuYXZpZg",

        "description": "Tesla is an American electric vehicle and clean energy "
        "company founded in 2003 by Martin Eberhard and Marc Tarpenning, with "
        "Elon Musk joining shortly after as an early investor and later becoming CEO. "
        "The company revolutionized the EV market with high-performance electric cars "
        "and cutting-edge battery technology. Tesla's lineup includes the Model S, "
        "Model 3, Model X, Model Y, and the recently launched Cybertruck, with future "
        "models like the Roadster and Semi in development. With a strong focus on "
        "autonomous driving, energy storage, and sustainable technology, Tesla "
        "continues to lead the industry in innovation and market dominance.",
        
        "share_price" : "$120.00",
        "models" : ["Model X", "Model Y", "Model S", "Model 3", "Cybertruck"]

    },

    "Lucid Motors": {
        "id": "3",
        "ticker": "LCID",
        "logo": "https://imgs.search.brave.com/oBjAP8K_I7bqYgTcvt7KwM9qvJjlYcRnoMZBUAYk6yw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/d2lrLmNvbS9jb250/ZW50L3VwbG9hZHMv/aW1hZ2VzL2x1Y2lk/LW1vdG9yczMxNjku/anBn",

        "description": "Lucid Motors is an American electric vehicle manufacturer "
        "known for producing luxury EVs with cutting-edge technology and "
        "industry-leading range. Founded in 2007 as Atieva, the company initially "
        "focused on battery technology before shifting to high-performance EV "
        "production under CEO Peter Rawlinson, a former Tesla engineer. Lucid's "
        "flagship model, the Air, boasts one of the longest ranges of any EV, "
        "while the upcoming Gravity SUV aims to expand its presence in the premium "
        "EV market. Backed by significant investment from Saudi Arabia's Public "
        "Investment Fund (PIF), Lucid is positioning itself as a strong competitor "
        "to Tesla and other luxury automakers.",

        "share_price": "$2.30",
        "models": ["Air", "Gravity"]
    },


    "Xpeng": {
        "id": "4",
        "ticker": "XPNG",
        "logo": "https://imgs.search.brave.com/nYBs5aPeCS00bfklsrZwgiBpfJ5T9AXsy6-0owAE_2A/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/d2lrLmNvbS9jb250/ZW50L3VwbG9hZHMv/aW1hZ2VzL3hwZW5n/LW1vdG9yczgzMjAu/anBn",
        
        "description": "Xpeng Motors is a Chinese electric vehicle manufacturer "
        "focused on smart, high-tech EVs with advanced autonomous driving "
        "capabilities. Founded in 2014 by He Xiaopeng, the company aims to "
        "compete with Tesla in China by offering innovative software-driven "
        "vehicles with competitive pricing. Xpeng's lineup includes the X9 MPV, "
        "G9 and G6 SUVs, and P7 and P5 sedans, all featuring cutting-edge "
        "driver-assistance systems and in-house developed AI technology. With "
        "strong backing from investors like Alibaba and Volkswagen, Xpeng "
        "continues to expand its market presence in China and internationally.",

        "share_price": "$12.90",
        "models": ["X9", "G9", "G6", "P7", "P5", "G3i"]
    },

    "Nio" : {
        "id": "5",
        "ticker": "NIO",
        "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOWe4_MU7ya0J7iqLB1M4GBkwIlgcoF1-y5g&s",
        
        "description": "Nio is a Chinese electric vehicle manufacturer "
        "specializing in premium smart EVs with a strong focus on autonomous "
        "driving and battery-swapping technology. Founded in 2014 by "
        "William Li, the company has positioned itself as a competitor to "
        "Tesla in China's luxury EV market. Nio's lineup includes three sedans, "
        "along with the 5 SUVs, all featuring cutting-edge driver-assistance systems."
        "With significant backing from Chinese state-owned funds and "
        "international investors, Nio continues to expand its battery-swapping "
        "infrastructure and global presence.",

        "share_price": "$4.63",
        "models": ["ET9", "ET7", "ET5", "EC6", "EC7", "ES6", "ES7", "ES8"]
    
    },

    "Ford": {
        "id": "6",
        "ticker": "F",
        "logo": "https://imgs.search.brave.com/JVYFZ-BO5tdeClOS-bsys5zVucLV5Xh-P1AIzffH9HE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9j/L2M3L0ZvcmQtTW90/b3ItQ29tcGFueS1M/b2dvLnBuZw",
        "description": "Ford, one of the oldest and most iconic automakers, "
        "has made a strong push into the electric vehicle market while "
        "maintaining its legacy in combustion and hybrid vehicles. Under "
        "the leadership of CEO Jim Farley, Ford's EV lineup includes the "
        "Mustang Mach-E SUV and the F-150 Lightning, an all-electric "
        "version of America's best-selling truck. Ford has also invested "
        "heavily in battery technology, with plans for new EV platforms "
        "and the development of its BlueOval battery plants in partnership "
        "with SK Innovation. With a focus on scaling EV production, "
        "Ford aims to challenge Tesla and legacy automakers in the growing "
        "electric market while leveraging its strong brand loyalty.",

        "share_price": "$23.85",
        "models": ["Mustang Mach-E", "F-150 Lightning"]
    },

    "Li Auto": {
        "id": "7",
        "ticker": "LI",
        "logo": "https://p.ampmake.com/fed/image/png/d4e456eef7dbf961f28cba4f4c42b7a2.png",
        "description": "Li Auto is a Chinese electric vehicle manufacturer specializing "
        "in extended-range electric vehicles (EREVs), which combine battery-powered "
        "drivetrains with small gasoline generators for increased range. Founded in "
        "2015 by Li Xiang, the company targets China's premium SUV market with models "
        "like the L6, L7, L8, and L9, offering advanced driver-assistance technology "
        "and spacious, tech-focused interiors. Li Auto's upcoming Mega model marks its "
        "first step into fully battery-electric vehicles (BEVs) as it expands beyond "
        "range-extended hybrids. With strong financial backing and a focus on efficiency "
        "and practicality, Li Auto is rapidly growing its presence in China's competitive "
        "EV market.",

        "share_price": "$11.89",
        "models": ["L6", "L7", "L8", "L9", "Mega"]
    },

    "BYD": {
        "id": "8",
        "ticker": "BYD",
        "logo": "https://imgs.search.brave.com/TYs1yIhzJqNvzMCx1C0wZ_Vm8G_BSDDRXc7ZPV44WCE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuc2Vla2xvZ28u/Y29tL2xvZ28tcG5n/LzQ3LzIvYnlkLWNv/bXBhbnktbHRkLWxv/Z28tcG5nX3NlZWts/b2dvLTQ3MzkzNi5w/bmc",
        "description": "BYD (Build Your Dreams) is a Chinese automaker and battery "
        "manufacturer that has grown into the world's largest EV producer by volume. "
        "Founded in 1995 by Wang Chuanfu, BYD started as a battery company before "
        "transitioning into electric vehicles, leveraging its expertise in lithium-iron "
        "phosphate (LFP) battery technology. The company's EV lineup includes sedans "
        "like the BYD Han, as well as a broad range of electric buses, commercial vehicles, "
        "and affordable passenger cars aimed at global markets. With strong backing from "
        "investors like Warren Buffett’s Berkshire Hathaway, BYD continues to expand its "
        "global footprint, competing with Tesla and legacy automakers in both China and "
        "international markets.",

        "share_price": "$3.40",
        "models": ["BYD Han"]
    },

    "Faraday Future": {
        "id": "9",
        "ticker": "FFIE",
        "logo": "https://imgs.search.brave.com/2OqTDx9JTb-f37h3r0bJX6rDZXksQxrFkJ8GwpJtMbM/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzg5LzI0/L2RiLzg5MjRkYjYz/NTNjZjMzNTRiNjc2/OGM1Zjc3NmJjNzBk/LmpwZw",
        "description": "Faraday Future is an American electric vehicle startup focused "
        "on developing ultra-luxury, high-performance EVs with advanced connectivity and "
        "AI-driven features. Founded in 2014 by Chinese entrepreneur Jia Yueting, the "
        "company has faced financial struggles but continues to push forward with its "
        "flagship model, the FF 91 2.0 series. Faraday Future's lineup includes the "
        "FF 91 2.0, FF 91 2.0 Futurist, and FF 91 2.0 Futurist Alliance, all designed "
        "for a premium, tech-centric user experience. Despite ongoing challenges, the "
        "company aims to disrupt the luxury EV market with its futuristic design, "
        "powerful performance, and cutting-edge technology.",

        "share_price": "$2.33",
        "models": ["FF 91 2.0", "FF 91 2.0 Futurist", "FF 91 2.0 Futurist Alliance"]
    },

    "Dodge": {
        "id": "10",
        "ticker": "STLA",
        "logo": "https://imgs.search.brave.com/tPh_jbCiq2o-Q4tCjzDfHYJHKbmrykvo3P7gz03l9As/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9kaS11/cGxvYWRzLWRldmVs/b3BtZW50LmRlYWxl/cmluc3BpcmUuY29t/L2tlbmRhbGxkb2Rn/ZWNocnlzbGVyamVl/cHJhbTEvdXBsb2Fk/cy8yMDE4LzAxL0Rv/ZGdlX0xvZ28xLmpw/Zw",
        "description": "Dodge, a brand under Stellantis, is known for its "
        "high-performance muscle cars and is now transitioning into the EV market "
        "with electrified models. Originally founded in 1900 by the Dodge brothers, "
        "the company has built a reputation for powerful vehicles like the Charger "
        "and Challenger. Dodge's first major EV effort includes the Charger Daytona, "
        "an all-electric muscle car that retains the brand’s aggressive styling and "
        "performance-focused DNA, alongside the Hornet R/T plug-in hybrid. With "
        "Stellantis investing heavily in electrification, Dodge aims to balance its "
        "heritage of raw power with the future of electric mobility.",

        "share_price": "$35.27",
        "models": ["Charger Daytona", "Hornet R/T"]
    }
}

# NICK FELIX CODE YAY HELLO I'M NICK

favorites_names = random.sample(list(ev_companies.keys()), 3)

# Create a list of dictionaries with the company name included
favorites_data = [{"name": name, **ev_companies[name]} for name in favorites_names]

# ROUTES

@app.route('/')
def home():
   return render_template('home.html', ev_companies=ev_companies, favorites=favorites_data)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query", "").strip().lower()
    if not query:
        return render_template("search_results.html", results=[], query=query, result_count=0)

    # Search in title (name), ticker, and description
    results = [
        {**data, "name": name}  # Add name to data dictionary
        for name, data in ev_companies.items()
        if query in name.lower() or query in data["ticker"].lower() or query in data["description"].lower()
    ]

    return render_template("search_results.html", results=results, query=query, result_count=len(results))

@app.route('/view/<id>')
def view_company(id):
    # Find the company with the matching ID
    for name, data in ev_companies.items():
        if data["id"] == id:
            company_name = name
            company_data = data
            break

    if company_data is None:
        return "Company not found", 404
    
    company_data = {**company_data, "name": company_name}

    return render_template("info.html", company=company_data)

@app.route('/add', methods=['GET'])
def add_form():
    """Render the form for adding a new company."""
    return render_template("add.html")

@app.route('/add', methods=['POST'])
def add_company():
    """Handle form submission and add a new company."""
    data = request.get_json()

    # Validate input fields
    name = data.get("name", "").strip()
    ticker = data.get("ticker", "").strip().upper()
    logo = data.get("logo", "").strip()
    description = data.get("description", "").strip()
    share_price = data.get("share_price", "").strip()
    models = [m.strip() for m in data.get("models", "").split(",") if m.strip()]

    errors = {}

    # Error handling
    if not name:
        errors["name"] = "Company name is required."
    if not ticker:
        errors["ticker"] = "Ticker symbol is required."
    if not logo:
        errors["logo"] = "Logo URL is required."
    if not description or len(description) < 20:
        errors["description"] = "Description must be at least 20 characters long."
    if not share_price or not share_price.replace(".", "", 1).isdigit():
        errors["share_price"] = "Share price must be a valid number."
    if not models:
        errors["models"] = "At least one model is required."

    # If errors exist, return them
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    # Create unique ID
    new_id = str(len(ev_companies) + 1)

    # Add to dictionary
    ev_companies[name] = {
        "id": new_id,
        "ticker": ticker,
        "logo": logo,
        "description": description,
        "share_price": f"${share_price}",
        "models": models
    }

    return jsonify({"success": True, "id": new_id})




if __name__ == '__main__':
   app.run(debug = True, port=5001)