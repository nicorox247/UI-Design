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
        "logo" : "Link",
        "description": 
        "Rivian is an American electric vehicle manufacturer focused on
        adventure-oriented EVs and sustainable transportation solutions. 
        The company offers the R1T electric pickup truck, the R1S electric SUV, 
        and has announced the upcoming R2 and R3 models aimed at a broader market. 
        Rivian has received significant investment from major players such as Amazon 
        and Ford, with Amazon also securing an exclusive contract for Rivian's 
        electric delivery vans. With a strong emphasis on battery technology, 
        rugged capability, and software innovation, Rivian is positioning 
        itself as a competitor to Tesla and legacy automakers in the EV space.",
        "share_price" : "$12.00",
        "models" : ["R1S", "R1T", "R2", "R3"]
    },

    "Tesla" : {
        "id" : "2",
        "ticker" : "TSLA",
        "logo" : "Link",
        "description": "Tesla is an American electric vehicle and clean energy 
        company founded in 2003 by Martin Eberhard and Marc Tarpenning, with 
        Elon Musk joining shortly after as an early investor and later becoming CEO.\n
        The company revolutionized the EV market with high-performance electric cars 
        and cutting-edge battery technology.\nTesla's lineup includes the Model S, 
        Model 3, Model X, Model Y, and the recently launched Cybertruck, with future 
        models like the Roadster and Semi in development.\nWith a strong focus on 
        autonomous driving, energy storage, and sustainable technology, Tesla 
        continues to lead the industry in innovation and market dominance.",
        "share_price" : "$120.00",
        "models" : ["Model X", "Model Y", "Model S", "Model 3", "Cybertruck"]

    },

    "Lucid Motors": {
        "id": "3",
        "ticker": "LCID",
        "logo": "Link",

        "description": "Lucid Motors is an American electric vehicle manufacturer 
        known for producing luxury EVs with cutting-edge technology and 
        industry-leading range.\nFounded in 2007 as Atieva, the company initially 
        focused on battery technology before shifting to high-performance EV 
        production under CEO Peter Rawlinson, a former Tesla engineer.\nLucid's 
        flagship model, the Air, boasts one of the longest ranges of any EV, 
        while the upcoming Gravity SUV aims to expand its presence in the premium 
        EV market.\nBacked by significant investment from Saudi Arabia's Public 
        Investment Fund (PIF), Lucid is positioning itself as a strong competitor 
        to Tesla and other luxury automakers.",

        "share_price": "$2.30",
        "models": ["Air", "Gravity"]
    },


    "Xpeng": {
        "id": "4",
        "ticker": "XPNG",
        "logo": "Link",
        
        "description": "Xpeng Motors is a Chinese electric vehicle manufacturer 
        focused on smart, high-tech EVs with advanced autonomous driving 
        capabilities.\nFounded in 2014 by He Xiaopeng, the company aims to 
        compete with Tesla in China by offering innovative software-driven 
        vehicles with competitive pricing.\nXpeng's lineup includes the X9 MPV, 
        G9 and G6 SUVs, and P7 and P5 sedans, all featuring cutting-edge 
        driver-assistance systems and in-house developed AI technology.\nWith 
        strong backing from investors like Alibaba and Volkswagen, Xpeng 
        continues to expand its market presence in China and internationally.",

        "share_price": "$120",
        "models": ["X9", "G9", "G6", "P7", "P5", "G3i"]
    }

    "Nio" : {
        "id": "5",
        "ticker": "NIO",
        "logo": "Link",
        "description": "Nio is a Chinese electric vehicle manufacturer 
        specializing in premium smart EVs with a strong focus on autonomous 
        driving and battery-swapping technology.\nFounded in 2014 by 
        William Li, the company has positioned itself as a competitor to 
        Tesla in China's luxury EV market.\nNio's lineup includes three sedans, 
        along with the 5 SUVs, all featuring cutting-edge driver-assistance systems.
        \nWith significant backing from Chinese state-owned funds and 
        international investors, Nio continues to expand its battery-swapping 
        infrastructure and global presence.",
        "share_price": "$4.63",
        "models": ["ET9", "ET7", "ET5", "EC6", "EC7", "ES6", "ES7", "ES8"]
    
    },

    "Ford": {
        "id": "6",
        "ticker": "F",
        "logo": "Link",
        "description": "Ford, one of the oldest and most iconic automakers, 
        has made a strong push into the electric vehicle market while 
        maintaining its legacy in combustion and hybrid vehicles.\nUnder 
        the leadership of CEO Jim Farley, Ford's EV lineup includes the 
        Mustang Mach-E SUV and the F-150 Lightning, an all-electric 
        version of America's best-selling truck.\nFord has also invested 
        heavily in battery technology, with plans for new EV platforms 
        and the development of its BlueOval battery plants in partnership 
        with SK Innovation.\nWith a focus on scaling EV production, 
        Ford aims to challenge Tesla and legacy automakers in the growing 
        electric market while leveraging its strong brand loyalty.",
        "share_price": "$120",
        "models": ["Mustang Mach-E", "F-150 Lightning"]
    }
    "Li Auto": {
        "id": "7",
        "ticker": "LI",
        "logo": "https://p.ampmake.com/fed/image/png/d4e456eef7dbf961f28cba4f4c42b7a2.png",
        "description": "Li Auto is a Chinese electric vehicle manufacturer specializing 
        in extended-range electric vehicles (EREVs), which combine battery-powered 
        drivetrains with small gasoline generators for increased range.\nFounded in 
        2015 by Li Xiang, the company targets China's premium SUV market with models 
        like the L6, L7, L8, and L9, offering advanced driver-assistance technology 
        and spacious, tech-focused interiors.\nLi Auto's upcoming Mega model marks its 
        first step into fully battery-electric vehicles (BEVs) as it expands beyond 
        range-extended hybrids.\nWith strong financial backing and a focus on efficiency 
        and practicality, Li Auto is rapidly growing its presence in China's competitive 
        EV market.",
        "share_price": "$120",
        "models": ["L6", "L7", "L8", "L9", "Mega"]
    }

    "BYD": {
        "id": "8",
        "ticker": "BYD",
        "logo": "Link",
        "description": "BYD (Build Your Dreams) is a Chinese automaker and battery 
        manufacturer that has grown into the world's largest EV producer by volume.
        \nFounded in 1995 by Wang Chuanfu, BYD started as a battery company before 
        transitioning into electric vehicles, leveraging its expertise in lithium-iron 
        phosphate (LFP) battery technology.\nThe company's EV lineup includes sedans 
        like the BYD Han, as well as a broad range of electric buses, commercial vehicles, 
        and affordable passenger cars aimed at global markets.\nWith strong backing from 
        investors like Warren Buffett’s Berkshire Hathaway, BYD continues to expand its 
        global footprint, competing with Tesla and legacy automakers in both China and 
        international markets.",
        "share_price": "$120",
        "models": ["BYD Han"]
    }

    "Faraday Future": {
        "id": "9",
        "ticker": "FFIE",
        "logo": "Link",
        "description": "Faraday Future is an American electric vehicle startup focused 
        on developing ultra-luxury, high-performance EVs with advanced connectivity and 
        AI-driven features.\nFounded in 2014 by Chinese entrepreneur Jia Yueting, the 
        company has faced financial struggles but continues to push forward with its 
        flagship model, the FF 91 2.0 series.\nFaraday Future's lineup includes the 
        FF 91 2.0, FF 91 2.0 Futurist, and FF 91 2.0 Futurist Alliance, all designed 
        for a premium, tech-centric user experience.\nDespite ongoing challenges, the 
        company aims to disrupt the luxury EV market with its futuristic design, 
        powerful performance, and cutting-edge technology.",
        "share_price": "$120",
        "models": ["FF 91 2.0", "FF 91 2.0 Futurist", "FF 91 2.0 Futurist Alliance"]
    }

    "Dodge": {
        "id": "10",
        "ticker": "STLA",
        "logo": "Link",
        "description": "Dodge, a brand under Stellantis, is known for its 
        high-performance muscle cars and is now transitioning into the EV market 
        with electrified models.\nOriginally founded in 1900 by the Dodge brothers, 
        the company has built a reputation for powerful vehicles like the Charger 
        and Challenger.\nDodge's first major EV effort includes the Charger Daytona, 
        an all-electric muscle car that retains the brand’s aggressive styling and 
        performance-focused DNA, alongside the Hornet R/T plug-in hybrid.\nWith 
        Stellantis investing heavily in electrification, Dodge aims to balance its 
        heritage of raw power with the future of electric mobility.",
        "share_price": "$120",
        "models": ["Charger Daytona", "Hornet R/T"]
    }
}